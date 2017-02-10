For each release, these are the versions of each dependency that we
support.

To update one, do the following:

1.  Clone the repository in question
2.  Unzip the updated dependency's source
3.  Commit the clean dependency before changing anything, deleting the
    old version's folder
4.  Update the build script for that dependency
5.  Make changes as required until it builds successfully on all [CPU
    architectures we support](minimum_requirements)
6.  Commit the changes to your repository
7.  Create a pull request against the parent repository
8.  Await the results of the continuous integration test builds
9.  If they pass, await code review from other Mixxx developers. (If
    not, examine why and fix.)
10. Reviewer suggests changes or merges
11. Await build server building and publishing a new copy of the
    environment
12. Create a PR against
    [mixxxdj/mixxx](https://github.com/mixxxdj/mixxx/tree/master/build)
    to update the "golden" version of the dependencies used for release
    builds.
13. Update the dependency version listed here for the next version of
    Mixxx.

# Mixxx 2.1

Repository:
[Windows](https://github.com/mixxxdj/buildserver/tree/2.1.x-windows)
[macOS](https://github.com/mixxxdj/buildserver/tree/2.1.x-unix)

| Library       | Windows    | Mac OS X    |
| ------------- | ---------- | ----------- |
| Qt            | 4.8.7      | 4.8.7       |
| autoconf      | N/A        | 2.69        |
| automake      | N/A        | 1.15        |
| chromaprint   | 1.3.1      | 1.3.1       |
| cmake         | N/A        | 3.5.2       |
| fftw          | 3.3.4      | N/A         |
| hss1394       | r8         | r8          |
| libid3tag     | 0.15.1b    | N/A         |
| libmad        | 0.15.1b    | N/A         |
| libogg        | 1.3.2      | 1.3.2       |
| libshout      | 2.4.1      | 2.4.1       |
| libsndfile    | 1.0.26     | 1.0.26      |
| libsoundtouch | 1.9.2      | 1.9.2       |
| libtool       | N/A        | 2.4         |
| libusb        | N/A        | 1.0.20      |
| libFLAC       | 1.3.1      | 1.3.1       |
| openssl       | 1.0.2h     | 1.0.2h      |
| opus          | 1.1.2      | 1.1.2       |
| opusfile      | 0.7        | 0.7         |
| pkg-config    | N/A        | 0.29.1      |
| portaudio     | 2014-01-30 | 2016-10-30  |
| portmidi      | 228        | 217         |
| protobuf      | 2.6.1      | 2.6.1       |
| pthreads      | 2.9.1      | N/A         |
| rubberband    | 1.8.1      | 1.8.1       |
| scons         | 2.5.1      | 2.5.0       |
| sqlite        | 3130000    | 3130000     |
| taglib        | 1.10       | 1.11        |
| vorbis        | 1.3.5      | 1.3.5       |
| zlib          | 1.2.8      | Qt internal |
| ASIO SDK      | 2.3        | N/A         |

# Mixxx 2.0

Repository:
[Windows](https://github.com/mixxxdj/buildserver/tree/2.0.x-windows)
[macOS](https://github.com/mixxxdj/buildserver/tree/2.0.x-unix)

| Library       | Windows    | Mac OS X    |
| ------------- | ---------- | ----------- |
| Qt            | 4.8.6      | 4.8.6       |
| chromaprint   | 1.1        | 1.1         |
| cmake         | N/A        | 2.8.12.2    |
| fftw          | 3.3.4      | N/A         |
| hss1394       | r8         | r8          |
| libid3tag     | 0.15.1b    | N/A         |
| libmad        | 0.15.1b    | N/A         |
| libogg        | 1.3.2      | 1.3.1       |
| libshout      | 2.4.0      | 2.4.0       |
| libsndfile    | 1.0.25     | 1.0.25      |
| libsoundtouch | 1.8.0      | 1.8.0       |
| libvorbis     | 1.3.4      | 1.3.3       |
| libFLAC       | 1.3.0      | 1.3.0       |
| opus          | 1.1        | 1.1         |
| opusfile      | 0.6        | 0.6         |
| portaudio     | 2014-01-30 | 2014-01-30  |
| portmidi      | 228        | 217         |
| protobuf      | 2.5.0      | 2.5.0       |
| pthreads      | 2.9.0      | N/A         |
| rubberband    | 1.8.1      | 1.8.1       |
| sqlite        | 3080600    | 3080600     |
| taglib        | 1.10       | 1.10        |
| zlib          | 1.2.8      | Qt internal |
| ASIO SDK      | 2.3        | N/A         |

# Mixxx 1.11.x

| Library       | Windows    | Mac OS X   |
| ------------- | ---------- | ---------- |
| Qt            | 4.8.3      | 4.8.3      |
| libid3tag     | 0.15.1b    | N/A        |
| libmad        | 0.15.1b    | N/A        |
| libogg        |            | 1.3.0      |
| libshout      | 2.3.1      | 2.3.1      |
| libvorbis     | 1.3.3      | 1.3.3      |
| libsndfile    |            | 1.0.25     |
| libsoundtouch | N/A        | N/A        |
| libFLAC       |            | 1.2.1      |
| taglib        | 1.7.2      | 1.7.2      |
| libhss1394    | r6         | r6         |
| portaudio     | 2011-11-21 | 2011-11-21 |
| portmidi      | 217        | 217        |
| protobuf      | 2.4.1      | 2.4.1      |
| ASIO SDK      | 2.2        | N/A        |

# Mixxx 1.10.x

  - Qt 4.7.4
  - libid3tag 0.15.1b (not on OS X)
  - libmad 0.15.1b (not on OS X)
  - libogg 1.3.0 
  - libshout 2.2.2
  - libvorbis 1.3.2
  - libsndfile 1.0.25
  - libsoundtouch 1.5.0
  - libflac 1.2.1
  - taglib 1.7
  - libhss1394 (r6)
  - portaudio (2011/3/26 stable snapshot)
  - portmidi (r217)
  - Windows Only
  - ASIO SDK 2.2
