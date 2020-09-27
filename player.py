# Defines the player

from direction import Direction
import utils

class Player:
  def __init__(self, address=(0,0), health=100, inventory=set()):
    self.address = address # Begin at the origin
    self.health = health # integer 0-100
    self.inventory = inventory # set of things

  def get_address(self):
    return self.address
    
  def get_health(self):
    return self.health

  def print_inventory(self):
    items = []
    for i in self.inventory:
      items.append(i.get_name())
    if len(items) == 0:
      items = ['nothing']
    utils.print_list('You have: ', items)

  def is_alive(self):
    return self.health > 0

  def change_health(self, amount):
    self.health += amount
    if self.health < 0:
      self.health = 0
    elif self.health > 100:
      self.health = 100

  def die(self):
    self.health = 0

  # Move to a new address
  # TODO: This currently only checks for valid map directions.
  # It does not check for doors or barriers.
  def move_by(self, world, offset):
    new_address = Direction.offset(self.address, offset)
    if world.check_valid_address(new_address):
      self.address = new_address
    else:
      print("You can't go that way")

  # Execute a player command.  Currently that means moving.
  # return True/False depending on whether or not this was a valid command
  def do(self, world, command):
    # command is a 1-word string
    offset = Direction.get_offset(command)
    if offset != None:
      self.move_by(world, offset)
      return True
    if command == 'health':
      print('You are feeling {}% healthy'.format(self.get_health()))
      return True
    return False

  # Look for an item in the player's inventory by name.
  # If found, return the item.
  def get_in_inventory(self, item_name):
    for i in self.inventory:
      if i.get_name() == item_name:
        return i
    return None

  def put_in_inventory(self, item):
    if item != None:
      self.inventory.add(item)

  def remove_from_inventory(self, item):
    if item in self.inventory:
      self.inventory.remove(item)