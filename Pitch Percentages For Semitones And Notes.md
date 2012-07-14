# Relative pitch percentage & semitone note table

(This is useful if you're making a controller act similar to the Vestax
Controller One.)

| Note name | Semitones       | Pitch percentage |
| --------- | --------------- | ---------------- |
| A         | \-12 = 1 octave | \-50%            |
| Bb        | \-11            | \-47.03%         |
| B         | \-10            | \-43.88%         |
| C         | \-9             | \-40.54%         |
| Db        | \-8             | \-37.00%         |
| D         | \-7             | \-33.26%         |
| Eb        | \-6             | \-29.29%         |
| E         | \-5             | \-25.08%         |
| F         | \-4             | \-20.63%         |
| Gb        | \-3             | \-15.91%         |
| G         | \-2             | \-10.91%         |
| Ab        | \-1             | \-5.61%          |
| A - 440Hz | 0               | 0.00%            |
| A\#       | 1               | \+5.95%          |
| B         | 2               | \+12.25%         |
| C         | 3               | \+18.92%         |
| C\#       | 4               | \+25.99%         |
| D         | 5               | \+33.48%         |
| D\#       | 6               | \+41.42%         |
| E         | 7               | \+49.83%         |
| F         | 8               | \+58.74%         |
| F\#       | 9               | \+68.18%         |
| G         | 10              | \+78.18%         |
| G\#       | 11              | \+88.77%         |
| A         | 12 = 1 octave   | \+100%           |

This was calculated using the following information. Since an octave
doubles (or halves) the frequency and there are 12 equal steps
(semitones), we can find that the frequency is multiplied (or divided)
by a certain factor:

mfact = 12th root of 2 = 2^(1/12) = 1.0594631

So you get

|     |                                |
| --- | ------------------------------ |
| A   | 440Hz                          |
| A\# | 440\*1.059 = 466.2 Hz          |
| B   | 440\*(1.059\*1.059) = 493.9 Hz |

etc..
