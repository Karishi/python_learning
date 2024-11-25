# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def branchDepth(root, node, depth = 0):
        if root is None:
            return -1
        
        if root is node:
            return depth

        left_depth = branchDepth(root.left, node, depth +1)
        if left_depth != -1:
            return left_depth
        
        right_depth = branchDepth(root.right, node, depth +1)
        if right_depth != -1:
            return right_depth
        
    def isBalanced(self, root):
        min_run = 2501
        max_run = 0
        
        for node in root:
            depth = branchDepth(root, node, depth)
            if depth < min_run:
                min_run = depth
            if depth > max_run:
                max_run = depth
            if max_run > min_run + 1:
                return False
        return True
    
