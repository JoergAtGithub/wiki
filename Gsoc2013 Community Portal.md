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
```

# Current Progress

# Team

  - RJ Ryan

# Comments
