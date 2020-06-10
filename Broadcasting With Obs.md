# Broadcasting/Recording with OBS Studio

[OBS Studio](https://obsproject.com/wiki/) is free and open source
software for video recording and live streaming, available on Windows,
Linux and Mac.

## Download and install OBS Studio

[Official download page](https://obsproject.com/download)

**Installing on Windows**

The Windows release of OBS Studio supports Windows 8, 8.1 and 10. The
installation is done via the usuall windows installer.

**Installing on Linux**

The Linux release is available officially for Ubuntu 18.04 and newer.
FFmpeg is required.

    sudo apt install ffmpeg

After installing FFmpeg, install OBS Studio using:

    sudo add-apt-repository ppa:obsproject/obs-studio
    sudo apt install obs-studio

You can find more information about building and installing OBS Studio
on other Linux distros
[here](https://github.com/obsproject/obs-studio/wiki/Install-Instructions).

## Setting up the scene with OBS Studio

When you first start OBS Studio, a default scene will be created and
there will be also no sources setup as shown here:

[[/media/obs_sources.png|]]

One scene you could create is by inserting a picture or a screencast
from Mixxx.

  - If you want to insert a picture, just click on the "+" and select
    "Image". 
  - If you want to insert a screencast, just click on the "+" and select
    "Screen Capture"

Do not forget to also insert the audio input from Mixxx by clicking on
the "+" and selecting audio input.

A scene could look like this:

[[/media/obs_mixxx.png|]]
