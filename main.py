# The game starts here.  This is the home of the main game loop.

from command import Command
from player import Player
import map
import utils

# Startup by initializing the world
player = Player(map.start);

# Display the introduction to the story
utils.type_slow(['You wake up itchy.', 'You have no idea how you got here.'])
print()

# Loop until the end condition is met
while (player.is_alive()):
  # Describe the current place
  player.get_place().describe()

  # prompt for command
  command = Command(player, "> ")

  # execute command
  try:
    command.execute()
  except:
    print('Something went wrong')
    # raise # re-raise the exception for debugging

  # whitespace between turns
  print()

# game over
utils.type_slow(['Game Over', 'Thanks for playing!'])