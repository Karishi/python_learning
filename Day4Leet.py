class MyStack(object):

    def __init__(self):
        self.obj = []

    def push(self, x: int):
        self.obj.append(x)
        return None
        

    def pop(self):
        item = self.obj.pop(-1)
        return item

    def top(self):
        item = self.obj[-1]
        return item

    def empty(self):
        if len(self.obj) == 0:
            return True
        else:
            return False

obj = MyStack()
obj.push(9)
obj.push(8)
param_2 = obj.pop()
print(f"{param_2} was the top of the stack")
param_3 = obj.top()
print(f"{param_3} still is top of stack.")
param_4 = obj.empty()
if param_4:
    print("The list is empty.")
else:
    print("The list is not empty.")

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()