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
([Bug \#986704](https://bugs.launchpad.net/mixxx/+bug/986704)). This
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
two features showing at the same time so, when the user enables a second
feature, it shares the left pane in a statick stack and both right panes
are visible.

This is inspired in the Nemo File Manager (if you enable the extra pane
in view menu). When the user focuses one of the two right panes, the
left pane is changed to show the focused feature's left pane.

[[/media/gsoc_2016/libraryfeature_0_1_0_2.png|]]

As we can see in the image, a button bar will have all the Library
Features allowing the user to select a new one (it will be added in the
current focused pane). Also, all the tables shown in the right panes
will have the Search Bar. Moreover, there will be the option to show
only one pane allowing the user to have the current Mixxx layout.

Also, there will be three types of Library Features:

  - Auto DJ like features that have a track table (right pane) and a set
    of control widgets (left pane)
  - Crates like features with the tree at the left pane and the table at
    the right pane
  - Features without a track table like "Notes" feature (with nothing at
    the left pane)

Here is an example with the playlists:

[[/media/gsoc_2016/libraryfeature_playlists_2.png|]]

## Deliverables

### v.0.1.0 - LibraryFeature

#### v.0.0.1 - LibraryViewManager

This is the first step in the project an as the project will add some
elements to the current GUI, it is better to have something to handle
all this new library features. Then, all related to the Library will be
a LibraryFeature and all of this will be handled by the
LibraryViewManager class that will respect the Mixxx init refactor idea
by rryan2 [link](mixxx_init_refactor). The main function for the
LibraryViewManager will be to set the proper left pane when the focus is
changed and show the selected LibraryFeature when clicked in the button
bar. Here is the UML for the LibraryViewManager and LibraryFeature
classes:

[[/media/gsoc_2016/librarymanager_2.png|]]

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

[[/media/gsoc_2016/library_0_1_1.png|]]

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

[[/media/gsoc_2016/library_0_1_2.png|]]

#### v.0.1.2.1 Add advanced grouping

Allows the user to select the 1st, 2nd and 3rd level for grouping
elements.

#### v.0.2.0 Add new search engine

add a new search engine where the user can select the filtering options,
showing the following menu:

  - Search method (v. 0.1.3.0)
  - All
  - Songs
  - Artists
  - Albums
  - File name
  - Search location (v. 0.1.3.1)
  - All
  - This view
  - Playlists
  - Crates

When the bugfixing is done this becomes (v. 0.2.0).

[[/media/gsoc_2016/library_0_2_0.png|]]

### v.0.3.0 - Browse PC view

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

W3 May 23rd - May 29th:

  - Fix midterm and weekly goals
  - Describe the required classes and behavior on the wiki

W4 May 30th - June 5th:

  - Begin coding new LibraryFeature and LibraryViewManager classes
    (v.0.0.1)

W5 June 6th - June 12th:

  - Finish coding of new LibraryFeature and LibraryViewManager classes
    (v.0.0.1)

W6 June 13th - June 19th:

  - Study for exams
  - Begin implementing new LibrarySidebar with the LibraryFeature
    (v.0.0.2)

W7 June 20th - June 26th (mid term evaluations):

  - Full time study for exams (until June 23th)

W8 June 27th - July 3rd:

  - Finish coding of new LibrarySidebar (v.0.0.2)
  - Add two panel focus change (v.0.0.3)
  - Finish of LibraryFeature section (v.0.1.0) -\> Merge (v.0.1.0)

W9 July 4th - July 10th:

  - Implement advanced grouping like Clementine (v.0.1.2.1).

W10 July 11th - July 17th:

  - Add new crates and playlists view (v.0.1.1) 

W11 July 18th - July 24th:

  - Implement new filtering options (v.0.2.0):
  - Implement search location filtering options (v.0.1.3.0)
  - Implement search method filtering options (v.0.1.3.1)
  - Write tests and bugfixing to filtering options (v.0.1.3.1 -\>
    v.0.2.0)
  - Merge v.0.2.0

W12 July 25th - July 31st:

  - Implement new Browse PC view, needs to be Bullet Proof (v.0.3.0)
  - Merge v.0.3.0

W13 August 1st - August 7th:

  - Bugfixing
  - Writing documentation 

W14 August 8th - August 14th:

W15 August 15th - August 23rd:

## Weekly reports

  - [\#0 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/0-weekly-report.html)
  - [\#1 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/1-weekly-report.html)
  - [\#2 Weekly
    report](http://jmigual.blogspot.com.es/2016/05/2-weekly-report.html)
