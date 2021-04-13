"""

Uses separate chaining with a node based linked list to handle hash collisions.
Note the function name '.insert' used on linked lists instead of '.insert_beginning'.
Note the use of blossom_lib, which is a list of the form [["flower0", "flower0 definition"], ...]

"""

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
  
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    payload = Node([key, value])
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_array = self.array[array_index]
    
    for node in list_at_array:
      if node[0] == key:
        node[1] = value
    list_at_array.insert(payload)
  
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]

    for node in list_at_index:
      if node[0] == key:
        return node[1]
    return

    if payload is None:
      return
    
    if payload[0] != key:
      return

    return payload[1]

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('rose'))
print(blossom.retrieve('tulip'))
print(blossom.retrieve('iris'))

for flower in flower_definitions:
  print(flower[0] + "," + flower[1] + "," + blossom.retrieve(flower[0]) )