# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def hasPathSum(root, targetSum):
    def checkPath(node, targetSum, hasSum = False, currentVal = 0, lastNodeVal = 0):
        if not node or hasSum:
            if not hasSum:
                currentVal -= lastNodeVal
            return hasSum
        
        if not node.left and not node.right:
           print(f"The leaf value is {currentVal+node.val}")
           if currentVal + node.val == targetSum:
              hasSum = True
              return hasSum
           
        hasSum = checkPath(node.left, targetSum, hasSum, currentVal+node.val, node.val)
        hasSum = checkPath(node.right, targetSum, hasSum, currentVal+node.val, node.val)
        
        return hasSum
    
    return checkPath(root, targetSum)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

targetSum = 9
print(f"HasPathSum returns {hasPathSum(root, targetSum)} for the value {targetSum}.")