# The game starts here.  This is the home of the main game loop.

from world import World
from command import Command
from player import Player
from map import map

# Startup by initializing the world
world = World(map);
player = Player();

# Loop until the end condition is met
while (player.is_alive()):
  # Describe the current place
  world.describe(player)

  # prompt for command
  command = Command(world, player, "> ")

  # execute command
  command.execute()

  # whitespace
  print()

# game over
print('Thanks for playing!')