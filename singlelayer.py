#!/usr/bin/python
from gdsCAD import *

# Create a Cell and add the box
cell=core.Cell('TOP')

# Create three boxes on layer 2 of different sizes centered at
# the origin and add them to the cell.
for l in (3,6,10):
    box=shapes.Box((-l,-l), (l,l), width=0.2, layer=2)
    cell.add(box)

# Create a layout and add the cell
layout = core.Layout('LIBRARY')
layout.add(cell)

# Save the layout and then display it on screen
layout.save('output.gds')
layout.show()

