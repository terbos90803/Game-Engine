# Defines the player

from core.utils import print_list, same_word

class Player:
  def __init__(self, place, health=100, inventory=set()):
    self.place = place # Place : Where the player is now
    self.health = health # integer : percent healthy 0-100
    self.inventory = inventory # set of Thing
    self.playing = True

  def get_place(self):
    return self.place
    
  def get_health(self):
    return self.health

  def print_inventory(self):
    items = []
    for i in self.inventory:
      items.append(i.get_name())
    if len(items) == 0:
      items = ['nothing']
    print_list('You have: ', items)

  def is_playing(self):
    return self.playing and self.is_alive()

  def quit(self):
    self.playing = False

  def is_alive(self):
    return self.health > 0

  def change_health(self, amount):
    self.health += amount
    changed = 'increased' if amount > 0 else 'decreased'
    print(f'Your health {changed} by {abs(amount)} percent')
    if self.health <= 0:
      self.die()
    elif self.health > 100:
      self.health = 100

  def die(self):
    self.health = 0
    print('You died')

  # Execute a player command.  Currently that means moving.
  # return True/False depending on whether or not this was a valid command
  def do(self, verb):
    # Check to see if the verb is a passable Path
    connection = self.place.get_connection(verb)
    if connection != None:
      if connection[0].is_passable():
        self.place = connection[1]
      else:
        print(verb, 'is blocked.', connection[0].why_blocked())
      return True
    if same_word(verb, 'health'):
      print(f'You are feeling {self.get_health()}% healthy')
      return True
    return False

  # Look for an item in the player's inventory by name.
  # If found, return the item.
  def get_in_inventory(self, item_name):
    for i in self.inventory:
      if same_word(i.get_name(), item_name):
        return i
    return None

  def put_in_inventory(self, item):
    if item != None:
      self.inventory.add(item)

  def remove_from_inventory(self, item):
    if item in self.inventory:
      self.inventory.remove(item)

  def action(self):
    for i in self.inventory:
      i.action(self, True)