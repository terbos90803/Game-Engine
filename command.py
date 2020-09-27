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
        self.word_list = smooth_input.split()

        if len(self.word_list) > 0:
            self.verb = self.word_list[0]
        else:
            self.verb = None

        if len(self.word_list) > 1:
            self.noun = self.word_list[1]
        else:
            self.noun = None

    # library of game commands
    def quit(self):
        self.player.die()

    def help(self):
      print('Commands: quit, look, inventory, north, south, east, west, examine [thing], take [thing], use [thing], drop [thing]')

    def look(self):
        self.world.describe(self.player, True)

    def inventory(self):
      self.player.print_inventory()

    def take(self):
      if self.noun != None:
        place = self.world.get_current_place(self.player)
        item = place.get_item(self.noun)
        if item != None:
          place.take_item(item)
          self.player.put_in_inventory(item)
          print('You picked up the', self.noun)
        else:
          print('There is no {} here'.format(self.noun))
      else:
        print('Name the thing to take')
      
    def drop(self):
      if self.noun != None:
        place = self.world.get_current_place(self.player)
        item = self.player.get_in_inventory(self.noun)
        if item != None:
          self.player.remove_from_inventory(item)
          place.put_item(item)
          print('You dropped the', self.noun)
        else:
          print("You aren't carrying a", self.noun)
      else:
        print('Name the thing to drop')
    
    # Needs visited, secrets, etc
    # How do i get contents?
    def track(self):
      location = self.player.get_address()
      print('Location: ', location)
      #print('Contains: ', self.map.contents)
      print('Health: ', self.player.health)
      # Need to display items
      print('Inventory: ', self.player.inventory)


    commands = {
      'quit': quit,
      'help': help,
      'look': look,
      'inventory': inventory,
      'take': take,
      'drop': drop,
      'track' : track,
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

        # For 2-word commands, check for custom commands on the thing
        if self.noun != None:
          place = self.world.get_current_place(self.player)
          # check the player's inventory for the item first
          in_inventory = True
          item = self.player.get_in_inventory(self.noun)
          if item == None:
            # check the current location second
            in_inventory = False
            item = place.get_item(self.noun)
          if item != None:
            # found something, try the command on it
            item.execute(self.verb, self.world, self.player, place, in_inventory)
            return   
          print('There is no {} here'.format(self.noun))
          return

        print("You can't do that")
