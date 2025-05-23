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

  # method to insert a new value into a bst
  def insert(self, val):
    if not self.root:
      self.root = Node(val)
    
    else:
      self._insert_recursive(self.root, val)
    
  # Helper method to recursively insert a value into a BST
  def _insert_recursive(self, node, val):
    if val < node.val:  # value is less than current node, we'll go left
      if not node.left:
        node.left = Node(val)
      else:
        self._insert_recursive(node.left, val)

    elif val > node.val:  # value is greater than current node, we'll go right
      if not node.right:
        node.right = Node(val)
      else:
        self._insert_recursive(node.right, val)

  # method to search for a value in a bst
  def search(self, val):
    return self._search_recursive(self.root, val)
  
  # Helper method to recursively search for a value in a bst and return the node if found
  def _search_recursive(self, node, val):
    # defining a base case
    if not node or node.val == val:
      return node

    if val < node.val:
      return self._search_recursive(node.left, val)
    
    elif val > node.val:
      return self._search_recursive(node.right, val)
      

# Example Usage. Creating an instance of a BST
bst = BST()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 