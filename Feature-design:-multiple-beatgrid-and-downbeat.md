This is a support document to help explaining the state of [#13330](https://github.com/mixxxdj/mixxx/pull/13330) and the multiple design options for multiple beatgrid feature.

> [!NOTE]
> This document focuses on the the core principle behind multi grid implementation details (backend). No CO (frontend) is being covered, beside example one that may help understand how to interact with the final feature.

Glossary

- **Grid marker**: The start of a beat grid or the first beat of that new grid
- **Padding beat**: A space or dummy beat between two valid BPM grids
- **Overshoot**: A beat which is played **after** where it should be due to human imperfection
- **Undershoot**: A beat which is played **before** where it should be due to human imperfection

# Design 1: theory meeting the practice

> TL;DR; a track always contains a round number of beat, at various BPM.

This was the original design this feature was implemented with and how preceding PRs for this feature approach the problem. Adding a new grid marker will ensure the beat count will remain round. This means in practice it will either:
- Shift grid and keep the BPM unchanged
- Scale and readjust the BPM

When a grid is bounded by two markers, explicitly defined by the user, this means either of the following:
- The BPM cannot be granularly adjusted 
- New adjacent grids will only be able to change their own BPM and cannot shift grids

Main benefits:
- Align with music theory

Main flaws:
- Imperfect track such as live performance will need to have compensation grid with irrelevant BPM, translating the human imperfection.

<details>
  <summary>previous long explanation</summary>

> A padding region (to translate human imperfection often present on non electronic music) will need a dummy BPM which will impact deck synching since this will add an extra beat. For example say you have a two 16-bars at 120 BPM on deck A, and a track on deck B sync'ed, with a slight imperfection, say a 1/10 of a beat beetween the two bars. With padding beats, you will still have ~32 beats, and thanks the our "nearest beat" sync system, synching with another track will keep it align to the other decks's 16-bar, making the imperfection almost inaudible. Without that padding beat, you will have 33 beats (32 beats at 120BPM and a beat at 1200BPM), and thus the track will be off by one beat. When you listen to it, track B will suddenly get a BPM of 1200 for half a second in order to get stay align with that "dummy beat" and the second bear will be off by one. 

</details>

Here are animations which illustrate the long explanation before:

> [!NOTE]
> The triangles represent the actual beat (e.g a kick drum) 

- In case of an undershoot, the transport is okay, but the bar/downbeat will have to appear incorrect  

  ![design_1_offset_undershoot](https://github.com/user-attachments/assets/3189780c-fe71-4f83-bcb2-f9e9f1a0841e)
- In case of an overshoot, the follower's track BPM will increase drastically during the beat offset and will let to an off-by-one problem

  ![design_1_offset_overshoot](https://github.com/user-attachments/assets/d62aaf51-895d-44d3-aa7a-3627eabc5f8d)

  Note that the alternative of scaling the last bar to "drawn" the imperfection on 4 beats (which is what Serato tutorial are suggestion AFAIU) will still lead to poor audio result

  ![design_1_scale_bar](https://github.com/user-attachments/assets/670115e6-e8b1-4511-9e68-32f6ca848221)




In technical terms, it means that a grid is defined by:
- its start
- its beat count
- its end or BPM


# Design 2: grid have their BPM

> TL;DR; a track is composed of multiple grids with their own BPM, they may be inferred from theory but they also have the ability to provide a non round number of beats

Adding a new grid marker will ensure adjacent area can remains untouched. This means in practice it is capable introduce non round number of beats of the previous grid and on the newly created grid. There is however nothing preventing it to adjust the previous and new grids BPM in order to keep the number of beat round.

Main benefits:
- Also compatible with music theory
- Doesn't introduce fake beat to translate imperfection

Main flaws:
- Non round number of beat will appear as padding beat, which may be confusing for users who want Mixxx to behave in a theory perfect way

In order to help comparing with the flaws of Design 1, here are animations which illustrate the different usecases:

> [!NOTE]
> The triangles represent the actual beat (e.g a kick drum) 

- In case of an undershoot

  ![design_2_offset_undershoot](https://github.com/user-attachments/assets/d5e30b99-2804-4e56-a858-e5ac343092a2)


- In case of an overshoot

  ![design_2_offset_overshoot](https://github.com/user-attachments/assets/956e77c8-e0a6-40a1-b867-56beb1999a4c)


In technical terms, it means that a grid is defined by:
- its start
- its beat length or BPM

# FAQ

## Is it correct, that the beatgrid syntax will be the same with both approaches, and only additional beats will occur?

This is kind of correct:

- With **Design 1**, adding a new beat marker will not create a beat but instead will stretch the beatgrid and mutate the BPM of the left region (relative to the play pos), and shift the right grid. We could imaging edge case where a beat is created, but the side effect will remain the same. 
- With **Design 2**, new beatgrid marker will create beat if created between two existing beats, otherwise the existing beat will be "promoted" to a marker, meaning a new grid staring point, indepedent to ajacent grid change

## Is it correct, that these additional beats can be removed/added by manual postprocessing with both approaches?

Not quite. Both of these changes can be added by manual postprocessing but **Design 1** doesn't really allow removing them since it mutates the BPM and/or all grids position following within the track.
We could imagine adding this to the undo action, but that is more work, unrelated to the backend design.

## Is it correct, that both functions could be implemented next to each other, because they use the same beatgrid format?

Absolutely, and this was the plan. When #13330 was submitted, we discussed about having a CO (frontend) going forward to explicitly mutate the BPM and scale the previous grid to the new added marker (basically not padding it, and mimicking the **Design 1**'s behaviour). As demoed in the PR, this is not a blocker to only have **Design 2**'s default behaviour, as changing the BPM of the grid will eventually remove the padding/round up the number of beat, just requires further CO interaction (a few clicks) currently. As per the discussion, we've added everything to allow iterating on this and add this option later on, to do it as an atomic operation.

## Do you see any issues with import/export of Serato or Traktor 4 beatgrid tracks? And if yes, with which approach?

In theory , Serato (and Traktor 4) appears to be using **Design 2** so there is no problem with serialisation/deserialisation with these data. As mentioned above, **Design 2** is entirely to be compatible with **Design 1**, this means that when padding beats are used, they will be tramslated to  "dummy" grid with an irrelevant BPM value, usually very off the actual value. This is how unit test are currently written.
Now, this was neither tested with Serato nor Traktor 4 yet.
