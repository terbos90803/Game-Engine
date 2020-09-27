# Direction enum

# Lists the four directions and specifies how each direction will change the address

from enum import Enum

class Direction(Enum):
  NORTH = (0, 1)
  EAST = (1, 0)
  SOUTH = (0, -1)
  WEST = (-1, 0)
  
  @staticmethod
  def get_offset(word):
    uword = word.upper()
    for d in Direction:
      if d.name == uword:
        return d.value
    return None

  @staticmethod
  def offset(address, offset):
    return (address[0] + offset[0], address[1] + offset[1])