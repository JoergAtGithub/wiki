Before publishing a new version of Mixxx, the final release builds
should be manually tested on Windows, macOS, and Linux. The purpose of
these tests is to confirm that nothing catastrophic broke at the last
minute, not to find every little bug. When you have completed these
tests, please communicate your results in the topic for the release in
the [\#development stream on
Zulip](https://mixxx.zulipchat.com/#narrow/stream/109171-development).

  - Load tracks into 2 decks and play at the same time. Confirm that you
    can hear audio output.
  - Go to Preferences -\> Waveform and verify that the RGB, RGB (GL),
    and RGB (GLSL) waveform renderers all work.
  - Move EQ knobs and volume faders with your mouse (and controller if
    you have one).
  - Load an effect, assign the effect unit to a playing deck, enable the
    effect, turn up the effect unit mix knob and confirm that you can
    hear the effect.
  - If there is a broadcasting server you can test with, try connecting
    to it and listening to the stream.
  - For major releases (2.x, but not 2.2.y), repeat the above tests with
    a new settings directory. Make a new directory and run `mixxx
    --settingsPath test-directory-name` to tell Mixxx to use a different
    path for the settings directory.
