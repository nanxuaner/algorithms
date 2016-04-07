# class BinaryTreeNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#
#     def getLeftChild(self):
#         return self.left
#
#     def getRightChild(self):
#         return self.right
#
#     def setNodeValue(self, value):
#         self.value = value
#
#     def getNodeValue(self):
#         return self.value
#
#     def insertRight(self, newValue):
#         if self.right == None:
#             self.right = BinaryTreeNode(newValue)
#         else:
#             node = BinaryTreeNode(newValue)
#             node.right = self.right
#             self.right = node
#
#     def insertLeft(self, newValue):
#         if self.left == None:
#             self.left = BinaryTreeNode(newValue)
#         else:
#             node = BinaryTreeNode(newValue)
#             node.left = self.left
#             self.left = node
# #recursion
# def printTree(root):
#
#     if root != None:
#         printTree(root.getLeftChild())
#         print(root.getNodeValue())
#         printTree(root.getRightChild())
#
#
# def testTree():
#     myTree = BinaryTreeNode(1)
#     myTree.insertLeft(2)
#     myTree.insertRight(3)
#     myTree.insertRight(4)
#     printTree(myTree)
#
# testTree()

# class BinaryTreeNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#
#     def getLeftChild(self):
#         return self.left
#
#     def getRightChild(self):
#         return self.right
#
#     def setNodeValue(self, value):
#         self.value = value
#
#     def getNodeValue(self):
#         return self.value
#
#     def insertRight(self, newNode):
#         if self.right == None:
#             self.right = BinaryTreeNode(newNode)
#         else:
#             node = BinaryTreeNode(newNode)
#             node.right = self.right
#             self.right = node
#
#     def insertLeft(self, newNode):
#         if self.left == None:
#             self.left = BinaryTreeNode(newNode)
#         else:
#             node = BinaryTreeNode(newNode)
#             node.left = self.left
#             self.left = node
#
# def printTree(root):
#     if root != None:
#         printTree(root.getLeftChild())
#         print(root.getNodeValue())
#         printTree(root.getRightChild())
#
#
# def testTree():
#     myTree = BinaryTreeNode(1)
#     myTree.insertLeft(2)
#     myTree.insertRight(3)
#     myTree.insertRight(4)
#     myTree.insertLeft(5)
#     myTree.setNodeValue(10)
#     printTree(myTree)
#
# testTree()

# class BinaryTreeNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#
#     def getRightChild(self):
#         return self.right
#
#     def getLeftChild(self):
#         return self.left
#
#     def setNodeValue(self, value):
#         self.value = value
#
#     def getNodeValue(self):
#         return self.value
#
#     def insertRight(self, newValue):
#         if self.right == None:
#             self.right = BinaryTreeNode(newValue)
#         else:
#             node = BinaryTreeNode(newValue)
#             node.right = self.right
#             self.right = node
#
#     def insertLeft(self, newValue):
#         if self.left == None:
#             self.left = BinaryTreeNode(newValue)
#         else:
#             node = BinaryTreeNode(newValue)
#             node.left = self.left
#             self.left = node
#
# def printTree(root):
#     if root != None:
#         printTree(root.getLeftChild())
#         print (root.getNodeValue())
#         printTree(root.getRightChild())
#
# def testTree():
#     myTree = BinaryTreeNode(1)
#     myTree.insertLeft(2)
#     myTree.insertRight(1)
#     myTree.insertRight(3)
#     myTree.insertLeft(10)
#     printTree(myTree)
#     myTree.insertLeft(11)
#     printTree(myTree)
#     myTree.setNodeValue(20)
#     printTree(myTree)
#
# testTree()

class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setNodeValue(self, value):
        self.value = value

    def getNodeValue(self):
        return self.value

    def insertRight(self, newValue):
        if self.right == None:
            self.right = BinaryTreeNode(newValue)
        else:
            node = BinaryTreeNode(newValue)
            node.right = self.right
            self.right = node

    def insertLeft(self, newValue):
        if self.left == None:
            self.left = BinaryTreeNode(newValue)
        else:
            node = BinaryTreeNode(newValue)
            node.left = self.left
            self.left = node


def printTreeInOrder(root):
    if root != None:
        printTreeInOrder(root.getLeftChild())
        print(root.getNodeValue())
        printTreeInOrder(root.getRightChild())

def printTreePreOrder(root):
    if root != None:
        print (root.getNodeValue())
        printTreePreOrder(root.getLeftChild())
        printTreePreOrder(root.getRightChild())

def printTreePostOrder(root):
    if root != None:
        printTreePostOrder(root.getLeftChild())
        printTreePostOrder(root.getRightChild())
        print (root.getNodeValue())

def testTree():
    myTree = BinaryTreeNode(1)
    myTree.insertLeft(2)
    myTree.insertLeft(3)
    myTree.insertRight(4)
    myTree.insertRight(5)
    myTree.insertRight(6)
    printTreeInOrder(myTree)
    print ()
    printTreePreOrder(myTree)
    print ()
    printTreePostOrder(myTree)

testTree()

#how to insert node in subtree