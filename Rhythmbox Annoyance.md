# Rhythmbox annoyance(s)

\<rant\>Sheesh, all these music programs insist on doing me 'favors'
that I didn't ask for. Like, it has it's own idea of a "music
collection", which is "every playable file I ever come across, ever",
when the real answer is for a person to "put your music in a folder, and
point to it". \</rant\>

rhythmbox accumulates every playable file ever seen into it's
"collection". You'd think that the Edit -\> Preferences -\> Music tab
path would be where it looked for music, but you would be wrong.

To enforce that rhythmbox actually *do so*, occasionally do this:

Quit rhythmbox,

    $ rm .gnome2/rhythmbox/rhythmdb.xml

Then restart.
