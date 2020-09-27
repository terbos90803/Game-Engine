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

  def examine(self, world, player, place, in_inventory):
    print(self.description)
    print('The flashlight is', self.state)
    return True

  def use(self, world, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the flashlight")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]
    return True
