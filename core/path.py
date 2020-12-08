# classes for paths between Places

# A regular Path is always passable
class Path:
  def __init__(self, name='path'):
    self.name = name

  def get_name(self):
    return self.name

  def is_passable(self):
    return True

  def why_blocked(self):
    return 'not blocked'

  def can_openclose(self):
    return False

  def can_unlock(self):
    return False


# A door can be open, closed, and locked
class Door(Path):
  def __init__(self, name='door', is_open=False, is_locked=False, key=None):
    super().__init__(name)
    self.is_open = is_open # Boolean : True when door is open
    self.is_locked = is_locked # Boolean : True when door is locked
    self.key = key # string : the correct key for this door

  def get_name(self):
    if self.is_locked:
      return f'locked {self.name}'
    elif self.is_open:
      return f'open {self.name}'
    else:
      return f'closed {self.name}'

  def is_passable(self):
    return self.is_open

  def why_blocked(self):
    if self.is_locked:
      return f'The {self.name} is locked. Use the {self.key} to unlock it.'
    elif self.is_open:
      return f'The {self.name} is open.'
    else:
      return f'The {self.name} is closed. Open it first.'

  def can_openclose(self):
    return True

  def can_unlock(self):
    return True
    
  def open(self):
    if not self.is_locked:
      self.is_open = True
      print(f'{self.name} opened')
    else:
      print(self.why_blocked())

  def close(self):
    self.is_open = False
    print(f'{self.name} closed')

  def unlock(self, key):
    if self.key == key:
      self.is_locked = False
      print(f'{self.name} unlocked')
    else:
      print('Wrong key')


# Connect two places together
# One Path will exist between two Places
# - first place
# - direction player will leave first Place
# - Path connecting the Places
# - direction player will leave second Place
# - second place
def connect(place1, direction1, path, direction2, place2):
  place1.add_connection(direction1, place2, path)
  place2.add_connection(direction2, place1, path)

