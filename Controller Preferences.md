# Controller Preferences

Author: Owen Williams

[Launchpad
Blueprint](https://blueprints.launchpad.net/mixxx/+spec/controller-options)
[Proof of Concept](https://github.com/ywwg/mixxx/tree/controller-prefs)

## Background

DJs use controllers in different ways, and it would be nice for Mixxx to
support those sorts of choices. Right now users have to hand-edit
javascript to change controller preferences, and that’s not reasonable
for many DJs for whom editing a text file is a big ask. Also, we want to
add support for MIDI clock in and out and the user will need to be able
to enable/disable this feature on an individual controller basis.

## Preference Persistence Design

Preferences will be stored in the mixxx.cfg file using the
configkey/value form `[Controller_[My_Controller_1]]`,`PreferenceName`
-\> value. `My_Controller_1` is the same as the Controller object’s
`m_pController->getName()` (need to check if that’s unique for multiples
of the same model of controller). That way there’s a simple mapping from
specific controller to controller preferences.

## Access to Preferences in Controller Javascript

The preferences need to be available to a controller’s javascript in
order to be useful. Preference settings will be set up by calling a
special function in the controller javascript, similar to how init() and
shutdown() work now. `ControllerEngine::initializeScripts()` currently
calls init, and it will be relatively easy to add another call to a
function like `updatePreferences()` that passes the preferences in.
Similarly we can add a connection to `[Preferences]`, `updated` so any
time the prefs with the correct prefix are updated, we call the update
function in the javascript.

The keys and values will be passed as a javascript Object:

``` cpp-qt
QScriptValue preferenceObject = m_pEngine->newObject();
const QMap<QString, QString> pref_map = getPrefsForController();
for (const auto& key : pref_map.keys()) {
        preferenceObject.setProperty(key, pref_map[key]);
}
QScriptValueList prefs;
prefs << preferenceObject;
callFunctionOnObjects(m_scriptFunctionPrefixes, "updatePreferences",
                      prefs);
```

So `initializeScripts()` takes the list of scripts, collects all the
preferences from the config file, assembles a javascript object and
passes it to updatePreferences. Each call to updatePreferences passes
all preferences, not just the prefs that changed. It’s up to controller
writers to handle the incoming preferences updates and decide if the
values have changed.

## Saving Preferences from Javascript

There will be a simple controllerengine function that takes the same js
Object map and writes it to the config file. (This is if the user pushes
a button on a controller that should be saved across sessions) Giving
ControllerEngine access to UserSettings Right now ControllerEngine is
pretty far away from the UserSettings pointer. I think I can get it
there this way:

  - ControllerManager does have m\_pConfig
  - Add an argument to the constructor of the ControllerEnumerators
  - Add an argument to the constructor of the Controller object.

When the enumerators construct controllers, they can pass in the
pointer.

## Iterating Through ConfigKeys

Currently the ConfigObject doesn’t have a way to iterate through all of
its keys. Because the controller prefs will be of the form
`[Controller_[My_Controller_1]]`,`PreferenceName` where preferencename
isn’t known ahead of time, I’ll need to add an accessor that returns a
list of keys. Probably `QList<ConfigKey>
ConfigObject::getAllConfigKeys()` or similar. That can just return
m\_values.keys(). Then the controllerengine can iterate through all the
configkeys and look for ones where the group has the correct controller
name.

## Preferences Dialog UI

The preferences dialog will need to surface the controller preferences.
This will probably be done on the first page of the preferences for a
controller so that it’s easy for users to find. I think the dialog can
be constructed programmatically -- search through config file and build
widgets for each found item.

## First Run

We’ll need to populate default preferences somewhere. Maybe from the js?
Or in the XML? Not sure about this yet.

## One More Thing…

Oooo, maybe it would be cool to allow the controller to register simple
button actions, like “test” or “reset lights.” That would be good for
debugging, but also a situation like having two of the same controller
connected and you want to know which one is which. Push the “blink me”
button and then you know which controller is which so which one to set
to deck 1 or deck 2.
