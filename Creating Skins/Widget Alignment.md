# Widget alignment

The children of a WidgetGroup (or of the **skin** node) can be aligned
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

Also, **'AlignCenter'** value can be specified. It is a shorthand for
**'AlignVCenter | AlignHCenter'**.

## Examples

Let's see how alignment works through a series of examples. We have the
following skin consisting of a clock and a blue empty WidgetGroup that
we would normally fill with other widgets, but let's keep it empty for
the sake of simplicity.

[[/media/creating_skins/skin_example_1.png|Skin first example]]

This are the skin.xml and the style.qss files:

``` xml
<!DOCTYPE skin>
<skin>
  <manifest>
    <title>WidgetAlignment</title>
    <author>Ferran Pujol Camins</author>
    <version>1.12.0.01</version>
    <description>An example skin showing how to properly align widgets.</description>
    <language>en</language>
    <license>Creative Commons Attribution, Share-Alike 3.0 Unported</license>
    <attributes>
      <attribute config_key="[Master],num_decks">2</attribute>
    </attributes>
  </manifest>

  <ObjectName>Mixxx</ObjectName>
  <Style src="skin:style.qss"/>

  <MinimumSize>500,200</MinimumSize>
  <SizePolicy>me,me</SizePolicy>
  <Layout>horizontal</Layout>

  <Children>
    <WidgetGroup>
      <ObjectName>SkinStuff</ObjectName>
      <Size>200,10me</Size>
      <Children></Children>
    </WidgetGroup>

    <Time>
      <ObjectName>Clock</ObjectName>
      <SizePolicy>min,min</SizePolicy>
    </Time>
  </Children>
</skin>
```

``` css
#Mixxx {
  background-color: #000000;
}

#SkinStuff {
  background-color: #100030;
}

#Clock {
  font: bold 23px;
  color: #FFFFFF;
  background-color: #300010;
}
```
