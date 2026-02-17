# fees Details
# student_type=input("Enter the student type:")
# if(student_type=='MSDS'):
#     tution_fee=float(input("Enter the tution fee:"))
#     bus_fee=float(input("Enter the bus fee:"))
#     print("the fee to be paid by the student is Rs:",tution_fee+bus_fee)
# elif(student_type=='MSH'):
#     tution_fee=float(input("Enter the tution fee:"))
#     hostel_fee=float(input("Enter the hostel fee:"))
#     print("the fee to be paid by the student is Rs:",tution_fee+hostel_fee)
# elif(student_type=='MGSDS'):
#    tution_fee=float(input("Enter the tution fee:"))
#    bus_fee=float(input("Enter the bus fee:"))
#    print("the fee to be paid by the student is Rs:",tution_fee+bus_fee)
# elif(student_type=='MGSH'):
#     tution_fee=float(input("Enter the tution fee:"))
#     hostel_fee=float(input("Enter the hostel fee:"))
#     print("the fee to be paid by the student is Rs:",tution_fee+hostel_fee)

# ATM Withdraw money
# acc_balance=100000
# withdrawl_amt=int(input("Enter the withdrawal amount:"))
# if(withdrawl_amt>acc_balance):
#     print("Insufficient balance")
# elif(withdrawl_amt>10000):
#     print("Limit reached")
# else:
#     print("Transaction completed")

# account_balance=100000
# PIN=1190
# pin=(int(input("enter the pin number:")))
# if(pin==PIN):
#     withdrawal_amount=int(input("enter the withrawal amount:"))
#     if(withdrawal_amount>account_balance):
#         print("insufficient balance")
#     elif(withdrawal_amount>10000):
#         print("withdrawal limit reached")
#     else:
#         print("transaction complete")
#         main_balance=account_balance-withdrawal_amount
#         print("account balance",main_balance)
# elif(pin!=PIN):
#     print("wrong pin")


# child=150
# adult=250
# senior=200
# age=int(input("enter age ="))
# time=input("enter the show time morning/evening:")
# morning_show=50
# evening_show=0
# if(age<5):
#     print("free ticket")
# elif(age>=5 and age<=17):
#     if(time=='morning'):
#         total=child-morning_show
#         print("the ticket price:",total)
#     elif(time=='evening'):
#         total=child-evening_show
#         print("the ticket price:",total)
# elif(age>=18 and age<=60):
#     if(time=='morning'):
#         total=adult-morning_show
#         print("the ticket price:",total)
#     elif(time=='evening'):
#         total=adult-evening_show
#         print("the ticket price:",total)
# elif(age>60):
#     if(time=='morning'):
#         total=senior-morning_show
#         print("the ticket price:",(30/100)*total)
#     elif(time=='evening'):
#         total=senior-evening_show
#         print("the ticket price:",(30/100)*total)


# a=0
# for i in range(1,101):
#     if(i%2==1):
#         a+=i
#         print(i)
# print("sum",a)


# a=0
# for i in range(1,101):
#     if(i%2==0):
#         a+=i
#         print(i)
# print("sum",a)


# for i in range(1,11):
#     a=i*5
#     print(i,"* 5 =",a)

# T=int(input("enter the mark="))
# E=int(input("enter the mark="))
# M=int(input("enter the mark="))
# C=int(input("enter the mark="))
# P=int(input("enter the mark="))
# total=(T+E+M+C+P)
# print("total mark=",total)
# average=((T+E+M+C+P)/5)
# print("average mark=",average)

# n=int(input("enter the value="))
# for i in range(1,n+1):
#     print("*"*i)

# n=int(input("enter the value="))
# for i in range(n,0,-1):
#     print("*"*i)













# i=1
# a=0
# while (i<=101):
#     if(i%2==1):
#         print(i)
#         a=a+i
#     i=i+1
    
# print("sum",a)


# i=1
# a=0
# while (i<=101):
#     if(i%2==0):
#         print(i)
#         a=a+i
#     i=i+1
    
# print("sum",a)

# n=int(input("enter the value"))
# i=0
# while (i<n):
#     i=i+1
#     a=i*5
    
#     print(i,"* 5 =",a)


# BUS SEAT BOOKING 
# total_seats = int(input("Enter the total number of seats in the bus: "))
# seat_number = 1
# while True:
#     if seat_number <= total_seats:
#         passenger_name = input(f"Enter passenger name for seat {seat_number}: ")       
#         print(f"Seat {seat_number} booked for {passenger_name}")       
#         seat_number += 1
#     else:
#         print("All seats are booked.")
#         break
