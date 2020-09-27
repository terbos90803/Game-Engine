# all the objects in the game

from thing import Thing


class Flashlight(Thing):
  def __init__(self):
    super().__init__('flashlight', 'an old flashlight')
    self.state = 'dead'

  on_use = {
    'dead': ('The flashlight is dead', 'dead'),
    'off': ('You turned the flashlight on', 'on'),
    'on': ('You turned the flashlight off', 'off')
  }

  def examine(self, word_list, world, player, place, in_inventory):
    print(self.description)
    print('The flashlight is', self.state)

  def use(self, word_list, world, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the flashlight")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]

  def combine(self, word_list, world, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'battery'})
    if other != None:
      self.new_battery()
      player.remove_from_inventory(other)

  def new_battery(self):
    print('You put a fresh battery in the flashlight')
    self.state = 'off'


class Battery(Thing):
  def __init__(self):
    super().__init__('battery', 'a new battery')
  
  def combine(self, word_list, world, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'flashlight'})
    if other != None:
      other.new_battery()
      player.remove_from_inventory(self)
