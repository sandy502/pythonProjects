# implement stack using a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False    

    def printll(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return

    # for push operation
    def push(self, new_data): 
        if self.head == None:
            self.head=Node(new_data)
             
        else:
            newnode = Node(new_data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
             
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
         
        if self.isempty():
            return None             
        else:
            return self.head.data   

if __name__ == "__main__":
    llist = Stack()
    llist.push(1)
    llist.push(5)
    llist.push(7)
    llist.push(2)
    llist.push(4)
    llist.push(6)   
    llist.printll()
    print("\n")
    llist.pop()  
    llist.pop()
    llist.printll()
    print("\n")
    print(llist.peek())               
