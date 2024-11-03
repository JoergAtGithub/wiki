# Compiling dependencies using vcpkg

Mixxx provides an archive with all the precompiled dependencies and build tools that Mixxx requires. If you prefer or need to compile them yourself, you can do so using the Mixxx vcpkg repository.

These instructions are for macOS arm64 release builds, but should be easily adapted to other configurations.

## Build tools

The build process requires several common build tools. You can install these using homebrew. Follow instruction on the [homebrew website](https://brew.sh) to install homebrew. Use it to install the following packages:

```
$ brew install automake autoconf-archive ccache nasm ninja pkg-config libtool
```

Note that homebrew will install everything in ```/opt/homebrew```

## Mixxx vcpkg repository

Clone the [Mixxx vcpkg repository](https://github.com/mixxxdj/vcpkg). This contains the ```vcpkg``` dependency manager and configurations for all of Mixxx dependencies.

```
$ git clone git@github.com:mixxxdj/vcpkg.git
$ cd vcpkg
```

Run the bootstrap script. This will setup the repository and build the ```vcpkg``` executable, which will be used to download, build and install all of Mixxx dependencies. The install location is inside the vcpkg directory.

```
$ ./bootstrap-vcpkg.sh
```

Once bootstrapped, run vcpkg with the following options:

```
$ ./vcpkg --x-install-root=installed --triplet=arm64-osx-release --host-triplet=arm64-osx-release install
```

When finished, you will find all compiled dependencies in the folder ```installed/arm64-osx-release```

## Configure Mixxx build

You can now configure the Mixxx build process:

Inside your mixxx root directory, as typically cloned from git with

```
$ git clone git@github.com:mixxx.git
$ cd mixxx
```

create an empty build directory. Inside that directory run ```cmake``` with the following options:

```
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_OSX_DEPLOYMENT_TARGET= -DCMAKE_GENERATOR=Ninja -DVCPKG_TARGET_TRIPLET=arm64-osx-release -DMIXXX_VCPKG_ROOT=<path to your vcpkg folder>
```

(Note: you will have to substitute the path to your vcpkg folder.)

You can now build Mixxx, using ```ninja``` directly, or indirectly with ```cmake```: 
```
$ cmake --build .
```
