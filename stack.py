# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         size = len(self.items)
#         return self.items.pop(size-1)
#
#     def report(self):
#         return self.items
#
#     def top(self):
#         size = len(self.items)
#         return self.items[size-1]
#
#     def size(self):
#         return len(self.items)
#
# def testStack():
#     myStack = Stack()
#     myStack.push(1)
#     myStack.push(2)
#     myStack.push(3)
#     myStack.push(4)
#     print (myStack.size())
#     print (myStack.report())
#     print (myStack.pop())
#     print (myStack.report())
#
# testStack()

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        size = len(self.items)
        return self.items.pop(size-1)

    def report(self):
        print self.items

    def top(self):
        size = len(self.items)
        print (self.items[size-1])

    def size(self):
        print (len(self.items))

def testStack():
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    myStack.top()
    myStack.size()
    myStack.report()
    myStack.pop()
    myStack.top()
    myStack.report()


testStack()