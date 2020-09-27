# The game map

from place import Place
from objects import *

# For non-functional objects
# Thing(name, description)

# Define functional objects in objects.py

# Place(name, address, description, contents)
# - name is a string
# - address is a tuple with 2 numbers
# - description is a string
# - contents is a set.  It can be the empty set: {}

# The order of the Places isn't important. Arrange them in a way that makes sense to you.
# It is very important that addresses all touch correctly.
# Use a paper map to plan everything carefully.
map = {
  Place('the barn', (0,0), 'The old barn is full of hay and the smell of animals', {Flashlight()}),
  Place('the yard', (-1,0), 'The yard between the barn and the house is overgrown with weeds', {}),
  Place('the house', (-2,0), 'The abandonded house is falling apart at the seams', {Battery()})
}