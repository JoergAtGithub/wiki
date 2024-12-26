Serato stores its crate information in a directory called
\_Serato\_/Subcrates in the root of the drive where the music is located
(this is true when the music is on a removable drive, unclear what
happens when it's on the primary drive of the computer). Each file in
this directory corresponds to one crate and will be named
CrateName.crate.

The format of these .crate files is a concatenated sequence of records.
Each record starts with a 4-byte ASCII tag, followed by a 4-byte
big-endian length (always at least one), followed by the bytes of the
record. The way the bytes are interpreted depends on the tag and follows
this table:

| Tag pattern | Data format                                                                 |
| ----------- | --------------------------------------------------------------------------- |
| o\*         | Nested sequence of records                                                  |
| t\*         | UTF-16 big-endian text                                                      |
| p\*         | UTF-16 big-endian text, value is a path (relative to the root of the drive) |
| u\*         | Unsigned 32-bit big-endian value                                            |
| s\*         | Signed 32-big big-endian value                                              |
| b\*         | Byte value                                                                  |
| vrsn        | UTF-16 big-endian text, value is crate format version                       |

Here are the meanings of specific fields:

| Tag name | Meaning                                 |
| -------- | --------------------------------------- |
| otrk     | Track                                   |
| ptrk     | Path to track file (nested inside otrk) |

Here's an example of the structure of the .crate file:

``` 
  [
    ('vrsn', '1.0/Serato ScratchLive Crate'),
    ('otrk', [
      ('ptrk', 'Music/Daft Punk - 2001 - Discovery/06 Night Vision.mp3')]),
    ('otrk', [
      ('ptrk', 'Music/Daft Punk - 2013 - Random Access Memories/05 Instant Crush.mp3')]),
  ]
```

Note that the name of the crate is \*not\* encoded in the crate itself;
it's only present in the filename. Also, some not-very-useful fields are
omitted in this example; for example there appear to be fields that give
the order that the title/artist/key/BPM columns should appear in the
browser.

[Here is some Python 3 code that can parse the .crate file
format.](https://gist.github.com/kerrickstaley/8eb04988c02fa7c62e75c4c34c04cf02)
