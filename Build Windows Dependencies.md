# Notes for building Mixxx's dependencies on Windows

We assume you've installed and configured Visual Studio Express and the
Microsoft Platform SDK as described in steps 1 & 2 [on this
page](compiling_on_windows), and if you want to build x64 versions with
the free Visual Studio Express, that you've done [this
hack](http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html).

## PortAudio

PortAudio provides MSVC project files, which makes things nice. Just
have the DirectX SDK installed and open and build. (Step-by-step is
given below.)

### x64 prep for VS Express

If you're doing an x64 build with VS Express, you'll first need to
change some things in the vcproj and sln file in a text editor before
you open them in VS:

1.  For the `portaudio\build\msvc\portaudio.sln` file:
    1.  Replace all instances of "Win32" (case-sensitive) with
        "DontWantThis" or something similar
    2.  Then replace all instances of "x64" with "Win32"
2.  For the `portaudio\build\msvc\portaudio.vcproj` file:
    1.  Change the line that says \<code=xml\> \<Configurations\>

<!-- end list -->

``` 
      <Configuration
          Name="Release|Win32"</code> to <code=xml>   <Configurations>
      <Configuration
          Name="Release|DontWantThis"</code>
  - Then change the similar ''Name="Release|x64"'' line to ''Name="Release|Win32"'' in the ''<Configuration'' below that one.
  - Don't worry about stuff below that since they all do the same thing regardless of the platform (at the time of writing (July 2009) at least.)
```

### To build

1.  Download and install the latest DirectX SDK:
    <http://msdn.microsoft.com/en-us/directx/aa937788.aspx>
2.  Start the platform SDK command prompt (Start→Microsoft Windows
    SDK→CMD Shell)
3.  Type `setenv /xp /x64 /release` and hit Enter.
4.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
5.  Add the DirectX SDK paths to the compiler:
    1.  Go to Tools-\>Options-\>Projects and Solutions-\>VC++
        Directories
    2.  Choose "Include files" on the right and add the path to the
        DirectX SDK Include directory, e.g. `C:\Program Files\Microsoft
        DirectX SDK (March 2009)\Include`
    3.  Choose "Library files" on the right and add the path to the
        DirectX SDK Library directory, e.g. `C:\Program Files\Microsoft
        DirectX SDK (March 2009)\Lib\x86`
    4.  Click OK.
6.  Open the portaudio\\build\\msvc\\portaudio.vcproj file via
    File-\>Open-\>Project/Solution. After doing the upgrade, you'll only
    see "Win32" targets if you're using VS Express. (If you've made the
    changes to the project files given above, building these will
    actually give you x64 versions. We had to do it this way otherwise
    VS Express would see the x64 targets in the file and refuse to make
    them available to you, since that's a premium feature of non-free
    versions of VS.)
7.  Choose the Release configuration and the Win32 platform
8.  Press F7 to build
9.  When it finishes, copy the following files into `mixxx-winlib` or
    `mixxx-win64lib`: `portaudio\include\portaudio.h
    portaudio\build\msvc\Win32\Release\portaudio.dll (or
    portaudio_x64.dll)
    portaudio\build\msvc\Win32\Release\portaudio.lib (or
    portaudio_x64.lib but rename it to portaudio.lib)
    `

#### Troubleshooting

  - If you get the error `..\..\src\hostapi\asio\pa_asio.cpp(1167) :
    error C2440: '=' : cannot convert from 'FARPROC' to
    'IsDebuggerPresentPtr'
                                    This conversion requires a reinterpret_cast, a C-style cast or
    function-style cast` open `portaudio\src\hostapi\asio\asio.cpp` and
    change the line:`IsDebuggerPresent_ = GetProcAddress( LoadLibrary(
    "Kernel32.dll" ), "IsDebuggerPresent" );` to `IsDebuggerPresent_ =
    IsDebuggerPresentPtr(GetProcAddress( LoadLibrary( "Kernel32.dll" ),
    "IsDebuggerPresent" ));` then build again.
