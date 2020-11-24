# Get input from the player and parse it

from path import Door
import utils


# A new command is created every time around the main loop

class Command:
    # Converts input to lower case, splits words into a list
    def __init__(self, player, prompt):
        self.player = player

        raw_input = input(prompt)
        # Convert the lower case input into a list:
        self.word_list = raw_input.split()

        # Are there any words at all?
        # The first word is always the verb
        if len(self.word_list) > 0:
            self.verb = self.word_list[0].lower()
        else:
            self.verb = None

        # Is there a second word?
        # The second word is always a noun
        if len(self.word_list) > 1:
            self.noun = self.word_list[1]
        else:
            self.noun = None


    # Library of game commands
    # These methods handle very high level or generic commands

    # Immediately quit the game
    def quit(self):
        self.player.quit()

    # Display the list of valid commands
    def help(self):
      utils.type_quick([
        'Basic Commands:', 
        ' - quit - end the game',
        ' - look - review the full description of the current place',
        ' - inventory - list what you are holding',
        ' - health - check your current health: 0-100%',
        ' - [direction] - any direction you can go from here, e.g. north, south, east, west',
        ' - examine [thing] - take a closer look at an object in this place or one you are holding',
        ' - take [thing] - if possible, pick up an object and put it in your inventory',
        ' - use [thing] - use a thing.  What happens depends on the thing.',
        ' - drop [thing] - remove a thing from your inventory and drop it here',
        ' - combine [thing1] [thing2] - if possible, combine two things together.  Sometimes, the order matters.  If thing1 thing2 doesn\'t work, try thing2 thing1.  You always have to be holding the first thing.',
        ' - open [thing/door] - open an unlocked thing or door',
        ' - close [thing/door] - close a thing or door',
        ' - unlock [thing/door] with [key] - unlock a locked thing or door using the correct key.  You must be holding the key.',
        '',
        'Some places or things have additional commands you can learn about.'],
        paragraph_space=0)

    # Display the full description of the current location even the player has been there before
    def look(self):
        self.player.get_place().describe(self.player, True)

    # List the items currently in the player's inventory
    def inventory(self):
      self.player.print_inventory()

    # If possible, move an item from the current location into the player's inventory
    def take(self):
      if self.noun != None:
        place = self.player.get_place()
        item = place.get_item(self.noun)
        if item != None:
          if item.is_takeable():
            place.remove_item(item)
            self.player.put_in_inventory(item)
            print('You picked up the', self.noun)
          else:
            print("You can't pick that up")
        else:
          print(f'There is no {self.noun} here')
      else:
        print('Name the thing to take')
      
    # If possible, move an item from the player's inventory to the current location
    def drop(self):
      if self.noun != None:
        place = self.player.get_place()
        item = self.player.get_in_inventory(self.noun)
        if item != None:
          self.player.remove_from_inventory(item)
          place.put_item(item)
          print('You dropped the', self.noun)
        else:
          print("You aren't carrying a", self.noun)
      else:
        print('Name the thing to drop')
    
    # Look for something to open and try to open it
    def open(self):
      if self.noun == None:
        print('What do you want to open?')
      else:
        connection = self.player.get_place().get_connection(self.noun)
        if connection != None:
          if connection[0].can_openclose():
            connection[0].open()
          else:
            print('You can\'t open', self.noun)
        else:
          print('Which way do you want to open?  Try "open [direction]"')

    # Look for something to close and try to close it
    def close(self):
      if self.noun == None:
        print('What do you want to close?')
      else:
        connection = self.player.get_place().get_connection(self.noun)
        if connection != None:
          if connection[0].can_openclose():
            connection[0].close()
          else:
            print('You can\'t close', self.noun)
        else:
          print('Which way do you want to close?  Try "close [direction]"')

    # Look for something to unlock and try to unlock it
    def unlock(self):
      if self.noun == None:
        print('What do you want to unlock?')
      else:
        if len(self.word_list) < 4:
          print(f'What do you want to unlock {self.noun} with?')
        else:
          keyname = self.word_list[3]
          key = self.player.get_in_inventory(keyname)
          if key != None:
            connection = self.player.get_place().get_connection(self.noun)
            if connection != None:
              if connection[0].can_unlock():
                connection[0].unlock(keyname)
              else:
                print('You can\'t unlock', self.noun)
            else:
              print('Which way do you want to unlock?  Try "unlock [direction] with [key]"')
          else:
            print('You don\'t have the', keyname)

    # Display helpful debugging information
    def track(self):
      place = self.player.get_place()
      print('Location:', place.get_name())
      print('Visited:', place.get_visited())
      place.print_contents()
      print('Health:', self.player.get_health())
      self.player.print_inventory()


    # Map between the names of valid commands and the methods that implement them
    commands = {
      'quit': quit,
      'help': help,
      'look': look,
      'inventory': inventory,
      'take': take,
      'drop': drop,
      'open': open,
      'close': close,
      'unlock': unlock,
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
        if self.player.do(self.verb):
          return

        # For 2-word commands, check for commands on the thing
        if self.noun != None:
          place = self.player.get_place()
          # check the player's inventory for the item first
          in_inventory = True
          item = self.player.get_in_inventory(self.noun)
          if item == None:
            # check the current location second
            in_inventory = False
            item = place.get_item(self.noun)
          if item != None:
            # found something, try the command on it
            item.execute(self.verb, self.word_list, self.player, place, in_inventory)
            return   
          print(f'There is no {self.noun} here')
          return

        print("You can't do that")
