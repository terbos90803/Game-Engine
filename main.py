# The game starts here.  This is the home of the main game loop.

from command import Command
from player import Player
import map

# Startup by initializing the world
player = Player(map.start);

# Display the introduction to the story
print('You wake up itchy.\nYou have no idea how you got here.\n')

# Loop until the end condition is met
while (player.is_alive()):
  # Describe the current place
  player.get_place().describe()

  # prompt for command
  command = Command(player, "> ")

  # execute command
  command.execute()

  # whitespace between turns
  print()

# game over
print('Game Over\nThanks for playing!')