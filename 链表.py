from math import trunc


class node:
    def __init__(self,key = None):
        self.key = key
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node(None)
    
    def append(self,key):
        new_node = node(key)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node#在python中不用指针，
        #直接把node赋值给next就行，直接赋值，不用传地址
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.key)
        print(elems)
    def get(self,index):
        if index>=self.length() and index<0:
            print("error")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node
            cur_idx+=1
    def erase(self,index):
        if index>=self.length() and index<0:
            print("error")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
    def __getitem__(self,index):
        return self.get(index)
    
    def insert(self,index,key):
        if index>=self.length() and index<0:
            return self.append(key)
        cur_index = 0
        cur_node = self.head
        last_node = self.head
        while True:
            last_node =cur_node 
            cur_node = cur_node.next
            if cur_index == index:
                new_node = node(key)
                last_node.next = new_node
                new_node.next = cur_node
                return
            cur_index+=1
    def insert_node(self,index,node):
        if index<0:
            print("error")
        if index>=self.length():
            cur_node=self.head
            while cur_node.next!=None:
                cur_node=cur_node.next
            cur_node.next=node
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node =cur_node 
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = node
                node.next = cur_node
                return
            cur_index+=1
    def set(self,index,key):
        if index>=self.length() or index<0:
            print("ERROR: 'Set' Index out of range!")
            return
        cur_node = self.head
        cur_index = 0
        while True:
            cur_node = cur_index
            if cur_index == index:
                cur_node.key = key
                return
            cur_index+=1

ll = linked_list()
ll.display()
ll.append(8)
ll.display()
ll.insert(1,7)
ll.display()
ll.length()
ll.insert(2,9)
ll.insert(2,18)
ll.display()
print(ll.length())