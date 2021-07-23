The Mixxx settings folder contains all user data and settings of your Mixxx installation.

## Location

**Linux**  
`~/.mixxx/`  
Note: make sure you have 'Show hidden files' enabled in your file manager
in order to show all dot-files and folders.

**Windows**  
Vista and up: `%LOCALAPPDATA%\Mixxx\`  
XP and below: `%USERPROFILE%\Local Settings\Application Data\Mixxx\`  
Type either of those into the location bar of a Computer or Folder window.

**macOS**  
Mixxx 2.3: `~/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx`  
Mixxx 2.2 and earlier: `~/Library/Application Support/Mixxx`  

## Content

`analysis` folder  
This contains all waveform analysis, i.e. the data used to compose a track's scrolling waveform and track overview.  
If not existent, this data will be recreated each time a track is loaded into a Mixxx deck. Thus it does not belong to the essential data to be backed up.  

`broadcast_profiles` folder  
All broadcast profiles you have configured.  

`controllers` folder  
All controller mappings you stored. This can be downloaded and self-built mappings, as well as built-in mappings that you modified in Preferences > Controllers > YourController manually or with the MIDI Wizard.  

`effects.xml` (TODO update for the new effects system)  
The current configuration of the 4 effect units, incl. the state of all controls.  

`mixxx.cfg`  
Everything configured by the Preferences, deck settings, skin settings, AutoDJ configuration, effect routing etc.  

`mixxx.log[.NN]`
session logs

`mixxxdb.sqlite`  
The Mixxx library database. All track locations, all track metadata, saved cues, loops, colors, playlists, crates, ...  

`samplers.xml`  
Stores tracks currently loaded to sample decks.  

`sandbox.cfg`  
??  

`soundconfig.xml`  
Sound device configuration from Preferences > Sound Hardware  