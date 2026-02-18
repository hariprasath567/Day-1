# fibonacci series
# n=int(input("enter the value:"))
# a,b=0,1
# for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b  


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib = fibonacci()

# for _ in range(8):
#     print(next(fib),end=" ")


# list indices
# list=[1,2,3,4,5]
# print(list[4])

# list slicing
# syntax [start index(include):end index(exclide)]
# print(list[1:4])
# print(list[:4])
# print(list[0:])
# print(list[-3:-1])

# list operator
# 1)concation operator(1)
# a=[1,2,3,4]
# b=[5,6,7]
# print(a+b)

# realtive usage
# 2)repition operator
# num=[1,2,3,4]
# print(num*3)

# 3)membership(in,out-in)
# f=["apple","banana","orange"]
# print("apple" in f)
# print("apple" not in f)
# print("grape" in f)

# comparsion
# list1=[1,2,3]
# list2=[1,2,4]
# print(list1==list2)
# print(list1<list2)

# L1=(0,1,2,3,4)
# L2=(5,6,7,8,9)
# print(list[2])
# print(list[1:4])
# print(L1+L2)
# print("3" in L1)
# print("7" in L1)
# print("3" not in L1)
# print("8" not in L2)
# print(L1==L2)
# print(L1<L2)

# list mwthod
# append
# n=[1,2,3]
# n.append(4)
# print(n)

# insert item
# syntex(index,item)
# num=[1,2,3,4]
# num.insert(2,5)
# print(num)

# extend
# a=[1,2]
# b=[3,4]
# b.extend(a)
# print(b)
# a.extend(b)
# print(a)

# remove
# num=[1,2,3,4,5,6]
# num.remove(2)
# num.remove(6)
# print(num)

# pop
# a=[10,20,30,40,50]
# a.pop(2)
# print(a)

# clear
# a=[10,20,30,40,50]
# a.clear()
# print(a)

# index
# num=[10,20,60,80,90]
# print(num.index(60)) 
# print(num[2])

# count
# num=[10,20,30,40,50,60]
# print(num.count(50))

# sort
# num=[10,20,30,40,33,21,15,45,65,72,55]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)

# reverse
# num=[10,20,30,40,50]
# num.reverse()
# print(num)

# copy
# num=[10,20,30,40,50]
# b=num.copy()
# print(b)

# map , filter
# n=[1,2,3,4]
# result=list(map(lambda x:x*2,n))
# print(result)

# num=[10,20,30,40,50,60]
# def function (x):
#     return x*2
# result=list(map(function,num))
# print(result)

# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# def function(x):
#     return x%2==0
# result=list(filter(function,n))
# print(result)

# from functools import reduce
# num=[1,2,3,4,5,6]
# result= reduce(lambda a,b:a+b,num)
# print(result)

# from functools import reduce
# num=[1,2,3,4,5,6]
# result= reduce(lambda a,b:a*b,num)
# print(result)

# from functools import reduce
# num=[1,2,3,4,5,6]
# result= reduce(lambda a,b:a%b,num)
# print(result)

# from functools import reduce
# num=[1,2,3,4,5,6]
# result= reduce(lambda a,b:a-b,num)
# print(result)

# from functools import reduce
# num=[1,2,3,4,5,6,7,8,9,10]
# def function(x):
#     return x%2==0
# result=list(filter(function,num))
# r= reduce(lambda a,b:a+b,result)
# print(result)
# print(r)

# from functools import reduce
# num=[1,2,3,4,5,6,7,8,9,10]
# def function(x):
#     return x%2!=0
# result=list(filter(function,num))
# r= reduce(lambda a,b:a+b,result)
# print(result)
# print(r)

# palindrome
# word=input("enter the text:")
# palindrome=word[::-1]
# if(word==palindrome):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# word=input("enter the text:")
# r=""
# for ch in word:
#     r= ch+r
# if(word==r):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# num=int(input("enter the value"))
# original=num
# rev=0
# while num>0:
#     digits=num%10
#     rev=rev*10+digits
#     num=num//10
# if(original==rev):
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")