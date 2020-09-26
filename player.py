# Defines the player

from direction import Direction

class Player:
  def __init__(self, address=(0,0), health=100, inventory={}):
    self.address = address # Begin at the origin
    self.health = health # integer 0-100
    self.inventory = inventory # set of things

  def get_address(self):
    return self.address
    
  def get_health(self):
    return self.health

  def print_inventory(self):
    print(self.inventory)

  def is_alive(self):
    return self.health > 0

  def die(self):
    self.health = 0

  def move_by(self, world, offset):
    new_address = Direction.offset(self.address, offset)
    if world.check_valid_address(new_address):
      self.address = new_address
    else:
      print("You can't go that way")

  def do(self, world, command):
    # command is a 1-word string
    offset = Direction.get_offset(command)
    if offset != None:
      self.move_by(world, offset)
      return True
    return False

  def get_in_inventory(self, item_name):
    for i in self.inventory:
      if i.get_name() == item_name:
        return i
    return None