# The game map

from place import Place
from thing import Thing

# Thing(name, description)
# Place(name, address, description, contents = {})

map = {
  Place('the barn', (0,0), 'The old barn is full of hay and the smell of animals', {Thing('flashlight', 'an old flashlight')}),
  Place('the yard', (-1,0), 'The yard between the barn and the house is overgrown with weeds'),
  Place('the house', (-2,0), 'The abandonded house is falling apart at the seams')
}