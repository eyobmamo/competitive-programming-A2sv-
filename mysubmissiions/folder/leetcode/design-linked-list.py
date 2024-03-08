class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def iterse(self):
        l1=[]
        current = self.head
        while current:
            l1.append(current.data)
            current = current.next
        return l1    


    def get(self, index: int) -> int:
        if index<0 or not self.head:
            return -1
        print(self.iterse())
        current = self.head
        position = 0
        print(str(current))
        if position == index  :
            return current.data
        else:
            while (current and position != index):
                print(current.data)
                current = current.next
                position = position + 1
            if current != None:
                return current.data
            else:
                return -1 

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new    
        

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new        
    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        current = self.head
        position = 0
        if position == index :
            if current:
                new.next=self.head
                self.head = new
            else:
                self.head=new    
        else:
            while ( current  and position + 1 != index):
                current = current.next
                position = position +1
            if current != None:
                new.next = current.next
                current.next = new        

    def deleteAtIndex(self, index: int) -> None:

        if self.head == None or index <0:
            return 
        current = self.head
        position = 0
        if position == index:
            if self.head.next:
                self.head = self.head.next
                return
            else:
                self.head=None    
        else:
            while(current.next  and position + 1 != index):
                current = current.next
                position = position + 1
            if current.next and current.next.next: 
                current.next = current.next.next 
            elif not current.next:
                return        
            else:
                current.next=None
                         
                
                
                 

                
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)