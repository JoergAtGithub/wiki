# Controller Mapping File Locations

## User Controller Mapping Folder

Put custom mappings that you made or downloaded from [the
forum](http://mixxx.org/forums/viewforum.php?f=7) in the following
folder. The MIDI Learning Wizard puts its mapping files here:

  - GNU/Linux: `/home/<username>/.mixxx/controllers`
  - OS X: `/Users/<username>/Library/Application
    Support/Mixxx/controllers`
  - Windows: `C:\Users\<username>\AppData\Mixxx\controllers`. On Windows
    XP, replace `Users` with `Documents and Settings`. The
    `%USERPROFILE%\AppData` folder is hidden, so if you have not
    already, you will need to set Windows explorer to [show hidden files
    and
    folders](https://support.quickbooks.intuit.com/support/Articles/INF12729).

Note that before Mixxx 1.12, mappings in this folder did not show up in
the drop down menu in the controller preferences for loading a preset.

## System Controller Mapping Folder

The default mapping files, which you can look at for examples or a
starting point for your own custom mapping, are located in the following
directory:

  - GNU/Linux: `/usr/share/mixxx/controllers` or
    `/usr/local/share/mixxx/controllers`
  - OS X: `/Applications/Mixxx.app/Contents/Resources/controllers/`
  - Windows: `C:\Program Files\Mixxx\controllers`

## Naming convention

Please name your mapping files according to these conventions before
making a pull request to have your mapping included in Mixxx.

XML MIDI mapping files use the naming convention `{manufacturer}
{device}.midi.xml`, for example `Stanton SCS3d.midi.xml`. XML HID
mapping files use the convention `{manufacturer} {device}.hid.xml`, for
example, `Hercules DJ Console RMX.hid.xml`. JavaScript files use the
naming convention `{manufacturer}-{device}-scripts.js`, for example
`Stanton-SCS3d-scripts.js`.

## Legacy Versions of Mixxx

For Mixxx 1.10 and earlier, replace 'controllers' with 'midi' in the
above paths.
