# classes for paths between Places

# A regular Path is always passable
class Path:

  def get_name(self):
    return 'path'

  def is_passable(self):
    return True


# A door can be open, closed, and locked
class Door(Path):
  def __init__(self, is_open=False, is_locked=False, key=None):
    self.is_open = is_open # Boolean : True when door is open
    self.is_locked = is_locked # Boolean : True when door is locked
    self.key = key # string : the correct key for this door

  def get_name(self):
    if self.is_locked:
      return 'locked door'
    elif self.is_open:
      return 'open door'
    else:
      return 'closed door'

  def is_passable(self):
    return self.is_open

  def open(self):
    if not self.is_locked:
      self.is_open = True
      print('Door opened')
    else:
      print('The door is locked')

  def close(self):
    self.is_open = False
    print('Door closed')

  def unlock(self, key):
    if self.key == key:
      self.is_locked = False
      print('Door unlocked')
    else:
      print('Wrong key')


# Connect two places together
# One Path will exist between two Places
# - direction player will leave first Place
# - first place
# - direction player will leave second Place
# - second place
# - Path connecting the Places
def connect(direction1, place1, direction2, place2, path):
  place1.add_connection(direction1, place2, path)
  place2.add_connection(direction2, place1, path)

