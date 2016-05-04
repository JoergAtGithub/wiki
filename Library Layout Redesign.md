# Library Layout Redesign

For the moment you can see all the info in the GSoC propsal here:
<https://docs.google.com/document/d/1HaZ5s7PKmE73LacEGbxRJy9LIKi0ZFbZ-emdSQ1m68o/edit?usp=sharing>

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

  - **Library tab:** add to the current LibrarySidebar a collapsed
    version (removing the Qt Treeview in some cases).
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
    useful for small screens.
  - **Library view:** now it has the playlists, the crates and the songs
    all together.

## Deliverables

### v.0.1.0 - LibrarySidebar collapsed

This is the first step in the project, the LibrarySidebar will have
small buttons instead of the current treeview items to select the
desired option. If the buttons do not fit then there is another button
(+) that opens a popup where there are the remaining options. The model
of this will be implemented like a tree but the 1st level will be the
buttons and the 2nd, 3rd… will be a real Qt Treeview allowing to make a
better integration with current Mixxx code. Theoretically the current
SidebarModel class should not be changed with this new layout because I
only will be changing the LibrarySidebar class model view. This will be
a new class and will not replace the existing LibrarySidebar so there
will be a collapsed and a expanded version of the LibrarySidebar.

\[Picture here\]

### v.0.2.0 - Library View

This step will have some releases:

#### v.0.1.1 Add Playlist/Crates view

When the user selects a playlist or a crate, a split view will appear
with two Qt TableViews one (at left) for the current songs in library
and the other (at right) for the songs in the playlist/crate. The user
can add songs with the right click context menu or drag them directly
from the left to the right.

\[picture here\]

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

\[picture here\]

#### v.0.2.1 Add advanced grouping

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

\[picture here\]

### v.0.3.0 Browse PC view

This view will extend the current Browse PC view adding the option to
view a single folder instead of all the system folders tree. When the
user selects a folder it shows all the songs containing This view is
split in a Qt Treeview (at left) and a Qt Tableview (at right). The left
view allows the user to browse the computer’s folders. The browse can be
in two different ways, a tree browse or a folder browse (can be selected
at preferences). The right view shows the found songs in the selected
folder (it can also show the songs in the subdirs inside the selected
folder, can be selected at preferences).

## Timeline:

W1 May 9th - May 15th:

  - Create Manager class prototype
  - Check viability of Manager class

W2 May 16th - May 22nd:

  - Code final Manager class
  - Implement LibrarySidebar collapsed version still without crates and
    playlists added

W3 May 23rd - May 29th:

  - Implement LibrarySidebar allowing the Manager to switch between
    collapsed and expanded versions.
  - Add crates and playlists to LibrarySidebar collapsed

W4 May 30th - June 5th:

  - Add crates and playlists to LibrarySidebar collapsed

W5 June 6th - June 12th:

W6 June 13th - June 19th:

W7 June 20th - June 26th:

W8 June 27th - July 3rd:

W9 July 4th - July 10th:

W10 July 11th - July 17th:

W11 July 18th - July 24th:

W12 July 25th - July 31st:

W13 August 1st - August 7th:

W14 August 8th - August 14th:

W15 August 15th - August 23rd:
