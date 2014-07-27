Hello,

The `LV2EffectProcessor` class is now implemented. It dynamically
creates an `EngineEffectParameter*` for each effect parameter it
extracts from the `EffectManifest`. It has 4 float arrays which are I/O
buffers (input left, input right, output left, output right). Also it
features a `params` array which is used to communicate parameter changes
to the plugin instance. This class' constructor receives a `const
LilvPlugin*` which is passed as a parameter to `lilv_plugin_instantiate`
function. This is the first function which needs to be called. The next
step is using `lilv_instance_connect_port` to connect the plugin's ports
to chunks of memory. For example, audio ports need to be connected to
float arrays, while each control port communicates through a single
float value. To be able to differentiate between those two types of
ports I use two lists of indices: one which stores the audio port
indices and another one which stores the control port indices.
`lilv_instance_activate` is the next function we need to call. It resets
all state information in the plugin, except for previously assigned port
data locations. Inside `LV2EffectProcessor::process` we update the
parameter array with values extracted from each `EngineEffectParameter`.
Now all we have to do is split the input into channels (L and R), call
`lilv_instance_run` and combine the resulting samples into an
interleaved stereo output. The plugin instance is deactivated and freed
inside the destructor.

LV2 plugins can have enumeration ports as parameters which can be
represented as drop down lists. However, it is an open debate about how
this type of parameters should be introduced into Mixxx's Effects
Framework. For the moment, I added a new ValueHint to
EffectManifestParameter: VALUE\_ENUMERATION. For each enumeration port,
I extracted a list of pairs which contains the description and the value
for each enumeration entry. I used `lilv_port_get_scale_points` to
obtain the options, I iterated through them and used
`lilv_scale_point_get` function to get the value and
`lilv_scale_point_get_label` function to get the description of each
scale point (enumeration entry).

Daniel had some issues with the lilv library, so I added a Lilv class to
`features.py`. I hope this solves the problem with lilv library linking.

Also, I have added kill buttons to Butterworth8EQEffect and opened a
pull request\[1\]. I am currently waiting for feedback. It depends if we
want to go this way with button and enumeration parameters, or tackle
this problem differently.

As a side task, I added search functionality to developer's log. I
needed this feature while doing some debugging. I used Qt Creator to
insert a `QLineEdit` and a `QPushButton` to the GUI. Inside
*dlgdevelopertools.cpp* I connedted QLineEdit's `returnPressed()` and
QPushButton's `clicked()` signals to a newly added slot,
`slotLogSearch()`. Here\[2\] is the PR I opened for this feature. Tell
me what you think about it. In my opinion, this might be handy for some
developers.

Stay tuned for updates,  
Nicu Badescu  
\[1\] - <https://github.com/mixxxdj/mixxx/pull/297>  
\[2\] - <https://github.com/mixxxdj/mixxx/pull/300>  
[Back to the main page\!](extending_the_effects_engine)
