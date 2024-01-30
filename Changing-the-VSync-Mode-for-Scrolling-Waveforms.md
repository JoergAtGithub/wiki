When running Mixxx 2.4.0 for the first time, a line `VSync 0` will be added to the `[Waveform]` settings in the Mixxx configuration file, `mixxx.cfg`, which can be found in the [Mixxx settings directory](https://manual.mixxx.org/2.4/en/chapters/appendix/settings_directory). This setting controls how the scrolling waveforms, spinnies and VU-meters are constantly redrawn.

```
[Waveform]
...
VSync 0
...
```

Possible values are:

- `VSync 0` for `DEFAULT`: Use the platform-dependent default. For 2.4.0, `PLL` on macOS and `TIMER` on Linux and Windows.
- `VSync 4` for `FREE`: Redraw as fast as possible, sleeping a minimal (1 millisecond) interval between draws. Used for benchmarking.
- `VSync 5` for `PLL`: Phase-locked-loop to track the actual refresh rate and timing of the display automatically. (New since 2.4.0)
- `VSync 6` for `TIMER`: Synchronise the redraws used a fixed timer interval based on the frame rate in the Waveform setting. (Default until 2.4.0)

## Notes on PLL

The phase-locked-loop (PLL) method has been a last-minute addition. This mechanism attempts to track the actual refresh rate and timing of the display automatically. On particular hardware, the default periodic timer-based approach can result in jitter and frame drops and the PLL may gives better results. The PLL has been made the default on macOS. If you experience issues, you can revert to the `TIMER` based approach. Likewise, you are encouraged to try out PLL on Windows and Linux.

When using TIMER, the frame rate setting in the Waveform section in the Mixxx settings dialog is directly linked to the timer interval. When using PLL, it is rounded to integer divisions of the PLL-detected frame rate (e.g. at 60 fps: 30, 20, 15, 10). Ideally there should be no need to run below 60 fps though. 

If you change your refresh settings in the macOS system Display settings, make sure to restart Mixxx.
