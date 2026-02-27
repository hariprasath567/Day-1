# Linked list

# advantages
# 1) stored in memory
# 2)fast acces by index
# 3) myst traverse strp by step
# 4)flexible size

# BASIC STRUCTURE
# data and address of the next node

# [10|next] - > [20|next] - > [30|None]

# step by step logic
# create a class node
# store data
# store reference to next node


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n1.next=n2
# n2.next=n3
# print(n1.data)
# print(n2.data)
# print(n3.data)
# print(n1.next.data)

# create linked list class
# create head pointer 
# head stores first node

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insert_begin(self,data):
#         newNode=Node(data)
#         newNode.next=self.head
#         self.head=newNode
#     def insert_end(self,data):
#         endnewNode=Node(data)
#         if self.head is None:
#             self.head=endnewNode
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=endnewNode
#     def insert_pos(self,pos,data):
#         newNode=Node(data)
#         if pos==1:
#             newNode.next=self.head
#             self.head=newNode
#             return
#         temp=self.head
#         for i in range(pos-2):
#             temp=temp.next
#         newNode.next=temp.next
#         temp.next=newNode

#     def display (self):
#         temp=self.head
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# li=LinkedList()
# li.insert_begin(10)
# li.insert_begin(5)
# li.insert_begin(20)
# li.insert_begin(30)
# li.insert_begin(40)
# li.insert_end(50)
# li.insert_end(40)
# li.insert_begin(92)
# li.display()

# for _ in range(8):
#     print("helo")