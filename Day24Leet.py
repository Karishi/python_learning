# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def minDiffInBST(root):
    def getMinDifference(root, minD = 10**5):
        if root is None:
            return minD
        
        if root.left is not None and abs(root.val - root.left.val) < minD:
           minD = abs(root.val - root.left.val)
        if root.right is not None and abs(root.val - root.right.val) < minD:
           minD = abs(root.val - root.right.val)
        minD = getMinDifference(root.left, minD)
        minD = getMinDifference(root.right, minD)

        return minD
        
           
    minD = getMinDifference(root)
    return minD

root = TreeNode(5)
root.left = TreeNode(0)
root.right = TreeNode(48)
root.right.right = TreeNode(51)
root.right.left = TreeNode(12)

total = minDiffInBST(root)
print(f"The minimum difference in the BST is {total}")
    