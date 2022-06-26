# Setting up Visual Studio Code for Mixxx development

**Visual Studio Code** is a free open source code editor / IDE that is
easy to set-up. VS code runs on Windows, Linux and MacOS.<br>
VSCode is very well suited for [Controller Scripting](midi_scripting) as
well as [working on Mixxx's core with C++](home#developer_documentation).

_Note, that VSCode is a completely different editor than 'Visual Studio', which is also available as a free (but closed source) [Community Edition](Visual%20Studio%20Community).<br>
If you intend to build Mixxx on Windows, use the Visual Studio 2019 (Community Edition) as described [here](Compiling-On-Windows)!_

## Setting up VScode for C++

Note: Most of this guide will assume that you have a folder named
`cbuild` in the root folder of the locally cloned repository. This is
where cmake will put the buildfiles and build the mixxx binary. If you
want to use a different folder, you need to adapt the paths present in
the config file templates given.

1.  Check out Mixxx source and build it.
    - If you haven't done this yet, follow the instructions for your
    operating system [here](home#compile_mixxx_from_source_code).
2.  Create an empty folder `cbuild` in the root folder of the locally cloned repository.
3.  Install Microsoft C/C++ extension.
    -  Open the extensions pane and search for "c++". Click the install
        button for the Microsoft extension.

        [[/media/code_install_c_etension.png|]]
4.  Select File -\> Open... and open the mixxx source folder.
    - Visual Studio Code saves it's configuration in a folder named
      .vscode in the mixxx source folder. Next time you want to work on
      mixxx you only need to open the mixxx source folder again.

### Enabling autocompletion

Put the following text into your \`c\_cpp\_properties.json\` (or create
it if it doesn't exist already) into the \`.vscode\` folder.

``` javascript
{
    "configurations": [
        {
            "name": "Linux",
            "compilerPath": "/usr/bin/gcc",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "gcc-x64",
            "compileCommands": "${workspaceFolder}/cbuild/compile_commands.json"
        }
    ],
    "version": 4
}
```

For this to properly work, its important to enable generation of the
compilation database while running CMake. The build and config tasks
following do this automatically for you.

### Compiling

Unfortunately, I'm not able to create configs for building Mixxx through
VScode on anything other than Linux. So this section assumes you are
running VScode on Linux. You should also have read the [compiling on
linux guide with cmake](compiling_on_linux#cmake) to properly grasp the
following section.

#### Generating buildfiles and compiling mixxx

Use the following `tasks.json` config (located in `.vscode`) to be
able to generate buildfiles and compile linux from within VScode:

``` javascript
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "CMake generate buildfiles",
            "type": "shell",
            "group": "build",
            "options": {
                "cwd": "cbuild"
            },
            "command": "cmake",
            "args": [
                "-DCMAKE_INSTALL_PREFIX=/usr/local",
                // add any further arguments for CMake here
                
                // generate debug build
                "-DCMAKE_BUILD_TYPE=Debug",
                "-DDEBUG_ASSERTIONS_FATAL=ON",
                // generate compile_commands.json
                "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
                "${workspaceFolder}"
            ],
            "problemMatcher": []
        },
        {
            "label": "CMake compile",
            "type": "shell",
            "command": "cmake --build . --parallel $(nproc)",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "options": {
                "cwd": "cbuild"
            },
            "problemMatcher": "$gcc"
        }
    ]
}
```

This will add the "CMake generate buildfiles" and "CMake compile" tasks
to VScode. Both can be invoked in the command prompt accessible via
\[CTLR\]+\[Shift\]+P. The "CMake compile" can also be invoked directly
by pressing \[CTLR\]+\[Shift\]+B.

### Debugging

Add this to your `launch.json` file to add debugging capabilities
(based on gdb) to vscode.

``` javascript
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/cbuild/mixxx",
            "args": [
                "--resourcePath res/",
                "--debugAssertBreak"
                // add more args here (for example a custom --settingsPath)
            ],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

You should now be able to launch Mixxx with gdb attached by pressing
F5. If you want to know more about debugging, Microsoft has a guide
which introduces to into VScodes debugging capabilities:
<https://code.visualstudio.com/docs/editor/debugging>

Alse see [Building your C++ application with Visual Studio Code](https://devblogs.microsoft.com/cppblog/building-your-c-application-with-visual-studio-code/).

### Troubleshooting

#### When I try to build the code, VSCode fails with `The terminal shell CWD ".../mixxx/cbuild" does not exist`

the `cbuild` directory is the temporary directory where CMake will generate the files for the buildsystem you are using. Since
the name of this directory is theoretically up to you, but vscode needs to know about it. To simplify this guide, we assumed this directory will be called `cbuild`. However, it does not exist when you clone the mixxx repository the first time so you need to create it yourself.

#### `#include`s are underlined in orange and the tooltip says something like `#include errors detected. Consider updating your compile_commands.json or includePath. Squiggles are disabled for this translation unit.`

This occurs when you either have an outdated `compile_commands.json` (or its missing entirely). You can fix this by running the "CMake generate buildfiles" and "CMake compile" tasks at least once. Make sure you include `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` when generating the buildfiles (this is already the case if you use the `tasks.json` from above)