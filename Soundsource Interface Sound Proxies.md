Sound source proxies handle reading files in various formats and
providing decoded audio samples to the upper levels.  
The proxies are the soundsource\*.cpp files. As of 1.7.2 that consists
of the following: (and associated .h includes)  
soundsourcemp3.cpp  
soundsourcem4a.cpp  
soundsourceffmpeg.cpp (broken)  
soundsourceoggvorbis.cpp  
soundsourcesndfile.cpp  
The above files provide the classes referred to by  
soundsource.cpp  
soundsourceproxy.cpp  

For the discussion of samples, I will use the following convention in
this page :  
1- sample rate is in Hz (ex.: the common 44100 Hz)  
2- a time sample is one sample at the current rate, i.e. 1/44100 s.
"timesamp"  
3- an audio sample is one numerical value expressing the audio signal of
a single channel. In the case of mixxx, this is one signed 16-bit value.

Mixxx's upper levels work in stereo, so every timesample has two audio
samples associated with it.  
Usually mixxx will count in audiosamples for 2 channels.  
See the ::seek and ::read descriptions below for more details.

All soundsource\*\*.cpp proxies must provide the following functions to
the upper levels:

SoundSourceX::SoundSourceX(QString qFilename);  
The constructor opens the specified file, verifies that it is valid &
readable, and prepare the file & library to actually read audio data.  
It should also fill in track details such as  
\- SRATE (sample rate in Hz) - must be readable by the upper levels  
\- other internal variables that will serve during decoding (file
length, number of channels, etc.)  
The constructor normally returns nothing, but a "return;" instruction
may be used in case of an unreadable / invalid file.  
Note that the presence of tags is not necessary to make a file
readable.  
On exit, the file handles should stay open.

SSX::\~SoundSourceX();  
The destructor, which closes the file & associated handles, data
structures, etc. cleanly. No return value.

long SSX::seek(long filepos);  
filepos is given in audiosamples. For example, to seek 1 second into a
common 44.1kHz audio file (mono or stereo doesn't matter),  
mixxx will actually call seek() with 88200 as a parameter. It is up to
the proxy to deal with mono / stereo files.  
The function should return the actual position that was succesfully
seeked to.

unsigned SSX::read(unsigned long size, const SAMPLE\*);  
"size" here is also given in audio samples, i.e. timesamples \* 2.  
SAMPLE\* is the pointer to a big enough array of "size" audiosamples.  
For example, read(10, dest\_buffer) means that the caller wants to read
5 time samples (10 audio samples) from  
the source file, and the dest\_buffer array contains enough place to
store exactly 10 \* 2 bytes (16-bit signed values).

The function must produce stereo, 16bit signed data. Mono files can be
handled by duplicating the audio data to both channels.  
The filled SAMPLE\* array would look like this:  
L R L R L R ... for a stereo file, where L or R is 2 bytes  
L l L l L l ... for a mono file, where l is a copy of L.

As ::read gets called an awful lot, performance is paramount. No dynamic
memory tricks (new, malloc, etc.), no library calls for every sample
(reading in blocks is highly recommended), etc.  
The function will return the actual number of audiosamples read.

long unsigned SSX::length();  
the function should return the file length (-NOT- the binary size) in
audio samples. For a 1 minute, 44.1kHz stereo file this would be  
60 \* 44100 \* 2.

int SSX::ParseHeader( TrackInfoObject \* );  
This gets called when a file/track is drag-dropped to a player or the
library.  
Some work is being done to sanitize the functionality & behaviour.  
The function should open the specified track, make sure it is readable,
attempt to extract tags and set the appropriate objects.  
"return ERR;" should signal the upper level that the file is invalid or
unreadable.  
A file without tags should be readable, and not cause a "return ERR;".  
  
Tags are set this way:  
Track-\>setTitle(QString(titlestring));  
Here are some examples of supported items:  
\-\>setTitle  
\-\>setArtist  
\-\>setBPM  
\-\>setDuration (in seconds)  
\-\>setBitrate (kilobits/s)  
\-\>setSampleRate (Hz)  
\-\>setChannels (1 or 2)  
  
On exit, the ::parseheader must close all file handles.  
When the function is succesfully executed, HeaderParsed must be set to
true:  
Track-\>setHeaderParsed(true);  
(so the upper levels therefore only need to call ::ParseHeader once.)  
On exit : "return OK;"
