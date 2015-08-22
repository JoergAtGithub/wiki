# Widget alignment

The children of a WidgetGroup can be aligned vertically and horizontally
in its available space. For example, imagine we have a WidgetGroup
(depicted as the red box in the drawing) that contains a Widget
(depicted as the green box). The size of the WidgetGroup is 300x300 and
the size of the Widget is 50x50. By default, Mixxx will center the
Widget in the WidgetGroup horizontally and vertically.

![Widget vertically and horizontally
centered](/creating_skins/widget_center_alignment.svg)

However, we can vertically align the Widget on top or on bottom of the
space the WidgetGroup occupies, and likewise for the horizontal
alignment. This gives us nine possible alignments for the Widget:

![Possible Widget
alignments](/creating_skins/widget_possible_alignments.svg)

The only widgets in Mixxx skin system that accept alignment properties
are WidgetGroups. A WidgetGroup can handle the alignment properties no
matter what its parent is, i.e. another WidgetGroup, a WidgetStack, a
SizeAwareStack, an Splitter or the skin
