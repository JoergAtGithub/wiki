# Summary

**Status:** This specification is **in drafting**. Please feel free to
edit this page and add your comments. Mixxx currently supports a
wide-range of hardware MIDI controllers that DJs can use to perform
with. Each supported MIDI controller has a “mapping” file that is
bundled with Mixxx, but this mapping must be manually selected by the
user before their controller works.

The aim of this project is to increase the usability for new users by
automatically selecting the correct MIDI mapping and to provide an
intelligent workflow for when an unsupported MIDI device is connected.
And when a mapping for a MIDI device is not present, the user should not
be left out in the cold. She should have the option of connecting to
mixxx.org to see if there are any official or user-contributed mappings
available for download.

# Design

## Optimize preset loading and mapping

  - Use Case

When a controller is plugged in and the user needs to do some
configurations automatically or manually.Current version Mixxx provide a
semiautomatic way, i.e. if there are mapping files in local library,
Mixxx will load it during the initialization, if not, Mixxx will do
nothing and users have to select a right preset mapping file from a
drop-down list or even build mapping files by themselves.This is a
little hard to some initial users, so a new small feature will be a
user-friendly design if Mixxx can automitically search local library
backend and list the match results for user.

  - Core functions 

<!-- end list -->

  - Once a local mapping file isn’t searched during the initialization,
    Mixxx will give a notice message box to user, such as “Sorry,Mixxx
    cann’t select a perfect mapping for you from local library, you can
    go to Preferences-\>Controller widget to get a right one by yourself
    through our ‘Mapping Preset Manager’”.
  - If Mixxx load a preset for the devices at the beginning, the result
    will be showed on ‘dlgprefcontrollerdlg.ui’ just like the current
    version. A few changes to ‘dlgprefcontrollerdlg.ui’, see Fig.1.

<!-- end list -->

``` 
      - add a device picture. This is very easy to implement, but will help some users a lot. Through this intuitive image, User will easily know whether a right map has be done comparing with their devices at their first sight of the ‘dlgprefcontrollerdlg.ui’. Of course, if no file can be loaded, there will display nothing.
      - change the drop-down list to a button with the name “Mapping Preset Manager”. When the button is pushed, another dialog like Fig.2 will be showed. 
```

## Get controller mappings from web

# Work Breakdown

  - Database
  - database scheme design 

<!-- end list -->

``` 
    * Client
    * Server
* write models with Django for server database building
* update /res/schema.xml for client database building
* write interface of client database operation
* Automaticly load preset file
* Modify controller dialog user interface(dlgprefcontrollerdlg.ui)
    * controller covert preview
    * Popup  Mapping Preset Manager push button
* Adjust the workflow for mixxx initialization
* Enhance preset search algorithm
* Mapping Preset Manager
* Mapping Preset Manager Dialog user interface(dlgmapingpresetmanagerdlg.ui)
    * search bar 
    * Tap switch between Local and Cloud 
    * Search results panel
    * Notification board 
    * apply button
    * Submenu for preset download, details display etc.
* Intelligent recommendation algorithm for mapping preset files
* presets download
* users rate and comment on preset files
* Restful API Engine
* build a api server with django and tastypie
* design protobuf for api response and request formats
* api/search
* api/upload
* api/details
* api/checkversion
* api/rate
* api/download
* Deploy
```

# Current Progress

# Team

  - RJ Ryan

# Comments
