# Required Text Blocks

It's possible to fill out a lot of information about each project for Outreachy.  Not everything is required but it will help interns understand the projects.

* (required) Short Description with verb first, like "Improve User Manual"
* (required) Long Description
* (optional) Intern Tasks: A bullet list of example tasks to be done, including small starter tasks, main project-spanning task, and stretch goals.  Does not have to be complete
* (optional) Intern Benefits: What will the intern get out of this project?
* (optional) Community Benefits: What does Mixxx get out of this project?


Skill requirements are described following the [Outreachy project skills key](https://www.outreachy.org/apply/project-selection/#project-skills-key).


## Touchscreen UX design
Required skills:
  * 3: C++ - beginner skill level is okay, but must have more experience with other programming languages in that case
  * 5: having a touchscreen device that can run Mixxx (Mixxx does not run on Android or iOS)

Preferred skills:
  * 3: designing for touchscreens

Nice to have skills:
  * 3: DJing or other experience using electronic music equipment
  * 3: UX testing

Generally, Mixxx users use DJ controller hardware because it is difficult to manipulate Mixxx fast enough while music is playing using just a keyboard and mouse. Nowadays, many laptops have touchscreens. Also, some users are using Mixxx with tablets or single board computers (such as Raspberry Pi and Odroid devices) together with a touchscreen and controller. However, Mixxx's GUI was designed before touchscreens were common and there are many ways it is difficult to use with only a touchscreen without relying on a mouse.

This project would entail making Mixxx's features practically usable with a touchscreen. The goal is not necessarily to fully replace a controller, but to make it practical to do basic mixing with just a touchscreen and to compliment controllers. Some features are currently only accessible through right click menus so alternative ways to use these would need to be designed and implemented. The project will also require changing the behavior of Mixxx's custom QWidgets to properly handle touch input. Some changes to Mixxx's skins may be required too.

## Preferences redesign
Required skills:
  * 3: C++

Preferred skills:
  * 4: UI design
  * 2: UX testing

Nice to have skills:
  * 3: DJing
  * 3: Qt Designer

Mixxx is a large, complex application with lots of options that users can configure. Over the years, this has made the preferences window rather unwieldy. This project would entail redesigning the preferences to make it easier for users to find what they are searching for as well as understand what every option does and why someone might want to change it. In some cases this may lead to changing the behavior of Mixxx so options are no longer required and/or moving options out of the preferences window.

## Improve User Manual

### Long Description:

Mixxx's [user manual](https://manual.mixxx.org/) does a decent job explaining the application, however there is lots of room for improvement. Many users come to Mixxx without any prior experience DJing and are left wondering how to practically use the application to mix music. The manual could be improved by explaining not only how to set up Mixxx and how to use specific features, but also explaining the bigger picture of how to play music with Mixxx.

There is some information in the manual that is obvious or already explained in the application with tooltips; some of this may be deleted from the manual. Other text could be moved directly into the Mixxx GUI. The manual should focus on explaining information that would take too many words to adequately explain in the Mixxx GUI. Also, it would be helpful to add more links to specific sections of the manual from the Mixxx GUI (and maybe edit the manual text with this context in mind).

### Intern Tasks:

* ?

### Intern Benefits

Gain experience doing technical writing on a large, mature project.

Get to know Git on an active project with many contributors

Gain experience with markdown for formatting

### Community Benefits




Required skills:
  * 5: English writing

Preferred skills:
  * 4: DJing

Nice to have:
  * 3: Technical documentation writing


## Video tutorials
Required skills:
  * 3: screen capturing
  * 5: video editing

Preferred skills:
  * 4: DJing with a controller so footage of this can be combined with screen capture video

New users are often overwhelmed and do not know how to get started using Mixxx. This project would entail making tutorial videos explaining Mixxx's features and demonstrating how to use them with real examples.

## Screenreader UX
Required skills:
  * 3: C++ - beginner skill level is okay, but must have more experience with other programming languages in that case
  * 4: using screenreader software

Preferred skills:
  * 3: implementing screenreader accessible software

Nice to have skills:
  * 2: QAccessibleInterface
  * 2: QWidgets
  * 3: DJing

Some blind and visually impaired users use Mixxx with screenreader software. However, Mixxx was not designed with screenreaders in mind so many features are cumbersome or impossible to use with screenreaders. This project would entail making Mixxx practically usable with screenreader software.