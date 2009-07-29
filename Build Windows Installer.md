# Making a Windows installer package

Mixxx uses the [NullSoft Install System](http://nsis.sourceforge.net/)
for building Windows self-extracting installers. This page contains
information on making such packages.

First, we assume you've built & run Mixxx successfully from the
instructions on the [Compiling on Windows](Compiling%20on%20Windows)
page.

## Preparation

When built with MSVC, Mixxx requires that certain MSVC DLL files be
present in order to run. Many people have these already installed on
their systems, but many do not (or have different versions,) so we must
include them with our packages.

To do that, you need to copy DLL files (and their manifests) mentioned
in the `winXX_build\mixxx.exe.manifest` file into the applicable
directory manually before making the installer package.

The needed files are likely:

  - `msvcp??.dll`
  - `msvcr??.dll`
  - `*Microsoft.VC??.CRT*.manifest`

Where *??* is the version number of the Visual Studio version used to
build Mixxx, one of its dependencies, or both. 2005 (v8.0) is `80`, 2008
(v9.0) is `90`.

These files can usually be found in the
`\VC\redist\xxx\Microsoft.VC??.CRT\` directory (where xxx is the machine
type: x86, x64/AMD64, or IA64) under your installation of Visual C++. If
you've installed the redistributable package (see below) on your build
system, they can also be found in %SYSTEMROOT%\\WinSxS. You'll want to
make sure you grab the exact version(s) specified in the
`mixxx.exe.manifest`, since that directory holds many versions.

If you can't find the DLLs in those places, you'll need to either
install the `vcredist[_x64]` package or extract it using
[MSIX](http://blogs.msdn.com/heaths/archive/2006/04/07/571138.aspx) and
grab the files from the `Microsoft_VCxx_CRT_xxx.msm` (CAB) file, which
can be extracted from the MSI file packed inside the `vcredist.exe`
file. (Use [7-Zip](http://www.7-zip.org/) to open the EXE as an
archive.) There's a different one for each architecture and compiler
combination, as shown below:

| Visual Studio 2005                                                                                                                 | [x86](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=200b2fd9-ae1a-4a14-984d-389c36f85647) | [x64/amd64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=eb4ebe2d-33c0-4a47-9dd4-b9a6d7bd44da) | [IA64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=747aad7c-5d6b-4432-8186-85df93dd51a9) |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [Visual Studio 2008](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=f3fbb04e-92c2-4701-b4ba-92e26e408569) | [x86](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=a5c84275-3b97-4ab7-a40d-3802b2af5fc2) | [x64/amd64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=ba9257ca-337f-4b40-8c14-157cfdffee4e) | [IA64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=dcc211e6-ab82-41d6-8dec-c79937393fe8) |

In any case, once you've located the needed DLL files, if you're doing a
32-bit build, copy the x86 DLL files and their manifest(s) (usually
found in a nearby "Manifests" folder) into mixxx-winlib. If a 64-bit
build, copy the x64/AMD64 DLL files and their manifest(s) into
mixxx-win64lib. Rename the manifest files so they just say the name of
the assembly, e.g.
`amd64_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_9d1c6ce0.manifest`
becomes just `Microsoft.VC80.CRT.manifest`

## Make the package

Just run `scons makerelease msvcdebug=0` and you should be good to go.
(If packaging for x64, Mixxx will be rebuilt to avoid
architecture-specific instructions.)

## Improvements

If someone feels like making this automatic, they will need to have the
NSI script and/or SConscript:

1.  Check the Mixxx.exe.manifest file and note which versions of which
    DLLs are needed
2.  Try to find the needed files in the \\VC\\redist\\ tree for the
    machine type
3.  Failing that, include the applicable .msm file from the
    redistributable packages and install it on the end-users machine.

Now, doesn't this make you long for a MinGW build? :)
