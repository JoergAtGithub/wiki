This is a support document to help explaining the state of [#13330](https://github.com/mixxxdj/mixxx/pull/13330) and the multiple design options for multiple beatgrid feature.

> [!NOTE]
> This document focuses on the the core principle behind multi grid implementation details (backend). No CO (frontend) is being covered, beside example one that may help understand how to interact with the final feature.

Glossary

- **Grid marker**: The start of a beat grid or the first beat of that new grid
- **Padding beat**: A space or dummy beat between two valid BPM grids

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
- Imperfect track such as live performance will need to have compensation grid with irrelevant BPM, translating the human imperfection

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
