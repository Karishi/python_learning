# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    sumFound = False
    startPoint = root
    process = [root]
    while not sumFound and len(process) > 0:
        node = process.pop(0)
        if node.left is not None:
            process.append(node.left)
        if node.right is not None:
            process.append(node.right)
        desired = k - node.val
        if desired != node.val:
            root = startPoint
            while not sumFound:
                if root.val == desired:
                    sumFound = True
                elif root.val < desired:
                    if root.left is not None:
                        root = root.left
                elif root.val > desired:
                    if root.right is not None:
                        root = root.right
                else:
                    break
    return sumFound
        

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)

if findTarget(root, 7):
    print("7 is in there!")
else:
    print("I did it wrong!")