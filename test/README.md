## Pin Connections

| Pin Number | Pin Name      | Connected To      |
|------------|---------------|-------------------|
| 1          | VCC           | +5V               |
| 2          | GND           | Ground            |
| 3          | Digital Pin 2 | LED Positive Leg  |
| 4          | Digital Pin 3 | Button            |
| 5          | Analog Pin A0 | Potentiometer Wiper |



## Circuit Diagram

  +5V
   |
   +
  ---
 |   |
 |   |
---  | 10k Ohm Resistor



### Using SVG or HTML for More Complex Diagrams

If you need a more complex diagram, you can use inline SVG or HTML in your markdown. This is more advanced and allows for more detailed representations.

#### Example:

```markdown
## Circuit Diagram

<svg width="200" height="200">
  <circle cx="100" cy="50" r="20" stroke="black" stroke-width="3" fill="red" />
  <line x1="100" y1="70" x2="100" y2="150" style="stroke:rgb(0,0,0);stroke-width:2" />
  <rect x="90" y="150" width="20" height="40" style="fill:blue;stroke:black;stroke-width:2;opacity:0.5" />
  <text x="100" y="170" font-family="Verdana" font-size="15" fill="black">Resistor</text>
</svg>







