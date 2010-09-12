# Library Scanner QA Checklist

This page is a checklist for ensuring that the Library and Library
Scanner are working as intended.

## Reference Test Grid

|                                                               |                                                                          |         |          |       |
| ------------------------------------------------------------- | ------------------------------------------------------------------------ | ------- | -------- | ----- |
| Behaviour to Test                                             | Expected behaviour                                                       | Windows | Mac OS X | Linux |
| Fresh library scan \[1\]                                      | completes successfully                                                   | ?       | ?        | ?     |
| Immediately rescan library without making changes             | completes quicker than fresh scan                                        | ?       | ?        | ?     |
| Upgrade library from 1.7.0 \[1\]                              | preserves metadata, all tracks imported                                  | ?       | ?        | ?     |
| Move a file from one directory to another                     | BPM and comment metadata should be preserved, file not marked as missing | ?       | ?        | ?     |
| Move the file back                                            | Should not see a duplicate entry for the file                            | ?       | ?        | ?     |
| Add a song to a library subdirectory, rescan                  | Song should appear in Mixxx library                                      | ?       | ?        | ?     |
| Cancel a fresh library scan                                   | some tracks should appear, no tracks should be marked as missing         | ?       | ?        | ?     |
| After a fresh scan, cancel a rescan                           | no tracks should be marked as missing                                    | ?       | ?        | ?     |
| Delete a song from disk, rescan                               | Song should be marked as missing                                         | ?       | ?        | ?     |
| Remove song from Mixxx library (right-click-\>Remove), rescan | Song should not appear after rescan                                      | ?       | ?        | ?     |
| Drag-and-drop removed song onto Mixxx library                 | Song should be re-added to Mixxx                                         | ?       | ?        | ?     |

\[1\] Delete your mixxxdb.sqlite first

## Mixxx 1.8.0 Test Grid

  - Test With: 
  - Mixxx 1.8.0, BZR rXXXX
  - Qt X.Y.Z (whatever is shipped on OSX and Windows with Mixxx)''
