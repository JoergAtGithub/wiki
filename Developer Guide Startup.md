# Startup

## main.cpp

As all C++ programs usually do, Mixxx starts up with a `main` function
located in `src/main.cpp`. It looks roughly like this:

    int main(int argc, char** argv) { 
        // start up Mixxx
    }

You don't need to pay much attention to this section of the code. Most
of what it does is:

  - Initialize logging to file and some other minor things.
  - Initialize some Qt basics and plugin paths.
  - Interpret command line arguments
  - Create a `MixxxApp` class which is what starts up the rest of Mixxx.

## MixxxApp Class

`MixxxApp` is the class that ties everything Mixxx does together. Mixxx
is made up of a variety of subsystems that all accomplish different
purposes. You can find all of the code to `MixxxApp` in `src/mixxx.h`
and `src/mixxx.cpp`.

In earlier years, `MixxxApp` was in charge of way more than it should
have been. Over time we've tried to reduce the number of things it is
responsible for, but as of Summer 2012 it's still a whopping 1600 lines.

Among the things it does (in no particular order) are:

  - Initialize all of the Mixxx subsystems.
  - Shut-down all of the Mixxx subsystems at shutdown time.
  - Handle all of the menu-bar actions.
  - Control the transition into and out of fullscreen mode.
  - Keeps a list of all the contributors to Mixxx that are shown in the
    credits.
  - Install and setup translations. 
  - Load and save the Mixxx config file.
  - Initializes and displays the Mixxx GUI
