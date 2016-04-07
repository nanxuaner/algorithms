# class Queue:
#     def __init__(self):
#         self.items = []
#     def add(self, item):
#         self.items.append(item)
#     def delete(self):
#         itemToDelet = self.items[0]
#         del self.items[0]
#         return itemToDelet
#     def size(self):
#         return len(self.items)
#     def report(self):
#         return self.items
#
# def testQueue():
#     myQueue = Queue()
#     myQueue.add(10)
#     myQueue.add(11)
#     myQueue.add(12)
#     myQueue.add(13)
#     print (myQueue.size())
#     print (myQueue.report())
#     print (myQueue.delete())
#     print (myQueue.report())
#     myQueue.delete()
#     myQueue.add(14)
#     print (myQueue.report())
#
#
# testQueue()
#
# class Queue:
#     def __init__(self):
#         self.items = []
#     def add(self, item):
#         self.items.append(item)
#     def delete(self):
#         return self.items.pop(0)
#     def size(self):
#         return len(self.items)
#     def report(self):
#         return self.items
#
# def testQueue():
#     myQueue = Queue()
#     myQueue.add(10)
#     myQueue.add(11)
#     myQueue.add(12)
#     myQueue.add(13)
#     print (myQueue.size())
#     print (myQueue.report())
#     print (myQueue.delete())
#     print (myQueue.report())
#     myQueue.delete()
#     myQueue.add(14)
#     print (myQueue.report())
#
#
# testQueue()

class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def delete(self):
        return self.items.pop(0)

    def report(self):
        return self.items

    def size(self):
        return len(self.items)

def testQueue():
    myQueue = Queue()
    myQueue.add(1)
    myQueue.add(2)
    myQueue.add(3)
    myQueue.add(4)

    print (myQueue.size())
    print (myQueue.report())
    print (myQueue.delete())
    print (myQueue.size())
    print (myQueue.report())

testQueue()

