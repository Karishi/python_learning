# Assignment: Find the value of the node farthest left that is at the
# maximum depth for the tree.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def findBottomLeftValue(root):
    startValue = root.val

    def getDepth(node, winningVal, maxD = 0, depth = 0):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            if depth > maxD:
                maxD = depth
                winningVal = node.val
        else:
            winningVal, maxD = getDepth(node.left, winningVal, maxD, depth + 1)
            winningVal, maxD = getDepth(node.right, winningVal, maxD, depth + 1)
            
        return winningVal, maxD
    
    winningVal, maxD = getDepth(root, startValue)

    return winningVal, maxD
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
val, dep = findBottomLeftValue(root)
print(f"Value {val} is leftmost at a depth of {dep}")