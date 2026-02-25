# Coder Stats
Get stats for languages and stars of users and repos, both for CodeBerg and for GitHub.

# Languages
<!-- TODO: Deploy and add an example --->
## User languages
```md
![https://<coder-stats-instance>/api/v1/codeberg/u/sanngridhr/languages/pie.svg](Sanngriðr's languages)
```
## Available options
### Pie-chart
| Option             | Type                            | Default        | Description
|--------------------|---------------------------------|----------------|------------
| limit              | integer or "auto"               | "auto"         | use top most `limit` languages. "auto" sets limit to the number of available theme colours
| include_forks      | boolean                         | false          | whether to include forks or not
| direction          | "clockwise" or "anti-clockwise" | "clockwise"    | direction of the piechart
| font               | string                          | "sans"         | labels font
| gap                | float                           | .05            | gap between pie wedges
| lump_small_data    | boolean                         | true           | whether to include an `Other` label that contains small data or to discard it
| radius             | float                           | .8             | pie radius
| start_angle        | float                           | 90             | starting angle of the first wedge
| theme              | [theme](#available-themes)      | "flexoki-dark" | theme name
| theme_reverse      | boolean                         | false          | whether to reverse theme colours on the pie or not
| theme_transparency | 00-FF hex string                | "FF"           | pie chart transparency
| width              | float                           | .02            | wedge width

# Themes
## Available themes
TBA