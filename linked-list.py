# ---------------------------------------
# Singly linked List
#----------------------------------------

class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
    
    # Node Addition

    def addNodeToEnd(self, val):
        if not self.root:
            self.root = ListNode(val)
        else:
            itr = self.root
            while itr.next:
                itr = itr.next
            itr.next = ListNode(val)
    
    def addNodeToFront(self, val):
        newNode = ListNode(val)
        newNode.next = self.root
        self.root = newNode
    
    # Node Deletion

    def deleteNodeFromEnd(self):
        if not self.root:
            print("Empty List")
        if not self.root.next:
            self.root = None
        else:
            itr = self.root
            prev = None
            while itr.next:
                prev = itr
                itr = itr.next
            prev.next = None
        
    def deleteNodeFromFront(self):
        if not self.root:
            print("Empty List")
        else:
            self.root = self.root.next

    # Display
    def display(self):
        itr = self.root
        while itr:
            print(itr.val, "->", end=" ")
            itr = itr.next
        print()

# ---------------------------------------
# Driver Function
#----------------------------------------
def main():
    newList = LinkedList()
    newList.addNodeToFront(2)
    newList.addNodeToFront(1)
    newList.addNodeToFront(0)
    newList.addNodeToEnd(3)
    newList.addNodeToEnd(4)
    newList.deleteNodeFromEnd()
    newList.deleteNodeFromFront()
    newList.display()

if __name__ == '__main__':
    main()