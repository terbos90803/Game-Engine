# Define what a Thing is

class Thing:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.commands = {
      'examine': self.examine,
      'use': self.use
    }

  def get_name(self):
    return self.name
  
  def add_command(self, command):
    self.commands.add(command)

  def replace_command(self, command, method):
    self.commands[command] = method

  def examine(self, world, player, place, in_inventory):
    print(self.description)
    return True

  def use(self, world, player, place, in_inventory):
    print('nothing happens')
    return True

  def execute(self, verb, world, player, place, in_inventory):
    # print('command:', verb, self.name)
    if verb in self.commands:
      if self.commands[verb](world, player, place, in_inventory):
        return
    
    print("You can't {} the {}".format(verb, self.name))
