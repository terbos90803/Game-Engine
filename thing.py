# Define what a Thing is

class Thing:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def get_name(self):
    return self.name
  
  def get_description(self):
    return self.description

  def add_command(self, command):
    self.commands.append(command)

  def examine(self, world, player, place):
    print(self.description)
    return True

  def take(self, world, player, place):
    place.take_item(self)
    player.put_in_inventory(self)
    return True
    
  def drop(self, world, player, place):
    place.put_item(self)
    player.remove_from_inventory(self)
    return True
    
  def use(self, world, player, place):
    pass

  commands = {
    'examine': examine,
    'use': use,
    'take': take,
    'drop': drop
  }

  def execute(self, world, player, place, verb):
    # print('command:', verb, self.name)
    if verb in self.commands:
      if self.commands[verb](self, world, player, place):
        return
    
    print("You can't {} the {}".format(verb, self.name))
