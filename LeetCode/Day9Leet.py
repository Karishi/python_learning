# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def maxDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    
    def getDepth(node, maxD, depth = 0):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            if depth > maxD:
                maxD = depth
        else:
            maxD = getDepth(node.left, maxD, depth + 1)
            maxD = getDepth(node.right, maxD, depth + 1)
            
        return maxD

    return getDepth(root, 0)
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(maxDepth(root))