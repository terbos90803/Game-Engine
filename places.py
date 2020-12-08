from core.place import Place
from core.thing import Thing
from objects import LimaBeans


# The Pantry has a hidden item, so it needs to be a special place.
# Special places are derived from Place
class Pantry(Place):
  def __init__(self):
    super().__init__(
      'the pantry',
      ['placeholder'])
    self.hidden_items = {LimaBeans()}
    self.dark_description = ['The pantry has many empty shelves, but some are too dark to see.']
    self.light_description = ['The pantry has many empty shelves, you can see them all with the flashlight.']

  def describe(self, player, force_describe=False):
    item = player.get_in_inventory('flashlight')
    is_on = item != None and item.get_state() == 'on'
    self.description = self.light_description if is_on else self.dark_description
    if is_on and len(self.hidden_items) > 0:
      self.contents.update(self.hidden_items)
      self.hidden_items = set()
    super().describe(player, force_describe)
