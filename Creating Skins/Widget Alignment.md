# Widget alignment

The children of a WidgetGroup (or the **skin** node) can be aligned
vertically and horizontally in its available space. For example, imagine
we have a WidgetGroup (depicted as the red box in the drawing) that
contains a Widget (depicted as the green box). The size of the
WidgetGroup is 300x300 and the size of the Widget is 50x50. By default,
Mixxx will center the Widget in the WidgetGroup horizontally and
vertically.

![Widget vertically and horizontally
centered](/creating_skins/widget_center_alignment.svg)

However, we can vertically align the Widget on top or on bottom of the
space the WidgetGroup occupies, and likewise for the horizontal
alignment. This gives us nine possible alignments for the Widget:

![Possible Widget
alignments](/creating_skins/widget_possible_alignments.svg)

To determine the alignment we want, we must set the property
**qproperty-layoutAlignment** of the WidgetGroup. First we need to give
a name to our WidgetGroup with the ObjectName tag and then set the
property in the skin stylesheet. **qproperty-layoutAlignment** property
can take the following values enclosed in single quotation marks:

| Horizontal alignment | Vertical alignment |
| -------------------- | ------------------ |
| AlignLeft            | AlignTop           |
| AlignHCenter         | AlignVCenter       |
| AlignRight           | AlignBottom        |

A combination of an horizontal and a vertical alignment can be specified
writing a value from each column and separating them with a vertical bar
like this:

    'AlignHCenter | AlignTop'

An additional **AlignCenter** value can be specified. It is a shorthand
for **'AlignVCenter | AlignHCenter'**.

## Examples

Let's see how alignment works through a series of examples.
