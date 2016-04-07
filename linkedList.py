# class Node:
#     def __init__(self, contents=None, next=None):
#         self.contents = contents
#         self.next = next
#
#     def getContents(self):
#         return self.contents
#
#     def __str__(self):
#         return str(self.contents)
#
# def printList(node):
#     while node:
#         print(node.getContents())
#         node = node.next
#         print()
#
# def testList():
#     node1 = Node("1")
#     node2 = Node("2")
#     node3 = Node("3")
#     node4 = Node("4")
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#
#     printList(node1)
#
# testList()

# class Node:
#     def __init__(self, contents=None, next=None):
#         self.contents = contents
#         self.next = next
#
#     def getContents(self):
#         return self.contents
#
#     def __str__(self):
#         return str(self.contents)
#
#     def deleteNode(self, node):
#         nodeTodelete = node.next
#         node.contents = node.next.contents
#         node.next = node.next.next
#
#         del nodeTodelete
#
# def search(node, value):
#     while node:
#         if node.getContents() == value:
#             print "found node %d" %(value)
#             return node
#         else:
#             node = node.next
#
#     print "not found node %d" %(value)
#     return None
#
# def printList(node):
#     while node:
#         print(node.getContents())
#         node = node.next
#         print("")
#
# def testList():
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#
#     printList(node1)
#
#     node1.deleteNode(node3)
#
#     printList(node1)
#
#     search(node1, 2)
#
#     search(node1, 10)
#
# testList()

# class Node():
#     def __init__(self, contents=None, next=None):
#         self.contents = contents
#         self.next = next
#
#     def getContents(self):
#         return self.contents
#
#     def __str__(self):
#         return str(self.contents)
#
# def printList(node):
#     while node:
#         print (node.getContents())
#         node = node.next
#         print ""
#     return None
#
# def deleteNode(node):
#     node_to_delete = node.next
#     node.contents = node.next.contents
#     node.next = node.next.next
#
#     del node_to_delete
#
# def search(node, value):
#     while node:
#         if node.getContents() == value:
#             print"found node %d" %(value)
#             return node
#         else:
#             node = node.next
#
#     print"node %d not exist" %(value)
#     return None
#
#
# def sortNode(node):
#     if not node:
#         return node
#
#     dummy = Node()
#     dummy.next = node
#     curr = node
#
#     while curr.next:
#         if curr.next.contents < curr.contents:
#             pre = dummy
#             while pre.next.contents < curr.next.contents:
#                 pre = pre.next
#             tmp = curr.next
#             curr.next = tmp.next
#             tmp.next = pre.next
#             pre.next = tmp
#         else:
#             curr = curr.next
#
#     return dummy.next
#
# def reverseList(node):
#     pre = None
#     curr = node
#
#     while curr:
#         tmp = curr.next
#         curr.next = pre
#         pre = curr
#         curr = tmp
#
#     return pre
#
# def detectCycle(node):
#     if not node:
#         return False
#
#     slow = node
#     fast = node
#
#     while fast.next and fast.next.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#
#     return False
#
# def testNode():
#     node1 = Node(2)
#     node2 = Node(1)
#     node3 = Node(5)
#     node4 = Node(3)
#     node5 = Node(2)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     printList(node1)
#     search(node1, 3)
#
#     deleteNode(node3)
#     printList(node1)
#
#     search(node1, 5)
#
#
#     node = sortNode(node1)
#     printList(node)
#
#
#     nodereverse = reverseList(node)
#     printList(nodereverse)
#
#     print detectCycle(nodereverse)
#
#
#
# testNode()

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val

    def __str__(self):
        return str(self.val)

def printList(node):
    while node:
        print (node.getVal())
        node = node.next
    return None

def deleteNode(node):
    node_to_delete = node.next

    node.val = node.next.val
    node.next = node.next.next

    del node_to_delete

def search(node, value):
    while node:
        if node.val == value:
            print ("Found node %s" %(value))
            return node
        else:
            node = node.next
    print ("Node not found")
    return None

def sortNode(node):
    if not node:
        return None

    dummy = Node()
    dummy.next = node
    curr = node

    while curr.next:
        if curr.next.val < curr.val:
            pre = dummy
            while pre.next.val < curr.next.val:
                pre = pre.next
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        else:
            curr = curr.next
    return dummy.next

def reverseList(node):
    pre = None
    curr = node

    while curr:
        tmp = curr.next
        curr.next = pre
        pre = curr
        curr = tmp
    return pre

def detectCycle(node):

    slow = node
    fast = node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow.getVal == fast.getVal:
            print ("Cycle in node")
            return node
    print ("Cycle not exist")
    return None


def testList():
    node1 = Node(1)
    node2 = Node(5)
    node3 = Node(3)
    node4 = Node(6)
    node5 = Node(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


    printList(node1)
    search(node1, 5)
    search(node1,10)
    node = sortNode(node1)
    printList(node)
    node_reverse = reverseList(node)
    printList(node_reverse)
    detectCycle(node_reverse)


testList()