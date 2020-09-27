## Preferences redesign
Required skills:
  * C++ - beginner skill level is okay, but need to have at least a little experience with the language

Preferred skills:
  * UI design
  * UX testing

Nice to have skills:
  * DJing
  * Qt Designer

Mixxx is a large, complex application with lots of options that users can configure. Over the years, this has made the preferences window rather unwieldy. This project would entail redesigning the preferences to make it easier for users to find what they are searching for as well as understand what every option does and why someone might want to change it. In some cases this may lead to changing the behavior of Mixxx so options are no longer required and/or moving options out of the preferences window.

## Touchscreen UX design
Required skills:
  * C++ - beginner skill level is okay, but must have more experience with other programming languages in that case
  * having a touchscreen device that can run Mixxx

Preferred skills:
  * designing for touchscreens

Nice to have skills:
  * DJing or other experience using electronic music equipment

Generally, Mixxx users use DJ controller hardware because it is difficult to manipulate Mixxx fast enough while music is playing using just a keyboard and mouse. Nowadays, many laptops have touchscreens. Also, some users are using Mixxx with tablets or single board computers (such as Raspberry Pi and Odroid devices) together with a touchscreen and controller. However, Mixxx's GUI was designed before touchscreens were common and there are many ways it is difficult to use with only a touchscreen without relying on a mouse.

This project would entail making Mixxx's features practically usable with a touchscreen. The goal is not necessarily to fully replace a controller, but to make it practical to do basic mixing with just a touchscreen and to compliment controllers. Some features are currently only accessible through right click menus so alternative ways to use these would need to be designed and implemented. The project will also require changing the behavior of Mixxx's custom QWidgets to properly handle touch input. Some changes to Mixxx's skins may be required too.

## Video tutorials
Required skills:
  * screen capturing
  * video editing

Preferred skills:
  * DJing with a controller so footage of this can be combined with screen capture video

New users are often overwhelmed and do not know how to get started using Mixxx. This project would entail making tutorial videos explaining Mixxx's features and demonstrating how to use them with real examples.

## Screenreader UX
Required skills:
  * C++ / QT programming
  * experience using screenreader software

Nice to have skills:
  * QAccessibleInterface
  * QWidgets

Some blind and visually impaired users use Mixxx with screenreader software. However, Mixxx was not designed with screenreaders in mind so many features are cumbersome or impossible to use with screenreaders. This project would entail making Mixxx practically usable with screenreader software.