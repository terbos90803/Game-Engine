# The game starts here.  This is the home of the main game loop.

from command import Command
from player import Player
import map
import story

# Startup by initializing the world
player = Player(map.start)

# Display the introduction to the story
story.intro(player)

# Loop until the end condition is met
while (player.is_playing()):
  # Describe the current place and do any place action
  place = player.get_place()
  place.describe(player)
  place.action(player)
  player.action()

  # prompt for command
  command = Command(player, "> ")

  # execute command
  try:
    command.execute()
  except:
    print('Something went wrong')
    raise # re-raise the exception for debugging

  # whitespace between turns
  print()

# game over
story.ending(player)
