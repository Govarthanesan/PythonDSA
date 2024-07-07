class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def AddFirst(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def AddLast(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=new_node

    def DeleteFirst(self):
        if self.head is None:
            print("List is Empty")
        self.head=self.head.next
    def DeleteLast(self):
        if self.head is None:
            print("List is Empty")
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def Count(self):
        if self.head is None:
            return 0
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def AddMiddle(self,data):
        if self.head is None:
            self.AddFirst(data)
        n=self.Count()
        new_node=Node(data)
        pos=(n//2)+1
        temp=self.head
        while pos-2:
            temp=temp.next
            pos-=1
        new_node.next=temp.next
        temp.next=new_node
    def DeleteMiddle(self):
        if self.head is None:
            print("List is Empty")
        n=self.Count()
        if n==1:
            self.DeleteFirst()

        pos=(n//2)+1
        temp=self.head
        while pos-2:
            temp=temp.next
            pos-=1
        temp.next=temp.next.next

    def Display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
l1=LinkedList()
l1.AddLast(10)
l1.AddLast(20)
l1.AddFirst(30)
l1.AddFirst(80)
l1.AddMiddle(50)
l1.DeleteMiddle()
# l1.AddFirst(90)
# l1.DeleteLast()
# l1.DeleteFirst()
print(l1.Count())
l1.Display()