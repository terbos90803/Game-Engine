# Define what a Thing is

# This is the Thing base class.  It's useful for non-functional things.
# If a specific thing has behaviors, derive from this class and put the behaviors there.
# Examples of deriving functional things can be found in objects.py

# The implementations of examine, use, and combine you'll find here don't do much.
# That's ok.  Don't change them here.
# If you need to change the behavior of a thing, override the examine, use, and/or combine
# methods in your derived class.
# Look at the examples in objects.py to see how to do this.

class Thing:
  def __init__(self, name, description, can_take):
    self.name = name # string : one word name
    self.description = description # string : full description
    self.can_take = can_take # Boolean : thing can be picked up
    self.commands = {
      'examine': self.examine,
      'use': self.use,
      'combine': self.combine
    }

  def get_name(self):
    return self.name

  def is_takeable(self):
    return self.can_take
  
  def add_command(self, command, method):
    self.commands[command] = method

  def examine(self, word_list, player, place, in_inventory):
    print(self.description)

  def use(self, word_list, player, place, in_inventory):
    print('nothing happens')

  def combine(self, word_list, player, place, in_inventory):
    print('nothing happens')

  def execute(self, verb, word_list, player, place, in_inventory):
    # print('command:', verb, self.name)
    if verb in self.commands:
      self.commands[verb](word_list, player, place, in_inventory)
    else:
      print("You can't {} the {}".format(verb, self.name))

  def combine_things(self, word_list, player, in_inventory, valid_others):
    if not in_inventory:
      print("You're not holding the", self.get_name())
    elif len(word_list) < 3:
      print('Combine the {} with what?'.format(self.get_name()))
    else:
      othername = word_list[2]
      other = player.get_in_inventory(othername)
      if other == None:
        print("You're not holding the", othername)
      elif other.get_name() in valid_others:
        return other
    return None

