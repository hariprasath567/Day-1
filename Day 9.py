#Priority Queue

#removes element based on the priority ijnsead of order

#Higer priority removed first
#not normal FIFO
#smaller number = higher priority

#task-->1
#task-->2
#task-->3

# real-time eg:
# hospital emergerncy room
# cpu task scheduling
# printer task priority
# network packet routing

# normal queue vs priority queue

# heap
# smallest number=higest priorty
# automatic sorting
# uses heapq module

# import heapq
# pq=[]

# heapq.heappush(pq,3)
# heapq.heappush(pq,1)
# heapq.heappush(pq,2)

# print("priority queue",pq)
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))

# import heapq

# pq=[]

# heapq.heappush(2,"medium task")
# heapq.heappush(1,"high task")
# heapq.heappush(3,"low task")

# while pq:
#     priority,task=heapq.heappop(pq)
#     print(priority,task)

