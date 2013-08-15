# The Mixxx Bug Tracker

Our bug tracker is hosted on
[Launchpad](http://bugs.launchpad.net/mixxx). It is an essential part of
how the Mixxx team keeps track of and gradually eliminates all of
Mixxx's defects.

## Bug Importance Guidelines

  - Wishlist
  - **A feature that Mixxx does not currently have.**
  - If the bug is a placeholder for a project, that project should have
    a Blueprint.
  - Example:

<!-- end list -->

``` 
    * Support a certain sub-format of the FLAC specification.
    * Add MIDI mapping for XXX controller.
    * Rewrite the Control system to not suck.
* Low
* **A minor feature is subtly broken. Not likely to impact 90% of Mixxx of users.**
* Example:
    * Keyboard shortcuts fail to work under certain circumstances.
    * A community supported MIDI mapping is broken.
    * A Mixxx Certified MIDI Mapping is subtly broken.
* Medium
* **A minor feature is seriously broken. A major feature is subtly broken.**
* Example:
    * A Mixxx Certified MIDI Mapping is broken.
    * In a corner case, looping can accidentally become unset.
* High
* **A core feature is seriously broken but does not immediately and drastically screw a live performance.**
* Example: 
    * Looping does not work. 
    * The Library does not list tracks starting with O.
    * AutoDJ does not transition to the next song. 
* Critical
* **Any bug that will screw someone who is using Mixxx live.**
* Example: 
    * segfaults
    * assertion failures 
    * skips in the master output
    * bugs that cause a player to go crazy and emit screeching noises
```
