# [WIP] Mixxx Effect Development Example

This is a practical guide of how to develop a simple native effect for
mixxx effects framework. In order to demonstrate actual steps needed, a
simple utility effect is used as an example effect.

More analytical info on topic can be found in the [Effects section of
the Developer Guide](Developer%20Guide%20Effects).

## Utility Effect

This effect comprises of two control elements, one knob that sets the
level/gain of the input processing audio and one switch that mutes or
unmutes the audio output.

Code developed for this effect can be reviewed in this pull request:
[Custom effect example
\#1284](https://github.com/mixxxdj/mixxx/pull/1284).

The actual effect implementation is done in the files utilityeffect.cpp
and utilityeffect.h located at src/effects/native/ directory.

In header file, after importing all the needed files, a structure with
the effect group state is declared. This structure will hold all the
state variables that the effect will keep from one block processing to
another.

Next the actual effect class is declared, with all the required methods.
In order to be able the effect to work with the native effect
backend,the following methods should be implemented: getId, getManifest
and processChannel.

Implementation of these methods is done in utilityeffect.cpp

getManifest is responsible for connecting the control elements with the
effect process. The two control elements are declared as pointers to
EffectManifestParameter object, and their type and default/min/max
values are set. Some extra info such as a description for hover text and
name tags that will indicate the control elements by the skin are
declared here as well.

Constructor of the effectobject is where all effect initialization shall
take place.

Finally the process method is where all the action happens. process is
called every numSamples/2 \* sampleRate seconds, and it delivers stereo
interleaved samples at pInput buffer. Output buffer should be completed
in a similar interleaved way with the processed samples.

This Utility effect implements also a simple ramping function, by adding
a controllable ramp envelope when effect state is mutually changed from
muted to unmuted and from enabled to disabled.

In order for the native effect backend be aware of the new effect, it
should be included and registered in
src/effects/native/nativebackend.cpp and
src/test/nativeeffects\_test.cpp

Finally, add the new files to `CMakeLists.txt` so they are included in
the cmake build.