# Setting up Visual Studio Code for Mixxx development

**Visual Studio Code** is a free open source code editor / IDE that is
easy to set-up.  
It is a completely different editor than [Visual Studio
Community](Visual%20Studio%20Community).  
VSCode is very well suited for [Controller Scripting](midi_scripting) as
well as [working on Mixxx's core with
C++](start#developer_documentation).

## Setting up VScode for C++

Note: Most of this guide will assume that you have a folder named
\`cbuild\` in the root folder of the locally cloned repository. This is
where cmake will put the buildfiles and build the mixxx binary. If you
want to use a different folder, you need to adapt the paths present in
the config file templates given.

1.  Check out Mixxx source and build it.

<!-- end list -->

  - If you haven't done this yet, follow the instructions for your
    operating system [here](start#compile_mixxx_from_source_code).

<!-- end list -->

1.  Install Microsoft C/C++ extension.
    1.  Open the extensions pane and search for "c++". Click the install
        button for the Microsoft extension.
        [[/media/code_install_c_etension.png|]]
2.  Select File -\> Open... and open the mixxx source folder.

<!-- end list -->

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

Use the following \`tasks.json\` config (located in \`.vscode\`) to be
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
                "-DOPTIMIZE=native",
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
            "problemMatcher": []
        }
    ]
}
```

This will add the "CMake generate buildfiles" and "CMake compile" tasks
to VScode. Both can be invoked in the command prompt accessible via
\[CTLR\]+\[Shift\]+P. The "CMake compile" can also be invoked directly
by pressing \[CTLR\]+\[Shift\]+B.

### Debugging

Add this to your \`launch.json\` file to add debugging capabilities
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
\`F5\`. If you want to know more about debugging, Microsoft has a guide
which introduces to into VScodes debugging capabilities:
<https://code.visualstudio.com/docs/editor/debugging>

\[1\]

1.  [Building your C++ application with Visual Studio
    Code](https://devblogs.microsoft.com/cppblog/building-your-c-application-with-visual-studio-code/)
