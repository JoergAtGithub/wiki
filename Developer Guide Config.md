# Introduction

The `ConfigObject` system is how Mixxx stores user preferences. The
`ConfigObject` is just a key-value store where the keys are `ConfigKey`
and the values are `QString`s.

A `ConfigKey` is a class that has two members, a `group` and an `item`.
The `group` describes the general category of the preference entry and
the `item` describes the actual preference. By convention, the `group`
is wrapped in square brackets, for example `[Library]`. Historically
this is because the group is used as the section when storing the
preferences on disk and since it is stored in the same format as a
[Windows INI file](http://en.wikipedia.org/wiki/INI_file), the sections
are wrapped in square brackets.

# Thread Safety

As of 07/2012 `ConfigObject` is not thread safe but it is often used
across threads in an unsafe manner. We haven't had any crashes reported
in the wild that we believe to be caused by this but we should fix this.

# Speed

Both the `getValueString` and `set` methods of `ConfigObject` are
\*linear time\* algorithms in the number of preferences stored in the
`ConfigObject`. Take care to not call these methods repeatedly since you
will waste time continuously iterating the list of all preferences. In
the future this should be converted to use a `QHash` so that set and get
are constant time operations.

# On-disk Storage

At startup, Mixxx loads the preference keys and values from the users
`~/mixxx.cfg` file. The `mixxx.cfg` file is formatted like a [Windows
INI file](http://en.wikipedia.org/wiki/INI_file).

As an example:

    [Recording]
    RecordingLocation=/home/rryan/Music/Recordings
    
    [Library]
    ShowITunes=0
    ShowRhythmBox=1

When this config file is loaded, the resulting `ConfigObject` will have
three entries

  - `ConfigKey("[Recording]","RecordingLocation")` will have the value
    "/home/rryan/Music/Recordings"
  - `ConfigKey("[Library]","ShowITunes")` will have the value "0"
  - `ConfigKey("[Library]","ShowRhythmBox")` will have the value "1"

# Getting and Setting Preference Options

Normally, the configuration object is passed around every section of
Mixxx as a variable defined like `ConfigObject<ConfigValue>* pConfig`.

To get a preference setting that is stored in the `ConfigObject`, do
something like the following:

    // ConfigObject is passed in to our constructor
    AnalyserBeats::AnalyserBeats(ConfigObject<ConfigValue>* pConfig) {
        // Get the [BeatDetection], MinBpm setting using a default of "80" if it isn't in the user's mixxx.cfg
        int min_bpm = pConfig->getValueString(ConfigKey("[BeatDetection]", "MinBpm"), "80").toInt();
        // Get the [BeatDetection], MaxBpm setting using a default of "120" if it isn't in the user's mixxx.cfg
        int max_bpm = pConfig->getValueString(ConfigKey("[BeatDetection]", "MaxBpm"), "120").toInt();
        // Get the [BeatDetection], Enabled setting using a default of "1" if it isn't in the user's mixxx.cfg
        bool bpm_detection_enabled = static_cast<bool>(pConfig->getValueString(ConfigKey("[BeatDetection]", "Enabled"), "1").toInt());
        // do logic based on user's preference settings
    }

Note that the values that a `ConfigObject` stores are all strings. You
are in charge of safely converting the value from string to integer or
whatever type you would like. It is good practice to provide a default
value for all the values you look up.

Similarly, to set preference settings, simply call `set` with a
`ConfigKey` and `QString` value.

    // Store the user's preference that we should show the iTunes features to them. Assumes m_bShowItunes is a bool that tracks the current setting in Mixxx. 
    m_pConfig->set(ConfigKey("[Library]", "ShowITunes"), m_bShowItunes ? "1" : "0");

It is good practice to set the user's preferences the moment in the
`ConfigObject` that they are changed instead of on shutdown or at
another time.

# Other uses of ConfigObject

Technically `ConfigObject` is a templated class that allows the storing
of values in a [Windows INI file](http://en.wikipedia.org/wiki/INI_file)
format. Mixxx's keyboard preferences are also stored using a
`ConfigObject` and the template value is just `ConfigValueKbd` instead
of `ConfigValue`.
