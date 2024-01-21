# Phase-locked-loop VSync Mode for scrolling waveforms

Mixxx 2.4.0 comes with an alternative mode to synchronise the scrolling waveform animation with the display refresh rate, using a so-called phase-locked-loop (PLL), which attempts to track the actual refresh rate and timing automatically. On particular hardware, the default periodic timer-based approach can result in jitter and frame drops and the PLL may gives better results.

This has been a last minute addition and is still considered experimental, so activation requires adding an entry `VSync 5` under the `[Waveform]` settings in the Mixxx configuration file `mixxx.cfg` which can be found in the [Mixxx settings directory](https://manual.mixxx.org/2.4/en/chapters/appendix/settings_directory).

```
[Waveform]
VSync 5
```
