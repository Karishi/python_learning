# Task: Turn a list of ordered values into a balanced binary tree
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

Lis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def treeBuild(max_index, min_index = 0):
    if not TreeNode:
        return
    
    node_index = (min_index + max_index) // 2
    node = TreeNode(Lis[node_index])
    if min_index < node_index - 1:
        node.left = treeBuild(min_index, node_index - 1)
    if node_index + 1 < max_index:
        node.right = treeBuild(node_index + 1, max_index)
    return node
