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

Once a local mapping file isn’t searched during the initialization,
Mixxx will give a notice message box to user, such as “Sorry,Mixxx
cann’t select a perfect mapping for you from local library, you can go
to Preferences-\>Controller widget to get a right one by yourself
through our ‘Mapping Preset Manager’”.

If Mixxx load a preset for the devices at the beginning, the result will
be showed on ‘dlgprefcontrollerdlg.ui’ just like the current version. A
few changes to ‘dlgprefcontrollerdlg.ui’, see Fig.1.

``` 
      - add a device picture. This is very easy to implement, but will help some users a lot. Through this intuitive image, User will easily know whether a right map has be done comparing with their devices at their first sight of the ‘dlgprefcontrollerdlg.ui’. Of course, if no file can be loaded, there will display nothing.
      - change the drop-down list to a button with the name “Mapping Preset Manager”. When the button is pushed, another dialog like Fig.2 will be showed. 
* Fig.1
```

[[/media/controllers.png|]]

  - Fig.2

[[/media/manager.png|]]

## Support getting controller mapping resources from web

  - Use Case

Mixxx can not do an automical map or an perfect map from local library
at the beginning, so users need to choose one by themselves.Mapping
files needed by user may exist in local or website, we’d better provide
an API for user to query both local and cloud depository.Most users are
not very sure which one to choose, so we’d better make an intelligent
recommendation for users, especially for novice users, to reduce the
sense of fear of using mixxx at the beginning. At the same time, it is
also very convenience.A mapping file has been downloaded into local
library, but maybe it has some bugs or is not that perfect. And there is
a new update version on the mixxx forum or somewhere, so when users try
to apply a local preset in the case of network connected, we’d better to
advice users to update to a new version of preset.

  - Core functions

Here I think we can create a new feature called "Mapping Files Manager",
with the following functions:

``` 
  - A search bar, through which user can get some likely right mapping files coing form local and cloud.
  - A local tab and a cloud tab, which can list the searching results seperately
  - Intelligent recommendation system, which can do an intelligent sort for users searching results and show the results with the most possibility at the top.
  - friendly and cool devices UI display, called mapping cover, which can help users locate the mapping file item quickly. 
  - displaying the source(mixxx or mixxx forum or other websites), grade level, certification or not, and the authors.
```

# Work Breakdown

  - ~~Database~~
  - ~~database scheme design~~ 

<!-- end list -->

``` 
    * <del>Client</del>
    * <del>Server</del>
* <del>write models with Django for server database building</del>
* <del>update /res/schema.xml for client database building</del>
* <del>write interface of client database operation</del>
* <del>export preset relevant data into database</del>
    * <del>write a script able to push preset relevant data into server database</del>
    * <del>push preset relevant data into mixxx local database when mixxx is initialized</del>
* Automaticly load preset file
* <del>Modify controller dialog user interface(dlgprefcontrollerdlg.ui)</del>
    * <del>controller covert preview</del>
    * <del>Popup  Mapping Preset Manager push button</del>
    * <del>Upload menu</del>
* <del>Adjust the workflow for mixxx initialization</del>
* <del>Enhance preset search algorithm</del>
* <del>Upload</del>
* <del>upload.ui</del>
* <del>logic: upload to cloud server and save in local</del>
* <del>Mapping Preset Manager</del>
* <del>Mapping Preset Manager Dialog user interface(dlgmapingpresetmanagerdlg.ui)</del>
    * <del>search bar</del> 
    * <del>Tap switch between Local and Cloud</del> 
    * <del>Search results panel</del>
    * Notification board 
    * <del>apply button</del>
* <del>fuzzy query both from local and cloud</del>
* <del>display the query results in the way of paging</del>
* <del>presets download</del>
* users rate and comment on preset files
* Intelligent recommendation algorithm for mapping preset files
* <del>check for update local preset</del>
* <del>Restful API Engine</del>
* <del>build an api server with django and tastypie</del>
* <del>design API</del>
    * <del>details</del>
    * <del>search</del>
    * <del>download</del>
    * <del>checkversion</del>
    * <del>upload</del>
    * <del>rate</del>
    
* Deploy
* Test
```

# Current Progress

deploy

# Team

  - RJ Ryan

# Comments
