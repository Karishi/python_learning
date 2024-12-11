# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def branchDepth(root, node, depth):
        if root is None:
            return -1
        
        depth = 0
        while root is not None:
            if root.val == node.val:
                return depth
            elif root.val > node.val:
                root = root.right
            else:
                root = root.left
            depth += 1
        
        
    def isBalanced(self, tree, root):
        min_run = 2501
        max_run = 0
        
        for node in tree:
            if node.left is None and node.right is None:
                depth = branchDepth(root, node, depth)
                if depth < min_run:
                    min_run = depth
                if depth > max_run:
                    max_run = depth
                if max_run > min_run + 1:
                    return False
        return True
    
