Hello again,

As you know from the last report, I made the Bessel Equalizers
configurable from preferences. Daniel noticed that the "Enable EQs"
check box did not cause immediate change. I took a look at the code
responsible for managing that box and found out that was the desired
behaviour. Only after clicking "Apply" the equalizers were enabled or
disabled. I talked with my mentor and concluded that instant change
would be nice. All I had to do was call `DlgPrefEQ::slotApply` method
inside `DlgPrefEQ::slotEnaEQChanged`. Also, on the EQ part I changed the
order of the Bandpass Bessel filter to 4.

I started working at LV2 native support. The first step was getting lilv
library to work inside Mixxx. I installed it on my system using the
package manager. In order to work, the library needed to be linked when
compiling the source files, using `-llilv-0` argument. I don't have much
experience with SCons so I tried a naive way of linking lilv: find where
SCons is storing its build parameters and append -llilv-0 to them. This
did not work because it was passed at the beginning of the command. I
learned that g++ is passing only one time over its arguments and it
links the library if the name of a source file is encountered before the
library argument. For example:

The `-llilv-0` argument inside this command is useless:  
`g++ -llilv-0 source_file.cpp`

This works as it should:  
`g++ source_file.cpp -llilv-0`

After doing a little research about SCons, I found out that linking
libraries is simply a matter of adding the name of the library to a
list: `build.env.Append(LIBS='lilv-0')`. Before merging the LV2
integration we must decide if we want to keep lilv as an external
dependency as it currently is, or bundle it together with Mixxx (see how
fidlib is handled).

I created a new class `LV2Manifest` which job is to receive a
`LilvPlugin*` and create an `EffectManifest` from it. This is useful
because Mixxx is using this EffectManifest to create and update
parameter knobs. Inside this class I iterated through plugin's control
ports and created corresponding EffectParameters. Here I set the control
hint to `EffectManifestParameter::CONTROL_KNOB_LINEAR` and check if the
value hint should be set to `VALUE_FLOAT` or `VALUE_INTEGRAL` using the
`lilv_port_has_property` function. The plugin's id, name and author
fields are initialized too. This class features a `m_isValid` boolean
field which is set to true if we support the plugin. Currently there are
two cases when we set this field to false:

  - when the plugin has required features (we can check this with
    `lilv_plugin_get_required_features` function)
  - when the plugin doesn't have two audio inputs and two audio outputs,
    since Mixxx is handling stereo samples

I created a basic LV2 backend and a first version of an effect
processor. I will work on improving them during the next week.

I did some tests with kn0ck0ut\[1\] plugin. I used Audacity, jalv and
lv2proc as LV2 hosts. The results are the same: the plugin is only
playing silence regardless of how I set its parameters. So I joined the
\#lv2 Freenode channel and asked for help, which came right away.
Here\[2\] you can read the conversation. This kind of responsiveness is
what I love about open source communities :D . When we conceived this
GSoC project, our goal was performing vocal removal on the fly, using
the before mentioned plugin. Luckily I found another\[3\] LV2 plugin
pack which features a Karaoke effect. I'll do some tests with it and
keep you posted\!

See you soon,  
Nicu Badescu

\[1\] - <https://github.com/jeremysalwen/kn0ck0ut-LV2>  
\[2\] - <https://gist.github.com/badescunicu/724b035396ed7bdd9ac8>  
\[3\] - <https://github.com/swh/lv2>  
[Back to the main page\!](extending_the_effects_engine)
