#what is time tuple
print("what is time tuple\n")
import datetime
import time
print("time tuple--\n",time.gmtime())

#write a program to get formatted time.
import time
print("time structure==\n",time.localtime(time.time()))
print("\n")
print("formatted time--\n",time.asctime(time.localtime(time.time())))
print("\n------------------------------\n")


#Extract month from the time.
import datetime
from datetime import date
d=datetime.date.today()
print("month--",d.month)
print("\n-------------------------------\n")


#Extract day from the time.
from datetime import datetime
a=datetime.now
print("day--",a.strftime("%A"))
print("\n----------------------------------\n")


#extract date from time.
import datetime
from datetime import date
d=datetime.date.today()
print("date--",d.day)
print("\n-----------------------------------\n")


#write a program to print time using localtime.
import datetime
print("time using localtime--",time.asctime(time.localtime()))
print("\n-------------------------------------\n")



#Find the factorial of a number input  by using math package functions.
import  math
x=int(input("enter any number whose factorial you want to calculate"))
print("factorial is==",math.factorial(x))
print("\n---------------------------------------\n")


#Find the gcd of a number  input by user using math package function.
import math
x=int(input("enterfirst number=="))
y=int(input("enter other number=="))
print("greatest common divisor--",math.gcd(15,20))
print("\n--------------------------------------\n")


#use os package and do the folloeing tasks.
print("1.get current working directory.\n")
print("2.get the user environment\n")
import os
print("current working directory--\n",os.getcwd())
print("\nuser environment--\n",os.environ)

