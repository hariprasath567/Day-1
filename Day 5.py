# class student:
#     def details(self,name,marks):
#         if marks>=40:
#             result="pass"
#             print(name,marks)
#             print(result)
#         else:
#             print("fail")
            
# s1=student()
# s2=student()
# s1.details("hari",88)


# class TemperatureConverter:
#     def __init__(self, celsius):
#         self.celsius= celsius

#     def c_to_f(self):
#         for c in self.celsius:
#             f = c * (9/5) + 32
#             print("f value is:",f)

# celsius_values = [0, 20, 37, 100]
# converter = TemperatureConverter(celsius_values)
# converter.c_to_f()

#OOPS
# def func(a,b):
#     return a+b
# result=func(5,7)
# print(result)



#syntax

# class Classname:
#     def method_name (self):
#         print("Message")


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show_result(self):
#         if self.marks>=40:
#             result="pass"
#         else:
#             result="Fail"
#         print('\n Student Name',self.name)
#         print("Marks",self.marks)
#         print("result:",result)
# name=input("Enter your name:")
# marks=int(input("Enter your mark:"))
# s1=Student(name,marks)
# s1.show_result()
