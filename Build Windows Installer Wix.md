# Making a Windows installer package

Mixxx uses the [Wix Toolset](http://wixtoolset.org/) for building
Windows MSI installers. This page contains information on making such
packages.

First, we assume you've built & run Mixxx successfully from the
instructions on the [Compiling on Windows](Compiling%20on%20Windows)
page.

## Preparation

You first need to download and install the [Wix
Toolset](http://wixtoolset.org/releases/) version 3.10

When built with MSVC, Mixxx requires that certain MSVC DLL files be
present in order to run. Many people have these already installed on
their systems, but many do not (or have different versions,) so we must
include them with our packages.

To do that, you need to download the vcredist installation package and
install it at the root of your build env directory.

There's a different one for each architecture and compiler combination,
as shown below:

| Visual Studio 2005                                                                                                                 | [x86](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=200b2fd9-ae1a-4a14-984d-389c36f85647) | [x64/amd64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=eb4ebe2d-33c0-4a47-9dd4-b9a6d7bd44da) | [IA64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=747aad7c-5d6b-4432-8186-85df93dd51a9) |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [Visual Studio 2008](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=f3fbb04e-92c2-4701-b4ba-92e26e408569) | [x86](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=a5c84275-3b97-4ab7-a40d-3802b2af5fc2) | [x64/amd64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=ba9257ca-337f-4b40-8c14-157cfdffee4e) | [IA64](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=dcc211e6-ab82-41d6-8dec-c79937393fe8) |
| Visual Studio 2010                                                                                                                 | [x86](http://www.microsoft.com/download/en/details.aspx?id=8328)                                                    | [x64/amd64](http://www.microsoft.com/download/en/details.aspx?id=13523)                                                   | [IA64](http://www.microsoft.com/download/en/details.aspx?id=21051)                                                   |
| Visual Studio 2013                                                                                                                 | [x86, amd64 and IA64](https://www.microsoft.com/en-gb/download/details.aspx?id=40784)                               |                                                                                                                           |                                                                                                                      |
| Visual Studio 2015                                                                                                                 | [x86 and amd64](https://www.microsoft.com/en-US/download/details.aspx?id=48145)                                     |                                                                                                                           |                                                                                                                      |

In any case, once you've located the vcredist installer, if you're doing
a 32-bit build, copy the x86 installer in the root of your build env
(not the root of mixxx sources, but the root of the BUILD ENV). If a
64-bit build, copy the x64/AMD64 installer.

The file should be named vcredist\_x86.exe or vcredist\_x64.exe.
