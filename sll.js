list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

// something close to this should be utilized for all of the above problems
runner = list.head
while(runner.next != null){
 console.log(runner.val)
}
