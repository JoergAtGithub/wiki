# Library Layout Redesign

All the weekly development will be posted here:
<http://jmigual.blogspot.com>

## Summary

This proposal consists of the implementation of a library layout
redesign with tabs for special purpose. The Qt Treeview will be changed
to a vertical layout of buttons allowing more space in many views (from
this point this will be called the LibrarySidebar collapsed version, the
current existing LibrarySidebar will be called the expanded version).
All things will take in account the controllers. Also, many things are
inspired in [Clementine](https://www.clementine-player.org/) player and
others are inspired in the library layout redesign discussion thread
([Bug-\.md#986704](https://bugs.launchpad.net/mixxx/+bug/986704)). This
will be developed in different small releases. The changes will be the
following:

  - **Library tree:** change the library tree to small buttons and some
    Lbrary Features will keep their existing tree views. Also there will
    be the option to have two LibraryFeatures at the same time.
  - **Library view:** the Treeview will be changed to create a one
    similar to the one existing in Clementine player
  - **Browse PC view:** this will add to this tab the option to see
    folders as a tree or only a single folder (selected in preferences).

## Benefits

With the current layout search songs by artist or by album is not very
intuitive. To be able to select the desired song quickly and using a
controller the layout must guarantee a fast access to all options. This
layout is designed grouping similar things in one tab. Also with this
new layout it will be able to fit in small screens (1024\*600).

  - **Library tab:** now it has small buttons allowing more space,
    useful for small screens, and for bigger screens there's the option
    to have two library features at the same time.
  - **Library view:** now it has the playlists, the crates and the songs
    all together and it allows to sort the songs by artist, album...

## Expected result

The main idea of this project is to allow a future addition of many
features to the library. Every feature will have two panes (right and
left pane), the left pane has the controls or trees needed by it (e.g.
the crates feature) and the right pane has the table (if a feature does
not need the left pane it is hidden). There will be the option to have
two (or N) features showing at the same time so, when the user enables a
second feature, it shares the left pane in a static stack and both right
panes are visible. This is not limited to only two right pane
containers, it can be up to N pane containers.

This is inspired in the Nemo File Manager (if you enable the extra pane
in view menu). When the user focuses one of the two right panes, the
left pane is changed to show the focused feature's left pane.

[[/media/gsoc_2016/libraryfeature_0_1_0_2.png|]]

As we can see in the image, a button bar will have all the Library
Features allowing the user to select a new one (it will be added in the
current focused pane). For the final version of the button bar the user
will be able to select which features he wants to be shown in the button
bar and to allow the user selecting this features the Library Legacy
Tree will be shown allowing the user to select the feature from it, in
the midterm version this won't be created already.

Also, all the tables shown in the right panes will have the Search Bar.
Moreover, there will be the option to show only one pane allowing the
user to have the current Mixxx layout.

Here's an "exploded" drawing of the feature's mapping in one pane or
another:

[[/media/gsoc_2016/library_layout_redesign/library_feature_stack_5.png|]]

The feature A is loaded in the right pane container 1 because it was
focused when clicking the A button in the button bar. If the pane
container 2 had been focused then the feature A would have been loaded
in the pane container 2.

Also, there will be three types of Library Features:

  - Auto DJ like features that have a track table (right pane) and a set
    of control widgets (left pane)
  - Crates like features with the tree at the left pane and the table at
    the right pane
  - Features without a track table like "Notes" feature (with nothing at
    the left pane)

The key mappings to handle the focus feature will be the following:

  - **Up**: SelectPrevItem
  - **Down**: SelectNextItem
  - **Left**: move selection left / collapse
  - **Right**: move selection right / expand
  - **Enter**: ChooseItem
  - **Tab**: ToggleFocusWidget

The mapping for the MIDI/HID control will be the same as the related in
the following PR: <https://github.com/mixxxdj/mixxx/pull/953>

To handle all of this in the skin.xml there will be the following tags:

  - LibrarySideBar for the ButtonBar
  - LibrarySideBarExpanded for the Library's Left Pane
  - Library for the Library's Pane, it can be declared multiple times
    and all of them will appear and this will allow to show two features
    at once. Every declared pane must have a unique <id></id> setting to
    allow the SearchBox to work.
  - SearchBox can be connected with the corresponding pane setting the
    same<Id></Id> tag.
  - LibraryBreadCrumb show's a breadcrumb of the current shown pane to
    allow visual feedback of the LibraryFeature pane change. It is
    connected with a pane with the <Id></Id> tag.
  - CoverArt for the existing cover art (will not be altered)

Here is an example with the playlists:

[[/media/gsoc_2016/libraryfeature_playlists_2.png|]]

To create the layout for this example in the skin.xml file it will be
like this:

``` xml
<WidgetStack>
  <Layout>Horizontal</Layout>
  <Children>
    <LibrarySidebar></LibrarySidebar>
    <LibrarySidebarExpanded></LibrarySidebarExpanded>
    
    <!-- For Track table 1 -->
    <WidgetStack>
      <Layout>Vertical</Layout>
      <Children>
        <SearchBox>
          <Id>1</Id>
        </SearchBox>
        <LibraryBreadCrumb>
          <Id>1</Id>
        </LibraryBreadCrumb>
        <Library>
          <Id>1</Id>
        </Library>
      </Children>
    </WidgetStack>
    
    <!-- For Track table 2 -->
    <WidgetStack>
      <Layout>Vertical</Layout>
      <Children>
        <SearchBox>
          <Id>2</Id>
        </SearchBox>
        <LibraryBreadCrumb>
          <Id>2</Id>
        </LibraryBreadCrumb>
        <Library>
          <Id>2</Id>
        </Library>
      </Children>
    </WidgetStack>
  </Children>
</WidgetStack>
```

Also to show the focus in the panes a new element in the QSS is added.
In this example a small border is added in the WBaseLibrary to make
clear the focus change.

``` css
/* When the WBaseLibrary does not have the focus */
WBaseLibrary[showFocus="0"] {
    padding: 2px 0 0 0;
    border: none;
}

/* When the WBaseLibrary has the focus */
WBaseLibrary[showFocus="1"] {
    padding: 2px 1px 1px 1px;
    border-top: 2px solid aqua;
}
```

## Deliverables

### v.0.1.0 - LibraryFeature

#### v.0.0.1 - LibraryViewManager

This is the first step in the project an as the project will add some
elements to the current GUI, it is better to have something to handle
all this new library features. This is the first step in the project and
will change a bit the existing Library class that handles the relation
between the Mixxx frontend (WLibrary, WLibrarySidebar, DlgRecording...)
and the backend (Library, LibraryFeature, BasePlaylistFeature...).
Currently all related to the Mixxx library is a LibraryFeature and all
of this is currently handled by the Library class that will respect the
Mixxx init refactor idea by rryan2 [link](mixxx_init_refactor).

The main changes to the Library class will be to add the option of
multiple right panes (currently by deafult there's one pane handled with
the WLibrary class). Also to make things easy a new class will be
introduced, LibraryPaneManager and there will be one of this classes for
each pane helping with events like focusChange. Here is the UML for the
relations between the existing Library and the LibraryPaneManager:

[[/media/gsoc_2016/library_layout_redesign/uml/general_7.png|]]

Here there's a detailed view of the stacked widget of every pane:

[[/media/gsoc_2016/library_layout_redesign/uml/widgetstack_4.png|]]

As it can be seen every pane will have one WLibrary and the sidebar
expanded will have a WBaseLibrary. When the user selects a feature the
library must decide in which pane this feature should be shown. And once
decided, the Library must show both the SidebarExpanded and the Pane of
the feature.

Here's a detailed view of the Library and LibraryFeature relations and
inheritance:

[[/media/gsoc_2016/library_layout_redesign/uml/libraryfeature_4.png|]]

As it can be seen the LibraryFeature instead of having the bindWidget()
function it will have a bindSidebarWidget() and bindPaneWidget()
allowing to have widgets without a sidebar widget or with a sidebar
widget that is not a tree (e.g. buttons in AutoDJ).

#### v.0.0.2 - LibrarySidebar

After the manager is created the LibrarySidebar must be changed to have
small buttons (button bar) instead of the current treeview items. If the
buttons do not fit then there is another button (+) that opens a popup
where there are the remaining options. As noted in the previous sections
the library features that need a tree will have it and it will be shown
next to the buttons bar.

Here the LibraryViewManager must handle the clicked() signal of the
buttons and display the proper feature for the clicked button. With this
design the current existing tree view won't be the same and will be
ignored or changed.

[[/media/gsoc_2016/library_0_1_0_2.png|]]

#### v.0.0.3 - Two panel focus change

When the LibrarySidebar is finished and is functional, then the second
right panel is added and the necessary methods to handle the focus
change and to change the tree on focus changed are added. This should be
an easy step after coding all the important changes in the v.0.0.2

### v.0.2.0 - Library View

#### v.0.1.1 Add Playlist/Crates view

This changes the current playlist/crates view to one that when the user
selects a playlist or a crate, a split view will appear with two Qt
TableViews one (at left) for the current songs in library and the other
(at right) for the songs in the playlist/crate. The user can add songs
with the right click context menu or drag them directly from the left to
the right.

[[/media/gsoc_2016/library_layout_redesign/library_0_1_1_2.png|]]

#### v.0.1.2 Add Clementine like view

Songs are ordered in the treeview and a button allows different sorting.
To do this the view has two modelers one for the menu (Library, Autodj,
iTunes…) and other for the songs. This option will keep in mind the
current skins and will allow to customize this new buttons. There are
the following sorting options to group by:

  - Artist
  - Artist / Album
  - Artist / Year - Album
  - Album
  - Genre / Artist
  - Genre / Artist / Album

[[/media/gsoc_2016/library_layout_redesign/library_0_1_2_3.png|]]

#### v.0.1.2.1 Add advanced grouping

Allows the user to select the 1st, 2nd and 3rd level for grouping
elements.

### v.0.2.0 History view

Currently History view needs a bit of changes. In this thread
(<https://bugs.launchpad.net/mixxx/+bug/1127120>) there's a proposal for
a history view change, changing the sort order and sorting in a tree in
the following way:

  - Year
  - Month

<!-- end list -->

``` 
    * Date
```

### v.0.3.0 Add new search behavior

Currently there's a small problem with the loose of context. If a party
guest comes and and requests a track "Do you have the song XXX from last
year?" the DJ must be able to search the song and return to the previous
state he was before searching the song.

#### v.0.2.1.0 Save state

To achieve this currently the scroll position is saved but not the sort
order. So this will store the sort order too to allow a full return
after searching the selected song.

#### v0.2.1.1 Sticky views

The other added option are the sticky views, this should allow the user
to save the current state (search, scroll and sort order) to restore it
later.

When the bugfixing is done this becomes (v. 0.3.0).

### v.0.4.0 - Browse PC view

This view will extend the current Browse PC view adding the option to
view a single folder instead of all the system folders tree. When the
user selects a folder it shows all the songs containing This view is
split in a Qt Treeview (at left) and a Qt Tableview (at right). The left
view allows the user to browse the computer’s folders. The browse can be
in two different ways, a tree browse or a folder browse (can be selected
at preferences). The right view shows the found songs in the selected
folder (it can also show the songs in the subdirs inside the selected
folder, can be selected at preferences).

[[/media/gsoc_2016/library_0_3_0.png|]]

## Timeline

~~W1 May 9th - May 15th:~~

  - ~~Create Manager class prototype~~
  - ~~Check viability of Manager class~~

~~W2 May 16th - May 22nd:~~

  - ~~Code final Manager class (CHANGED)~~

~~W3 May 23rd - May 29th~~:

  - ~~Fix midterm and weekly goals~~
  - ~~Describe the required classes and behavior on the wiki~~

~~W4 May 30th - June 5th~~:

  - ~~Begin coding new LibraryFeature and LibraryViewManager classes
    (v.0.0.1)~~

~~W5 June 6th - June 12th~~:

  - ~~Finish coding of new LibraryFeature and LibraryViewManager classes
    (v.0.0.1)~~

~~W6 June 13th - June 19th~~:

  - ~~Study for exams~~
  - ~~Add new button bar~~
  - ~~Add sidebar expanded~~
  - ~~Add multiple panes view~~
  - ~~Accept drop targets~~
  - ~~Add v.0.0.2 design to all skins~~
  - ~~Begin implementing new LibrarySidebar with the LibraryFeature
    (v.0.0.2)~~

~~W7 June 20th - June 26th (mid term evaluations)~~:

  - ~~Full time study for exams (until June 23rd)~~
  - ~~Bugfixing new LibrarySidebar~~
  - ~~Check properly keyboard mapping (after June 23rd)~~

~~W8 June 27th - July 3rd~~:

  - ~~Show breadcrumbs~~
  - ~~Finish coding of new LibrarySidebar (v.0.0.2)~~
  - ~~Add two panel focus change (v.0.0.3)~~
  - ~~Separate LibraryFeature to allow a future plugin behaviour~~
  - ~~Finish of LibraryFeature section (v.0.1.0) -\> Merge (v.0.1.0)~~

~~W9 July 4th - July 10th~~:

  - ~~Implement advanced grouping like Clementine (v.0.1.2.1).~~
  - Favorites in sidebar - "More" button in sidebar

~~W10 July 11th - July 17th~~:

  - ~~Add new crates and playlists view (v.0.1.1)~~ 

W11 July 18th - July 24th:

  - ~~Implement new History Feature (v.0.2.0)~~
  - Implement new search behavior (v.0.3.0):
  - ~~Implement save state (v.0.2.1)~~

W12 July 25th - July 31st:

  - ~~Bugfixing~~

W13 August 1st - August 7th:

  - Implement folders in Library (like Browse PC view) (v.0.4.0)
  - Add icons only option in WButtonBar
  - Add <library_icon_color> tag
  - Fix double sidebar
  - Fix search selection

W14 August 8th - August 14th:

  - Implement new search behavior (v.0.3.0):
  - Begin implementing sticky views (v.0.2.2)
  - Bugfixing
  - Writing documentation 

W15 August 15th - August 23rd:

## Weekly reports

  - [\#0 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/0-weekly-report.html)
  - [\#1 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/1-weekly-report.html)
  - [\#2 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/2-weekly-report.html)
  - [\#3 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/3-weekly-report.html)
  - [\#4 Weekly
    report](http://jmigual.blogspot.com.es/2016/06/4-weekly-report.html)
  - [\#5 Weekly
    report](http://jmigual.blogspot.com.es/2016/06/5-weekly-report.html)
  - [\#6 Weekly
    report](http://jmigual.blogspot.com.es/2016/06/6-weekly-report.html)
  - [\#7 Weekly
    report](http://jmigual.blogspot.com.es/2016/06/7-weekly-report.html)
  - [\#8 Weekly
    report](http://jmigual.blogspot.com.es/2016/07/8-weekly-report.html)
  - [\#9 Weekly
    report](http://jmigual.blogspot.com.es/2016/07/9-weekly-report.html)
  - [\#10 Weekly
    report](http://jmigual.blogspot.com.es/2016/07/10-weekly-report.html)
