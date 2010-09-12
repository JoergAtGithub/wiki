
====== Library Scanner QA Checklist ======

This page is a checklist for ensuring that the Library and Library Scanner are working as intended.
===== Reference Test Grid =====

| Behaviour to Test ^ Expected behaviour ^ Windows ^ Mac OS X ^ Linux
^ Fresh library scan [1] | completes successfully | ? | ? | ? |
^ Upgrade library from 1.7.0 [1] |  preserves metadata | ? | ? | ? |
^ Move a file from one directory to another | BPM and comment metadata should be preserved, file not marked as missing | ? | ? | ? |
^ Move the file back | Should not see a duplicate entry for the file | ? | ? | ? |
^ Cancel a fresh library scan | some tracks should appear, no tracks should be marked as missing | ? | ? | ? |
^ After a fresh scan, cancel a rescan | no tracks should be marked as missing | ? | ? | ? |
^ 

[1] Delete your mixxxdb.sqlite first

===== Mixxx 1.8.0 Test Grid =====

  * Test With: 
  * Mixxx 1.8.0, BZR rXXXX
  * Qt X.Y.Z (whatever is shipped on OSX and Windows with Mixxx)''
