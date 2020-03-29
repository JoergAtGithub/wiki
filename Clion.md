CLion is a **commercial** Cross-Platform IDE for C and C++ by JetBrains.

JetBrains supports non-commercial open-source projects by providing
licenses to contributors free of charge. You can apply
[here](https://www.jetbrains.com/community/opensource/#support).

# Step-by-Step Setup

For CLion 2019.3.5.

Open CLion.

Select **Open** in the welcome window:

[[/media/clion_2019-3-5_welcome_screen.png|]]

Navigate to the mixxx folder, select the `CMakeLists.txt` file and click
**Open**.

Select **Open as Project**:

[[/media/clion_2019-3-5_open_dialog.png|]]

Open the preferences window and navigate to **Build, Execution,
Deployment** \> **CMake**.

Add the following options to the **CMake options** field:

macOS:

``` 
  -DQt5_DIR=
```

Set the **Generation path** field to `cmake_build`:

[[/media/clion_2019-3-5_build_options_generation_path.png|]]

CLion will generate the build files in this folder, which will be create
in the root path of the project. Don't commit this folder. Configure git
to exclude it. Open `.git/info/exclude` and append `cmake_build` in a
new line.
