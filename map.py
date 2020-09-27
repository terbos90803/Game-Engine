# The game map

from place import Place
from path import *
from objects import *


# For non-functional objects
# Thing(name, description)
# Example: Thing('rock', 'just a rock')

# Define functional objects in objects.py
# Example: Flashlight needs to turn on and off, so it is a functional object


#
# Step 1: make all the Places
#

# Place(name, description, contents, paths)
# - name is a string
# - description is a string
# - contents is a set.  It can be the empty set: {}

barn = Place(
  'the barn', 
  'The old barn is full of hay and the smell of animals', 
  {Flashlight()})

yard = Place(
  'the yard', 
  'The yard between the barn and the house is overgrown with weeds', 
  {Thing('rock', 'a small rock', True), Thing('boulder', 'a large boulder', False)})

house = Place(
  'the house', 
  'The abandonded house is falling apart at the seams', 
  {Battery()})

pantry = Place(
  'the pantry',
  'The pantry has many empty shelves',
  {})

#
# Step 2: Where to start
#
start = barn


#
# Step 3: Connect the places together
#

# Use Path and Door to connect Places together.
# Make sure each place is connected to something else.
# Your paper map is really important to get this right.

# connect('from direction leaving place1', place1, 'from direction leaving place2', place2, Path)
connect('west', barn, 'east', yard, Path())
connect('west', yard, 'east', house, Door())
connect('north', pantry, 'south', house, Door(False, True, 'rock'))