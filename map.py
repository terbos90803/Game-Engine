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
# - description is a string list
# - contents is a set.  It can be the empty set: {}

barn = Place(
  'the barn', 
  ['The old barn is full of hay and the smell of animals'], 
  {Flashlight()})

yard = Place(
  'the yard', 
  ['The yard between the barn and the house is overgrown with weeds'], 
  {Thing('rock', 'a small rock', True), Thing('boulder', 'a large boulder', False)})

house = Place(
  'the house', 
  ['The abandonded house is falling apart at the seams'], 
  {Battery()})

pantry = Place(
  'the pantry',
  ['The pantry has many empty shelves'],
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

# connect(place1, 'direction leaving place1', Path, 'direction leaving place2', place2)
#
# The easy way to read this is from the outside in.
#   connect(yard, 'east', Path(), 'west', barn)
#     from the yard, go east through the Path to get to the barn
#     from the barn, go west through the Path to get to the yard
#
# Note: the first/second order doesn't matter.
#   connect(yard, 'east', Path(), 'west', barn)
# is the same as
#   connect(barn, 'west', Path(), 'east', yard)

connect(yard, 'east', Path(), 'west', barn)
connect(house, 'east', Door(), 'west', yard)
connect(house, 'north', Door(False, True, 'rock'), 'south', pantry)