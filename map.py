# The game map

from place import Place
from objects import *


# For non-functional objects
# Thing(name, description)
# Example: Thing('rock', 'just a rock')

# Define functional objects in objects.py
# Example: Flashlight needs to turn on and off, so it is a functional object


# Place(name, address, description, contents)
# - name is a string
# - address is a tuple with 2 numbers
# - description is a string
# - contents is a set.  It can be the empty set: {}

# The order of the Places isn't important. Arrange them in a way that makes sense to you.
#
# It is very important that addresses all touch correctly.
# i.e. (0,0) touches (1,0), but (0,0) does not touch (1,1) directly, you have to go
# through (1,0) to get there.
#
# If there is a wall or door between (0,0) and (0,1), 
#
# Use a paper map to plan everything carefully.
map = {
  Place('the barn', (0,0), 'The old barn is full of hay and the smell of animals', {Flashlight()}),
  Place('the yard', (-1,0), 'The yard between the barn and the house is overgrown with weeds', {Thing('rock', 'a small rock', True), Thing('boulder', 'a large boulder', False)}),
  Place('the house', (-2,0), 'The abandonded house is falling apart at the seams', {Battery()})
}