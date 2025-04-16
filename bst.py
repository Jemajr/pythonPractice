# binary search tree class, creating TreeNode class as well for the nodes themselves

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)


class BST:
  def __init__(self):
    self.root = None

  def insert(self, val):
    if not self.root:
      self.root = Node(val)
    
    else:
      self.recursivelyInsert(self.root, val)
    
  def recursivelyInsert(self, node, val):
    ...