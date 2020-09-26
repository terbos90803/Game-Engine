# Get input from the player and parse it


class Command:
    # Converts input to lower case, splits words into a list
    def __init__(self, world, player, prompt):
        self.world = world
        self.player = player

        raw_input = input(prompt)
        # Convert the input to lower case:
        smooth_input = raw_input.lower()
        # Convert the lower case input into a list:
        word_list = smooth_input.split()

        if len(word_list) > 0:
            self.verb = word_list[0]
        else:
            self.verb = None

        if len(word_list) > 1:
            self.noun = word_list[1]
        else:
            self.noun = None

    # library of game commands
    def quit(self):
        self.player.die()

    def help(self):
      print('Commands: quit, look, inventory, north, south, east, west, examine [thing]')

    def look(self):
        self.world.describe(self.player, True)

    def inventory(self):
      self.player.print_inventory()

    commands = {
      'quit': quit,
      'help': help,
      'look': look,
      'inventory': inventory
    }

    # Validate and execute the command
    def execute(self):
      if self.verb != None:
        # Check for game commands
        if self.verb in self.commands:
          self.commands[self.verb](self)
          return

        # Check to see if this is a player command
        if self.player.do(self.world, self.verb):
          return

        if self.noun != None:
          item = self.player.get_in_inventory(self.noun)
          if item != None:
            item.execute(self.verb)
            return
          place = self.world.get_current_place(self.player)
          item = place.get_item(self.noun)
          if item != None:
            item.execute(self.verb)
            return            

        print("You can't do that")
