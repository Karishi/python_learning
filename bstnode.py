class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return 
        if self.val == val:
            return
        
        if self.val > val:
            if self.left is None:
                self.left = BSTNode(val)
            self.left.insert(val)
        if self.val < val:
            if self.right is None:
                self.right = BSTNode(val)
            self.right.insert(val)
    
    def get_min(self):
        if self.left:
            return self.left.get_min()
        return self.val

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.val