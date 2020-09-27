# Defines the class of places

class Place:
  def __init__(self, name, address, description, contents):
    self.name = name # string
    self.address = address # tuple
    self.description = description # string
    self.contents = contents # set of things
    self.visited = False

  def get_name(self):
    return self.name

  def get_address(self):
    return self.address

  def get_description(self):
    return self.description

  def get_contents(self):
    return self.contents

  def contains(self, item):
    return item in self.contents

  def describe(self, valid_directions, do_describe):
    print('You are in', self.name)
    if do_describe or not self.visited:
      print(self.description)
      if len(self.contents) > 0:
        items = []
        for i in self.contents:
          items.append(i.get_name())
        print('You see:', *items)
      print('You can go:', *valid_directions)
      self.visited = True

  def get_item(self, item_name):
    for i in self.contents:
      if i.get_name() == item_name:
        return i;
    return None

  def take_item(self, item):
    if item in self.contents:
      self.contents.remove(item)

  def put_item(self, item):
    if item != None:
      self.contents.add(item)