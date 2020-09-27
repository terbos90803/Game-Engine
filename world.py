# Defines the world of the game.

from direction import Direction

# The World class knows about the map and how to do a few basic things with Places.

class World:
    def __init__(self, map):
        self.map = map

    def get_place_by_address(self, address):
        for p in self.map:
            if p.address == address:
                return p
        return None

    def check_valid_address(self, address):
        return self.get_place_by_address(address) != None

    def get_current_place(self, player):
        address = player.get_address()
        return self.get_place_by_address(address)

    def describe(self, player, do_describe=False):
        place = self.get_current_place(player)
        valid_directions = []
        for d in Direction:
          if self.check_valid_address(Direction.offset(place.get_address(), d.value)):
            valid_directions.append(d.name.lower())
        place.describe(valid_directions, do_describe)
