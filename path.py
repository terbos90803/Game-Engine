# classes for paths between Places

# A regular Path is always passable
class Path:
  def __init__(self, place):
    self.place = place # Place : where this path leads

  def is_passable(self):
    return True


# A door can be open, closed, and locked
class Door(Path):
  def __init__(self, place, open=False, locked=False, key=None):
    super().__init__(place)
    self.open = open # Boolean : True when door is open
    self.locked = locked # Boolean : True when door is locked
    self.key = key # string : the correct key for this door

  def is_passable(self):
    return self.open

  def open(self):
    if not self.locked:
      self.open = True

  def close(self):
    self.open = False

  def unlock(self, key):
    if self.key == key:
      self.locked = False
      print('Door unlocked')
    else:
      print('Wrong key')
