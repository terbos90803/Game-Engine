# Define what a Thing is

class Thing:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.commands = {
      'examine': self.examine,
      'use': self.use,
      'combine': self.combine
    }

  def get_name(self):
    return self.name
  
  def add_command(self, command):
    self.commands.add(command)

  def replace_command(self, command, method):
    self.commands[command] = method

  def examine(self, word_list, world, player, place, in_inventory):
    print(self.description)

  def use(self, word_list, world, player, place, in_inventory):
    print('nothing happens')

  def combine(self, word_list, world, player, place, in_inventory):
    print('nothing happens')

  def execute(self, verb, word_list, world, player, place, in_inventory):
    # print('command:', verb, self.name)
    if verb in self.commands:
      self.commands[verb](word_list, world, player, place, in_inventory)
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

