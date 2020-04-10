**Visual Studio Code** is a free open source code editor / IDE that is
easy to set-up.  
It is a completely different editor than [Visual Studio
Community](Visual%20Studio%20Community), which is easier to use for some
languages (Used a lot for javascript/TypeScript development)

Follow this instructions to set-up Visual Studio Code for Mixxx
development.

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

<!-- end list -->

1.  Configure the c++ extension to enable code completion.
    1.  Create a folder named .vscode in the mixxx root folder (if not
        already created).
    2.  Inside this folder, create a file named settings.json (if not
        already created).
    3.  Add the following content to this file: `{
                                        "C_Cpp.default.cStandard": "c11",
                                        "C_Cpp.default.cppStandard": "c++11",
                                        "C_Cpp.default.compileCommands":
        "${workspaceFolder}/compile_commands.json"
        }
        `

\[1\]

1.  [Building your C++ application with Visual Studio
    Code](https://devblogs.microsoft.com/cppblog/building-your-c-application-with-visual-studio-code/)
