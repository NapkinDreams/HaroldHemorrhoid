def get_user(name):
  for name in Path("/path/folder/directory").glob("*.json"):
    f = open(txt_path)
    user = json.load(f)
    user_selection.append(user)

class User(Character):
  def __init__(self, name, password):
    super().__init__()
    self.name = name
    self.password = password
    self.data = data