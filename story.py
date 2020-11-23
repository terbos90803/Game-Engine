# All of the story wrapper bits
import utils

def display_intro(player):
  utils.type_slow([
    'You wake up itchy.', 
    'You have no idea how you got here.'],
    after_space=1)


def display_ending(player):
  utils.type_slow([
    'Game Over', 
    'Thanks for playing!'])