# Defines the class of places

import utils

# The methods on this class are mostly accessors and should be self-explanatory

class Place:
  def __init__(self, name, description, contents):
    self.name = name # string : short name for this Place
    self.description = description # string : full description of this Place
    self.contents = contents # set of Thing : the things that start out in this Place
    self.paths = dict() # dictionary of direction/Path : where you can go from here
    self.visited = False # Boolean : has the player been here before?

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description

  def get_visited(self):
    return self.visited

  def get_contents(self):
    return self.contents

  def contains(self, item):
    return item in self.contents

  def connect(self, paths):
    self.paths = paths

  def print_contents(self):
    if len(self.contents) > 0:
      items = []
      for i in self.contents:
        items.append(i.get_name())
      utils.print_list('You see: ', items)

  # Describe this place
  def describe(self, force_describe = False):
    print('You are in', self.name)
    if force_describe or not self.visited:
      print(self.description)
      self.print_contents()
      utils.print_list('You can go: ', self.prune_directions(valid_directions))
      self.visited = True

  # Lookup an item by name in this Place.
  # return the item if it's here.
  def get_item(self, item_name):
    for i in self.contents:
      if i.get_name() == item_name:
        return i;
    return None

  def remove_item(self, item):
    if item in self.contents:
      self.contents.remove(item)

  def put_item(self, item):
    if item != None:
      self.contents.add(item)