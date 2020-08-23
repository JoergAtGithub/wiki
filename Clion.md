CLion is a **commercial** Cross-Platform IDE for C and C++ by JetBrains.

JetBrains supports non-commercial open-source projects by providing
licenses to contributors free of charge. You can apply
[here](https://www.jetbrains.com/community/opensource/#support).

# Prerequisites

**macOS**

Follow [Compiling on macOS](compiling_on_os_x), steps 1 to 3 to install
Mixxx dependencies **using Homebrew** and get the Mixxx source code.

# Step-by-Step Setup

*Tested on CLion 2020.1*

## Build configuration

Open CLion.

Select **Open** in the welcome window:

[[/media/clion_2019-3-5_welcome_screen.png|]]

Navigate to the mixxx source folder, select the `CMakeLists.txt` file
and click **Open**.

Select **Open as Project**:

[[/media/clion_2019-3-5_open_dialog.png|]]

Open the preferences window and navigate to **Build, Execution,
Deployment** \> **CMake**.

Add the following options to the **CMake options** field:

**macOS**

    -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR=/usr/local/opt/qt5/cmake/Qt5/ -DCMAKE_PREFIX_PATH=/usr/local/opt/

Set the **Generation path** field to `cmake_build`:

[[/media/clion_2019-3-5_build_options_generation_path.png|]]

CLion will generate the build files in this folder, which will be
created in the root path of the project. Don't commit this folder.
Configure git to exclude it. Open `.git/info/exclude` and append
`cmake_build/` in a new line.

Click **OK** to save the changes and close the preferences window.

Select **mixxx** on the Run configuration drop-down menu:

[[/media/clion_2020-1_run_configuration.png|]]

Press the Build button to build Mixxx\! [[/media/clion_build_button.png|]]

## Run configuration

Clion automatically detects the built mixxx binary.

Open **Run \> Edit Configurations...** and select **mixxx** on the
left-side list. Add the following arguments to the **Program arguments**
field:

    --resourcePath res --settingsPath settings --developer --controllerDebug --debugAssertBreak

[[/media/clion_2020-1_edit_run_configurations.png|]]

Press the Run button to run Mixxx\! [[/media/clion_run_button.png|]]
