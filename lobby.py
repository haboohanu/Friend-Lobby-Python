class Person():
  def __init__(self, n):
    self.name = n
    self.friends = []
    self.distance = 9999
    self.color = 'black'
    self.status = 'offline'

  def add_friend(self, p):
    if p not in self.friends:
      self.friends.append(p)
      self.friends.sort(key=lambda x: x.name)

  def trigger_status(self):
    if self.status == 'offline':
      self.status = 'online'
    elif self.status == 'online':
      self.status = 'offline'
    
  def print_friends(self):
    for i in self.friends:
      print(i.name)
  
  def __str__(self):
    return str(self.name)

  def __repr__(self):
    return str(self.name)






class Graph:
  def __init__(self):
    self.group = {}

  def add_person(self, p):
    if isinstance(p,Person) and p.name not in self.group:
      self.group[p.name] = p

  def add_connection(self, p1, p2):
    if p1.name and p2.name in self.group:
      self.group[p1.name].add_friend(p2)
      self.group[p2.name].add_friend(p1)


  def print_graph(self):
    for key, value in self.group.items():
      print(key , value.friends , value.distance)

  def bfs(self, person):
    queue = []
    person.distance = 0
    person.color = 'red'
    for friend in person.friends:
      friend.distance = person.distance + 1
      queue.append(friend)

    while queue:
      current_person = queue.pop(0)
      current_person.color = 'red'

      for friend in current_person.friends:
        if friend.color == 'black':
          queue.append(friend)
          if friend.distance > current_person.distance + 1:
            friend.distance = current_person.distance + 1

  def get_online_friends(self, person):
    online_friends = []
    for friend in person.friends:
      print(friend.status)
      if friend.status == 'online':
        online_friends.append(friend)
    print(online_friends)

  def get_offline_friends(self, person):
    online_friends = []
    for friend in person.friends:
      print(friend.status)
      if friend.status == 'online':
        online_friends.append(friend)
    print(online_friends)

  def change_status(self, person):
    person.trigger_status()

  
      
    



p1 = Person("Jimmy")
p2 = Person("Sabrina")
p3 = Person("Kirran")
    

g = Graph()
g.add_person(p1)
g.add_person(p2)
g.change_status(p2)
g.add_person(p3)
g.add_connection(p1,p2)
g.add_connection(p2,p3)
g.bfs(p1)
g.print_graph()
g.get_online_friends(p1)
