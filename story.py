# All of the story wrapper bits
from core.utils import type_slow

def intro(player):
  type_slow([
    'You wake up itchy.', 
    'You have no idea how you got here.'],
    after_space=1)


def ending(player):
  type_slow([
    'Game Over', 
    'Thanks for playing!'])