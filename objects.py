# all the objects in the game

from thing import Thing

# If you just want to have a non-functional thing that only has a name and description,
# you can just create a Thing() in map.py.
# If you want a thing to have special behaviors, you need to create a class for it here.

# Use the example of Flashlight and Battery to see how to add behaviors.

# The Flashlight starts out dead.  It needs a new battery.
# The Flashlight needs to know if it is dead, off, or on.  This is called 'state'.
class Flashlight(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('flashlight', 'an old flashlight')
    self.state = 'dead' # start out dead

  # What happens when we 'use' the Flashlight depends on its state.
  # This dictionary lists what to print and the new state.
  # Examples:
  #  - If you use a dead Flashlight, it stays dead
  #  - If you use a good Flashlight, it will toggle on and off
  on_use = {
    'dead': ('The flashlight is dead', 'dead'),
    'off': ('You turned the flashlight on', 'on'),
    'on': ('You turned the flashlight off', 'off')
  }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, world, player, place, in_inventory):
    print(self.description)
    print('The flashlight is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, world, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the flashlight")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]

  # When we combine the Flashlight with something else, make sure that's a legal action.
  # The only thing we can combine the Flashlight with is the battery.
  # If the other thing is the battery, then make the Flashlight work and hide the battery.
  def combine(self, word_list, world, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'battery'})
    if other != None:
      self.new_battery()
      player.remove_from_inventory(other)

  # When putting a battery in the Flashlight, it starts off.
  # This is most important when changing a dead Flashlight into a working one.
  def new_battery(self):
    print('You put a fresh battery in the flashlight')
    self.state = 'off'


# A Battery is a mostly non-functional object.
# We could have gotten away with just a plain thing named 'battery',
# but we want to allow combining with the Flashlight even if the battery is listed first.
# We want both of these things to work:
# - combine flashlight battery
# - combine battery flashlight
class Battery(Thing):
  def __init__(self):
    super().__init__('battery', 'a new battery')
  
  # This combine is very much like the one in Flashlight, but self and other are swapped
  def combine(self, word_list, world, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'flashlight'})
    if other != None:
      other.new_battery()
      player.remove_from_inventory(self)
