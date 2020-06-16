====== Macro Format ======

This is the format specification for Mixxx Macros, a feature that allows the recording and reproduction of jumps and particular control changes.

See [[Mixxx Macros]] for more infos as long as this is a WIP project.

===== Needed parts =====

  * send info on cue jumps (but not on scrubbing)
  * database table to store Macros
  * recording buttons (deck-independent)
  * macro list for each deck with name, loop option, enable option

===== Controls =====

==== [MacroRecording] ====
^ Key/Control ^ Range ^ What it does ^ On-screen feedback ^
| recording_toggle | binary | Arms Macro recording & stops it | Recording icon |
| recording_status | 0-2, RO | Indicates whether a Macros is being recorded: 0 = no recording, 1 = recording armed, 2 = recording active | Recording icon |
| deck | integer | The deck the Macro is being recorded to (0 if the recording_status != 2) | Toggle Button
| quantize | binary | Whether to quantize the recorded timestamps | Toggle Button |
| save | binary | Save the current Macro to its respective MacroRack | Button |

==== [ChannelN] ====
^ Key/Control      ^ Range       ^ What it does ^
| macros_show      | binary      | Whether to show the Macro Rack for this deck |
| macros_count     | integer, RO | Amount of Macros saved in this deck |
| macro_X_activate | binary      | If Macro X exists, seek to the first action and start it. If Macro X is unset, start recording for it. |
| macro_X_status   | 0-2, RO     | Whether this Macro is currently running |
| macro_X_enabled  | binary      | Whether this Macro will automatically be started when the track is loaded |
| macro_X_loop     | binary      | Whether this Macro should loop infinitely |
| macro_X_clear    | binary      | If Macro X is set, delete it and remove it from the Rack |

===== Format =====
