# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    sumFound = False
    process = [root]

    def recursiveBSTSearch(root, desired, sumFound):
        if root is None:
            return False
        
        print(root.val)
        if root.val < desired:
            sumFound = recursiveBSTSearch(root.right, desired, sumFound)
        elif root.val > desired:
            sumFound = recursiveBSTSearch(root.left, desired, sumFound)
        else:
            return True
        
        return sumFound

    while sumFound == False and len(process) > 0:
        node = process.pop(0)
        if node.left is not None:
            process.append(node.left)
        if node.right is not None:
            process.append(node.right)
        desired = k - node.val
        print(f"Desired is {desired}")
        if k is not 2 * node.val:
            sumFound = recursiveBSTSearch(root, desired, sumFound)
            print(sumFound)
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