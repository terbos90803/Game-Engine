# Defines the class of places

import utils

# The methods on this class are mostly accessors and should be self-explanatory

class Place:
  def __init__(self, name, address, description, contents):
    self.name = name # string : short name for this Place
    self.address = address # 2-tuple : cartesian address of this Place
    self.description = description # string : full description of this Place
    self.contents = contents # set of Thing : the things that start out in this Place
    self.visited = False # Boolean : has the player been here before?

  def get_name(self):
    return self.name

  def get_address(self):
    return self.address

  def get_description(self):
    return self.description

  def get_visited(self):
    return self.visited

  def get_contents(self):
    return self.contents

  def contains(self, item):
    return item in self.contents

  def print_contents(self):
    if len(self.contents) > 0:
      items = []
      for i in self.contents:
        items.append(i.get_name())
      utils.print_list('You see: ', items)

  # Remove directions from a list if you have closed doors or barriers
  # This method is the default implementation for all placed and must not change anything
  # If you need to have special behavior for a specific place, then make a derived class
  # from Place and change the behavior of prune_directions() there.
  def prune_directions(self, directions):
    return directions

  # Describe this place
  # The list of valid_directions passed in is based on the map.
  # If you have any doors or barriers in this place, then you need to remove directions
  # from the list using prune_directions()
  def describe(self, valid_directions, do_describe):
    print('You are in', self.name)
    if do_describe or not self.visited:
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