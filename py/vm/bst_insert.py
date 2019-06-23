from Queue import *

class tnode(object):
  def __init__(self, data=None):
    self.left=None
    self.right=None
    self.data=data

class bst:
  def __init__(self):
    self.root=None

  def insert(self, data):
    self.root, count=self.insertNode(self.root, data, 0)
    print "inserting "+str(data)+" takes: "+str(count)+" steps!"

  def insertNode(self, node, data, count):
    count=0
    if not node:
      node=tnode(data=data)
    elif data<=node.data:
      node.left, count=self.insertNode(node.left, data, count)
    else:
      node.right, count=self.insertNode(node.right, data, count)
    return node, (count+1)

  def __str__(self):
    if not self.root:
      return "empty tree"
    tree_str=""
    stack=Queue()
    stack.put(self.root)
    tmp=Queue()
    while(True):
      node=stack.get()
      tree_str+=str(node.data)+"\t"
      if node.left:
        tmp.put(node.left)
      if node.right:
        tmp.put(node.right)
      if stack.empty() and tmp.empty():
        break
      elif stack.empty():
        del stack
        stack=tmp
        tmp=Queue()
        tree_str+="\n"
    return tree_str


def main():
  test=bst()
  test.insert(3)
  test.insert(5)
  test.insert(1)
  test.insert(2)
  test.insert(0)
  test.insert(8)
  test.insert(4)
  print test
  test.insert(4)
  test.insert(4)
  test.insert(5)

main()