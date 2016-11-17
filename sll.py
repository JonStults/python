# list = SinglyLinkedList()
# list.head = Node('Alice')
# list.head.next = Node('Chad')
# list.head.next.next = Node('Debra')

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
#
list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
#
# obj = ('Jon', 'Danny', 'Clevo', 'Todd', 'Miller', 'Phil')

# def node(val):
#     self.val = val
#     self.next = null
#
# def removeBack(object):
#     runner = self.head
#     if runner != null:
#         if runner.next == null:
#             self.head = null
#         else:
#             while runner.next != null:
#                 runner = runner.next
#                 runner = null
#
# print removeBack({'jon', 'sean', 'todd'})
