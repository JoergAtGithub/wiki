# Skin System Changelog

## Mixxx 2.3.0

``` 
 * If supported by the selected skin, display [[creating_skins#skin_preview_image|skin preview screenshots]] for a set of color variations to choose from in Preferences -> Interface -> Color Scheme [[https://github.com/mixxxdj/mixxx/pull/2008|pull#2008]]
 * Allow to set set variables within color schemes [[creating_skins#skin_preview_image|skin preview screenshots]] for a set of color variations to choose from in Preferences -> Interface -> Scheme [[https://github.com/mixxxdj/mixxx/pull/1988|pull#1988]]
```

## Mixxx 2.1.0

``` 
 * Display [[creating_skins#skin_preview_image|skin preview screenshots]] in Preferences -> Interface [[https://github.com/mixxxdj/mixxx/pull/1525|pull#1525]]
 * Added support for platform-dependent [[creating_skins#qss_style|skin styling]]. [[https://github.com/mixxxdj/mixxx/pull/1590|pull#1590]]
 * Added [[creating_skins#recording_duration|<RecordingDuration>]] widget that Displays the duration of the running recording.[[https://github.com/mixxxdj/mixxx/pull/1221|pull#1221]],  [[https://github.com/mixxxdj/mixxx/pull/1398|pull#1398]]
 * Added ''PlayedOverlayColor'' to [[creating_skins#waveform_overview|<Overview>]] that makes the overview-waveform darker for the played portion of the track. Support ARGB for ''PlayedOverlayColor'', ''AxesColor'', ''PlayPosColor'', and ''BgColor'' [[https://github.com/mixxxdj/mixxx/pull/1203|pull#1203]]
 * Added [[creating_skins#EffectSelector|<EffectSelector>]] widget that allows to select effects from alphabetically ordered lists of available effects.[[https://github.com/mixxxdj/mixxx/pull/1135|pull#1135]]
 * Added ''Orientation'' to [[creating_skins#waveform|<Visual>]] and [[creating_skins#waveform_overview|<Overview>]] which allows choosing between horizontal and vertical waveforms/overviews. [[https://github.com/mixxxdj/mixxx/pull/983|pull#983]]
 * Added support for collapsible [[creating_skins#splitter|<Splitter>]] children. [[https://github.com/mixxxdj/mixxx/pull/917|pull#917]]
 * Added [[creating_skins#battery|<Battery>]] widget to show the battery status. [[https://github.com/mixxxdj/mixxx/pull/401|pull#401]]
```

## Mixxx 2.0.0

``` 
 * Allow each child of a [[creating_skins#widgetstack|<WidgetStack>]] to specify which page is show on hide. See [[https://github.com/mixxxdj/mixxx/pull/576|pull#576]]
 * Add property to elide parts of the text fit to the Text item's (Widget inherited from WLabel) text. Available options are ''none'', ''left'', ''right'', and ''middle''. See [[https://github.com/mixxxdj/mixxx/pull/506|pull#506]]
 * <code=xml><TrackProperty>
 ...
 <Elide>right</Elide>
```

\</TrackProperty\>\</code\>

``` 
 * Add support for [[creating_skins#singleton_widgets|Singleton widgets]] that should only be instantiated once but may appear in multiple places in a skin definition. This is useful for complex widgets like the library, which are memory intensive. See [[https://github.com/mixxxdj/mixxx/pull/463|pull#463]]
 * Add scalemode support to most widget images, See [[https://github.com/mixxxdj/mixxx/pull/426|pull#426]]
     * FIXED = Draw the image in its native dimensions with no stretching or tiling.
     * STRETCH = Stretch the image
     * STRETCH_ASPECT = Stretch the image maintaining its aspect ratio.
     * Tile = Tile the image. Some examples below:
     * <code=xml><Slider scalemode="STRETCH">foo.svg</Slider>
```

\<Handle scalemode="STRETCH\_ASPECT"\>foo.svg\</Handle\> \<BackPath
scalemode="TILE"\>foo.png\</BackPath\>\</code\>

``` 
 * Show cover art in background of [[creating_skins#spinning_vinyl_image_spinny|<Spinny>]] vinyl widget. See [[https://github.com/mixxxdj/mixxx/pull/391|pull#391]]
 * Added support for variables in svg attributes. See [[https://github.com/mixxxdj/mixxx/pull/302|pull#302]].
 * Added ''<StarRating>'' widget that allows to rate a track currently loaded in a deck. See [[https://github.com/mixxxdj/mixxx/pull/380|pull#380]].
 * Added ''<SignalRGBLowColor>'', ''<SignalRGBMidColor>'', ''<SignalRGBHighColor>'' to [[creating_skins#waveforms|<Waveforms>]]. Allows separate color config for RGB waveforms, if selected in ''Preferences>Waveforms>Summery Type>RGB (GL)''. See [[https://github.com/mixxxdj/mixxx/pull/363|pull#363]]
 * Added [[creating_skins#sizeawarestack|<SizeAwareStack>]] widget that allows to allows resize to available screen space at runtime. See [[https://github.com/mixxxdj/mixxx/pull/358|pull#358]]
 * Allow inline svg to handle ''<Variable>'' elements. See [[https://github.com/mixxxdj/mixxx/pull/286|pull#286]]
 * Added the feature to ''<Number_>'' widgets to insert the value int the ''<Text>'' by ''%1''. See [[https://github.com/mixxxdj/mixxx/pull/245|pull#245]]
 * Added [[creating_skins#db_display|<NumberDb>]], that allows to display a ratio scaled in dB. See [[https://github.com/mixxxdj/mixxx/pull/245|pull#245]]
 * <del>Added optional ''mode="stretch"'' attribute for all widgets that support <BackPath>. Default is tiled backpaths, see [[https://github.com/mixxxdj/mixxx/pull/178|pull#178]]</del> Replaced by ''scalemode'' support for widgets, see above.
 * Added ''Transform'' support to ''Connection'' blocks in the skin. Adds a general ValueTransformer class that does simple, invertible transformations on numbers, see [[https://github.com/mixxxdj/mixxx/pull/157|pull#157]]. E.g. to make the gain knob work counterclockwise, use the following connection: <code=xml>
```

\<Connection\>

    <ConfigKey>[Master],volume</ConfigKey>
    <Transform>
      <Invert/>
      <Add>1</Add>
    </Transform>

\</Connection\>\</code\>

``` 
 * You can also configure thresholds with the ''Transform'' feature, see [[https://bugs.launchpad.net/mixxx/+bug/1376277|lp:1376277]]. E.g. to display a widget only with 4 decks configured, use the following connection: <code=xml>
```

\<Connection\>

    <ConfigKey>[Master],num_decks</ConfigKey>
    <Transform>
      <Invert/>
      <Add>4</Add>
    </Transform>
    <BindProperty>visible</BindProperty>

\</Connection\>\</code\>

  - A transformation for boolean *Not* is also possible, see
    [pull\#413](https://github.com/mixxxdj/mixxx/pull/413). E.g. to
    show/hide the library widget, use the following connection:
    `<Connection>
            <ConfigKey persist="true">[Master],show_library</ConfigKey>
            <Transform>
                    <Invert/>
                    <Not/>
            </Transform>
            <BindProperty>visible</BindProperty>
    </Connection>`

<!-- end list -->

``` 
 * Added ''SplitSizesConfigKey'' to [[creating_skins#splitter|<Splitter>]]. Store sizes in a configkey and remember library layout on skin change and restart, see [[https://github.com/mixxxdj/mixxx/pull/209|pull#209]]
 * Use ''visual_bpm'' key instead ''bpm'' so [[creating_skins#bpm_number_display|<BPM>]] does not updates too quickly
 * Added [[creating_skins#effective_musical_key_display|<Key>]], that allows to display the effective musical key after pitch shifting, see [[https://github.com/mixxxdj/mixxx/pull/47|pull#47]]
 * Deprecated **beatsync** pushbutton in favor of **sync_enabled** toggle button.  In most skins and controller setups this can be the same button that ''beatsync'' was (though skins need to change it to a two-state button).
 * Added **sync_master**.  Each deck can optionally be designated explicit master for master sync mode.  This is a toggle button.  (There is also **[InternalClock],sync_master**).
 * Added **[InternalClock],bpm** which shows the speed of the internal synchronization clock.  This is a read/write control.
 * Added "reverseroll", which like rolling beatloops is a pushbutton that enables reverse and slip mode while held.  (recommend adding to right click of reverse button)
 * Added ''<MinimumSize>'', ''<MaximumSize>'', and ''<SizePolicy>'' to all widgets.
 * ''<WidgetGroup>'' changed base classes from QGroupBox to QFrame.
 * ''<Splitter>'' is now a WSplitter which inherits from QSplitter.
 * Added ''<ObjectName>'' to all widgets.
 * Added resizable skin support. To enable, treat ''<skin>'' like a ''<WidgetGroup>'' and give it a ''<Layout>''.
 * Added skin template system.
 * Added ''<ComboBox>'' widget.
 * Added ''<KnobComposed>'' widget.
 * ''<BindProperty>'' does not persist the control value in ''mixxx.cfg'' by default.
 * New syntax for requesting a control to persist in ''mixxx.cfg'': ''<ConfigKey persist="true"></ConfigKey>''.
 * Added support for specifying style in a separate file: ''<Style src="skin:style.qss"/>''
 * ''<EmitOnDownPress>'' is calculated from the connected control and can be omitted.
 * ''<EmitOnPressAndRelease>'' is calculated from the connected control and can be omitted.
 * ''<ConnectValueToWidget>'' is calculated from the connected control and can be omitted.
 * ''<ConnectValueFromWidget>'' is calculated from the connected control and can be omitted.
 * ''<LeftClickIsPushButton>'' is calculated from the connected control and can be omitted.
 * ''<RightClickIsPushButton>'' is calculated from the connected control and can be omitted.
 * Start Mixxx in developer mode: ''Mixxx --developer'' to see extended tooltips for skinner and a menu item and keyboard shortcut to reload changes in skin.xml
 * Added a style-able [[creating_skins#launch_image|<LaunchImage>]] inside the ''<LaunchImageStyle>'' tag
```

## Mixxx 1.11.0

``` 
 *  Removed <BeatHighlightColor>, the highlight color when beatgrid was near playback position in the [[creating_skins#waveform|<Waveform>]], see [[https://bugs.launchpad.net/mixxx/+bug/1112396|lp:1112396]]
 * Added //key// [[creating_skins#trackproperty|TrackProperty]]. This displays the musical key but does not change if the speed/pitch change during playback, see [[https://bugs.launchpad.net/mixxx/+bug/1159141|lp:1159141]]
 * Added <BackPath> node that allows resizable background images for [[creating_skins#widgetgroup|WidgetGroup]] which support color schemes, see [[https://bugs.launchpad.net/mixxx/+bug/1095400|lp:1095400]] & [[https://bugs.launchpad.net/mixxx/+bug/1094785|lp:1094785]]
 * Replaced <MarkerColor> with <AxesColor>, the color of the static horizontal line, and <PlayPosColor>, the color of the static vertical line on the [[creating_skins#waveform|<Waveform>]] and the cursor in the [[creating_skins#waveform_overview|<Overview>]], see [[https://bugs.launchpad.net/mixxx/+bug/1099182|lp:1099182]]
 * [[creating_skins#spinning_vinyl_image_spinny|<Spinny>]] image center according to their own size. Was aligned top/left before. This allows xwax like effects, see [[https://bugs.launchpad.net/mixxx/+bug/1058605|lp:1058605]]
 * The [[skin_colour_scheme_architecture|color filtering architecture]], which allows to create a different coloured version of a skin, does support image transparency.
 * Added the [[creating_skins#splitter|<Splitter>]]> section, which controls the size of child widgets by dragging the boundary between the children.
 * Added the [[creating_skins#widgetstack|<WidgetStack>]]> section, provides a stack of widgets where only one widget is visible at a time. This could be used to make multiple pages of hotcue buttons so you can flip through the pages.
 * Added the [[creating_skins#skin_manifest|<Skin Manifest>]]> section, which tells Mixxx details about the skin and currently allows to specify changes to Mixxx controls that should be executed when the skin is loaded.
 * Replaced <Tooltips> with <TooltipId> key. This avoids the need to write individual tooltip text per node, allows tooltips translation, makes skins more coherent and maintenance easier. Make sure to select the correct ID for each key, available IDs are in //src/skin/tooltips.cpp//
 * Added <AxesColor> to define the color for horizontal/vertical line in in the waveform, see [[creating_skins#waveform|<Visual>]]
 * Added [[creating_skins#recording|<Recording>]] control that allows toggle of recording
 * Added <EndOfTrackColor> in waveform & waveform overview that allow to define the color of the overlay that will be displayed as notification within the last seconds of a track, see [[creating_skins#waveform|<Visual>]] and [[creating_skins#waveform_overview|<Overview>]]
 * Added <Align> to the waveforms options that allows to display only those portions of the waveform which would have been above or below the center. By default, the waveform display is centered about a line and portions will extend both above and below the center, see [[creating_skins#waveform|<Visual>]]
 * Added <SignalLowColor>,<SignalMidColor>,<SignalHighColor> that allow to define different colors for low/mid/high frequencies in waveform & waveform overview. If skin do not provide low/mid/high signal colors it falls back to the color defined in <SignalColors>, see [[creating_skins#waveform|<Visual>]] and [[creating_skins#waveform_overview|<Overview>]]
 * Removed <HfcColor>, the horizontal line`s color in the waveform, see [[creating_skins#waveform|<Visual>]]
 * Removed <ProgressColor> & <ProgressAlpha > option to change the color for track analysis progress visualisation in waveform overview, see [[creating_skins#waveform_overview|<Overview>]]. Track analysis progress will be still visible in waveform overview.
 * Added the <manifest> skin section that allows you to specify the skin title, author, description, etc. and set Mixxx controls on skin load.
```

## Mixxx 1.10.0

``` 
 * Added [[creating_skins#spinning_vinyl_image_spinny|<Spinny>]] image which displays a visual guidance for relative track positioning while mixing
 * Added <Time> widget which displays the current time, see [[creating_skins?&#clock|<Clock>]]
 * Removed rate <Connection> groups from all <NumberRate> controls, now the text does immediately update if rate range or direction changes, see [[creating_skins#pitch_rate_display|<Pitch rate display>]]
 * Added <ProgressColor> & <ProgressAlpha > option to change the color for track analysis progress visualisation in waveform overview, see [[creating_skins#sectionvisual|<Visual>]]
 * Added <BgPixmap> option to the [[creating_skins#sectionvisual|<Visual>]] group. This allows custom background images for waveform and waveform overview. Image transparency is possible for the waveform overview. Remove the BgColor to make it work. If you supply a BgColor it means "paint the background of the overview to this color" so it prevents transparency.
 * Removed default gradient background from waveform display
```

## Mixxx 1.9.1

``` 
 * Extended Mixxx to support now 36 [[creating_skins#hotcue|hotcues]] (was 32 between Mixxx 1.8.0-1.9.0)
 * If no background color for [[creating_skins#waveform_overview|waveform overview]] is provided, the background is treated as transparent
```

## Mixxx 1.9.0

  - added [advanced styling options](/creating_skins#library_display)
    for library
  - added [TrackProperty](/creating_skins#trackproperty) node
  - added [WidgetGroup](/creating_skins#widgetgroup) node
  - added [BPM tap](/creating_skins#bpm_tap) button
  - added [Key lock](/creating_skins#key_lock) button
  - added [Repeat](/creating_skins#repeat) button
  - removed [End of track mode](/creating_skins#end_of_track_mode)
    button
