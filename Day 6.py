# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self. __balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("deposit:",amount)
#     def withdraw(self,amount):
#         if amount<=self. __balance:
#             self.__balance-=amount
#             print("withdrawal successful",self.withdraw)
#         else:
#             print("Insufficent balance")
#     def show_balance(self):
#         print("THE bank balance:",self.__balance)
# pin=1190
# PIN=int(input("Enter the PIN number:"))
# name=input("Enter the name:")
# balance=int(input("Enter the opening balance:"))
# s=BankAccount(name,balance)
# while True:
#     if pin==PIN:
#             print("\n 1.deposit 2.withdraw 3.check Balance 4.Exit")
#             choice=int(input("enter your choice:"))
#             if choice==1:
#                 amt=int(input("Enter your amount:"))
#                 s.deposit(amt)
#             elif choice==2:
#                 withdraw=int(input("Enter the withdraw amount:"))
#                 s.withdraw(withdraw)
#             elif choice==3:
#                 s.show_balance()
#             elif choice==4:
#                 print("Thanks for Visting our ATM")
#                 break
#     else:
#           print("Enter the valid PIN number")
#           break


#Polymorphsim

#build in function
#len()
# print(len("HELLo"))
# print(len([1,2,3,4,5,6,7]))

# #operator polymorphism
# print(5+3)
# print("5"+"3")


# def add(a,b):
#     return a+b
# print(add(5,3))
# print(add('hello','world'))

# class animal:
#     def sound(self):
#         print("animal make sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meows")
# d=dog()
# c=cat()
# a=animal()


# a.sound()
# d.sound()
# c.sound()



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposit:", amount)

#     def withdraw(self, amount):
#         pass

#     def show_balance(self):
#         return self.__balance   


# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.show_balance():
#             self._BankAccount__balance -= amount   
#             print("Withdrawal successful:", amount)
#         else:
#             print("Insufficient balance")


# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.show_balance():
#             self._BankAccount__balance -= amount
#             print("Withdrawal successful:", amount)
#         else:
#             print("Insufficient balance")


# pin = 1190
# PIN = int(input("Enter the PIN number:"))
# name = input("Enter the name:")
# balance = int(input("Enter the opening balance:"))

# print("1. Savings Account")
# print("2. Current Account")
# ch = int(input("Enter your Account type:"))

# if ch == 1:
#     obj = SavingsAccount(name, balance)
# else:
#     obj = CurrentAccount(name, balance)

# while True:
#     if pin == PIN:
#         print("\n1. Deposit  2. Withdraw  3. Check Balance  4. Exit")
#         choice = int(input("Enter your choice:"))

#         if choice == 1:
#             amt = int(input("Enter your amount:"))
#             obj.deposit(amt)

#         elif choice == 2:
#             amt = int(input("Enter the withdraw amount:"))
#             obj.withdraw(amt)

#         elif choice == 3:
#             print("The bank balance:", obj.show_balance())

#         elif choice == 4:
#             print("Thanks for Visiting our ATM")
#             break
#     else:
#         print("Wrong PIN number")
#         break



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount, "New Balance:", self.balance)

#     def show_balance(self):
#         return self.balance


# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal:", amount, "New Balance:", self.balance)
#         else:
#             print("Insufficient balance")


# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal:", amount, "New Balance:", self.balance)
#         else:
#             print("Insufficient balance")


# # Main program
# pin = 1190
# PIN = int(input("Enter the PIN number: "))
# name = input("Enter the name: ")
# balance = int(input("Enter the opening balance: "))

# print("1. Savings Account")
# print("2. Current Account")
# ch = int(input("Enter your Account type: "))

# if ch == 1:
#     obj = SavingsAccount(name, balance)
# else:
#     obj = CurrentAccount(name, balance)

# while True:
#     if pin == PIN:
#         print("\n1. Deposit 2. Withdraw 3. Check Balance 4. Exit")
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             amt = int(input("Enter your amount: "))
#             obj.deposit(amt)
#         elif choice == 2:
#             withdraw_amt = int(input("Enter the withdraw amount: "))
#             obj.withdraw(withdraw_amt)
#         elif choice == 3:
#             print("Balance:", obj.show_balance())
#         elif choice == 4:
#             print("Thank you for banking with us!")
#             break
#     else:
#         print("Invalid PIN")
#         break



# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side

# class circle(shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return 3.14* self.radius*self.radius

# square=square(2)
# circle=circle(4)
# print(square.area())
# print(circle.area())



# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, number, total_seats):
#         self.number = number
#         self.total_seats = total_seats

#     @abstractmethod
#     def calculate_fare(self):
#         pass

#     def show_details(self):
#         print("Bus Number:", self.number)
#         print("Total Seats:", self.total_seats)


# class LuxuryBus(Vehicle):
#     def calculate_fare(self):
#         return 500

# class OrdinaryBus(Vehicle):
#     def calculate_fare(self):
#         return 200

# class SeatManager:
#     def __init__(self, total_seats):
#         self.__total_seats = total_seats
#         self.__booked = []

#     def book_seat(self):
#         if len(self.__booked) < self.__total_seats:
#             seat_no = len(self.__booked) + 1
#             self.__booked.append(seat_no)
#             return seat_no
#         else:
#             return None

#     def cancel_seat(self, seat_no):
#         if seat_no in self.__booked:
#             self.__booked.remove(seat_no)
#             print("Seat", seat_no, "cancelled successfully.")
#         else:
#             print("Invalid seat number.")

#     def available_seats(self):
#         return self.__total_seats - len(self.__booked)

# class Passenger:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("Passenger Name:", self.name)
#         print("Passenger Age:", self.age)


# class Ticket:
#     def __init__(self, passenger, bus, seat, fare):
#         self.passenger = passenger
#         self.bus = bus
#         self.seat = seat
#         self.fare = fare

#     def show_ticket(self):
#         print("\n----- TICKET DETAILS -----")
#         self.passenger.show()
#         print("Bus Number:", self.bus.number)
#         print("Seat Number:", self.seat)
#         print("Fare:", self.fare)
#         print("---------------------------")


# print("1. Luxury Bus")
# print("2. Ordinary Bus")

# choice = int(input("Choose Bus Type: "))

# if choice == 1:
#     bus = LuxuryBus("LUX123", 5)
# else:
#     bus = OrdinaryBus("ORD456", 5)

# seat_manager = SeatManager(bus.total_seats)
# tickets = []

# while True:
#     print("\n1. Available Seats")
#     print("2. Book Seat")
#     print("3. Cancel Seat")
#     print("4. Show Tickets")
#     print("5. Exit")

#     option = int(input("Enter choice: "))

#     if option == 1:
#         print("Available Seats:", seat_manager.available_seats())

#     elif option == 2:
#         name = input("Enter Passenger Name: ")
#         age = int(input("Enter Passenger Age: "))

#         seat = seat_manager.book_seat()

#         if seat is None:
#             print("Bus is Full!")
#         else:
#             passenger = Passenger(name, age)
#             fare = bus.calculate_fare()   
#             ticket = Ticket(passenger, bus, seat, fare)
#             tickets.append(ticket)
#             ticket.show_ticket()

#     elif option == 3:
#         seat_no = int(input("Enter seat number to cancel: "))
#         seat_manager.cancel_seat(seat_no)

#     elif option == 4:
#         if not tickets:
#             print("No tickets booked yet.")
#         else:
#             for t in tickets:
#                 t.show_ticket()

#     elif option == 5:
#         print("Thank you for using Bus Booking System!")
#         break

#     else:
#         print("Invalid choice!")

