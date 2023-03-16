# adding two numbers.
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=a+b
# print(f"sum of {a} and {b} is {c}")

# ⭐String formating
# num1 = 20
# num2 = 30
# print(f"sum of {num1} and {num2} is {num1+num2}")

# OR

# num1 = 20
# num2 = 30
# print("sum of {} and {} is {}" .format(num1,num2,num1+num2))

# OR

# num1 = 20
# num2 = 30
# print("sum of %d and %d is %d" %(num1,num2,num1+num2))

# ⭐use of map( ) and split()
# a=input("enter numbers with space:  ")
# print(a)
# print(type(a))
# b=a.split()
# print(b)
# print(type(b))
# x,y,z=map(int,b)
# print(x,y,z)
# t,r,e=map(int,input("enter numbers space: ").split())
# print(t,r,e)
# print(type(t))

# #finding max in between 3 numbers.
# n1,n2,n3 =map(int,input("Enter numbers").split())
# n1=int(input("Enter 1st number: "))
# n2=int(input("Enter 2nd number: "))
# n3=int(input("Enter 3rd number: "))
# print(f"{n1} is max") if n1>n2 and n1>n3 else print(f'{n2} is max') if n2>n1 and n2>n3 else print(f" {n3} is max")

# ch=input("Enter a alphabet: ")
# print(f"alphabet{ch} is an alphabet") if (ch>="a" and ch<="z") or (ch>="A" and ch<="Z") else print ("not an aphlabet")

# ch=input("Enter a character: ")
# print(f"{ch} is a vowel") if (ch=="a" or ch=="e"or ch=="i"or ch=="o" or ch=="U") else print ("not vowel")

# Number convertion
# # num=int(input("Enter a number: "))
# print("hexadecimal of"+'num'+":"+str(hex(num)))
# print("value %x,%o,%d,%c,%e,%f"%(num,num,num,num,num,num))

# a = 65
# print("{:d},{:x},{:o}".format(a,a,a))

# #Area of triangle
# a=float(input("Enter first side: "))
# b=float(input("Enter second side: "))
# c=float(input("Enter third side: "))
# print(a,b,c)
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print("area {:.2f}".format(area))
# print("area=",area)
# print(f"area is {area:.2f}")
# print("area is %.3f"%(area))

# ##Arithmatic operation of two numbers.
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# add= num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# modul=num1%num2
# print(f"addition is {add}\nsubstraction is {sub}\n multiplication is {mul}\n div is {div}\n modul is {modul}")

# Circle Area.
# r=int(input("Enter radius: "))
# area=3.14*r**2
# c=2*3.14*r
# print(f"area is {area}\n circumfere is {c}")
# print("Area ="+str(round(area))+"\n circumference ="+str(round(c,2)))

# #program to convert degree fehrenheit to degree celsius,celsiu to fehrenheit.
# t1=float(input("Enter the temperature in fahrenheit: "))
# t2=float(input("temperature in celsius: "))
# c=0.56*(t1-32)
# f=(t2*1.8)+32
# print(f"temperature in degree celsius :{c:.1f} ")
# print(f"temperature in degree fehrenheit:{f:.2f}")

# cha=input("enter a character: ")
# ascii=ord(cha)
# print(f"ascii {ascii}")

# num=int(input("enter a number: "))
# char=chr(num)
# print(f"char {char}")

# converting a character lowercase to uper case without fuction using.
# ch=input("enter a character: ")
# ch1ffffff=chr(ord(ch)-32)
# print(ch1ffffff)

# import turtle
# turtle.color("red")
# turtle.circle(50)

# My Address
# Name="Satyabrat pradhan"
# Father_name="Kartik ch pradhan"
# pin=759122
# address="angul"
# print("Name:",Name + "\nFather_name:",Father_name + "\npin:",str(pin)+"\naddress",address )

# x=int(input("enter any value:"))
# y=int(input("enter any value:"))
# z=x**y
# print(z)

# Bill amount for an itrm given its quantity sold, value,discount,and tax.
# qty=float(input("Enter the quantitiy of item sold : "))
# val=float(input("Enter the value of item : "))
# discount=float(input("Enter the discount percentage : "))
# tax=float(input("Enter the tax : "))
# amt=qty*val
# discount_amt=(amt*discount)/100
# sub_total=amt-discount_amt
# tax_amt=(sub_total*tax)/100
# total_amt=sub_total+tax_amt
# print("**********BILL*********")
# print("Quantity sold : \t ",qty)
# print("Price per item : \t",val)
# print("\n \t \t ----------------")
# print("Amount : \t \t",amt)
# print("Discount : \t\t-",discount_amt)
# print("  \t  \t-----------------")
# print("Discount Total : \t",sub_total)
# print("Tax : \t\t\t+",tax_amt)
# print(" \t \t  -----------------")
# print("Total amount to be Paid ",total_amt)

# if 100>30:
#     print("s")
# print(5)

# write a program to determine a char entered by user
# char = input("press any key: ")
# if char.isalpha():
#     print("user has enter a character")
# if (char.isdigit()):
#     print("user has enter a digit ")``
# if (char.isspace()):
#     print("user has enter a white space")

# Write a program to find input number ia +ve,-ve or zero.
# num=int(input("Enter a number: "))
# if num>0:
#     print(f" number {num} is +ve")
# if num<0:
#     print(f" number {num} is -ve")
# if num==0:
#     print(f"number {num} is zero")

# num=int(input("Enter a number: "))
# if num>0:
#     print(f" number {num} is +ve")
# elif num<0:
#     print(f" number {num} is -ve")
# else :
#     print(f"number {num} is zero")

# Write a program input number is divisible by 7.
# num=int(input("Enter a number"))
# if num % 7==0:
#     print(f"{num} is divsible by 7")
# else :
#     print(f"{num} is not divible by 7")

# program for Login application.
# username=input("enter username: ")
# password=input("enter password: ")
# if username=="satya":
#     if password=="12345":
#         print("you are welcome")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")

# Finding maximum between 3 members.
# n1,n2,n3=map(int,input("Enter numbers: ").split())
# if n1>n2:
#     if n1>n3:
#         print(f"{n1} is max")
#     else:
#         print(f"{n3} is max")
# elif n2 >n3:
#     print(f'{n2} is max')
# else:
#     print(f"{n3} is max ")

# ⭐ Leap year
# year=int(input("Enter any year: "))
# if year%4==0:
#     if year%100 ==0:
#         if year%400==0:
#             print(f"{year} is leap")
#         else:
#             print(f"{year} is not leap year")
#     else :
#         print(f"{year} is leap year")
# else:
#     print(f" {year} is not leap")

# year=int(input("Enter any year:"))
# if year% 400==0:
#     print (f"{year} is leap")
# elif year%4==0 and year%100 !=0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

#⭐ Match case.
# num=int(input("Enter any number: "))
# match(num):
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case _:
#         print("invalid input")

# print("*****MENU*****")
# print("1. Finding Area of Circle")
# print("2. Finding Area of Triangle")
# print("3. Exit")
# opt=int(input("Enter your option: "))
# match (opt):
#    case 1:
#       r=float(input("Enter Radius of Circle"))
#       area=math.pi*r**2
#       print(f'Area of Circle {area:.2f}')
#    case 2:
#        base,height=map(float,input("Enter base,height").split())
#        area=0.5*base*height
#        print(f'Area of Triangle is {area:.2f}')
#    case 3:
#        print("***Happy Learning***")
#    case _:
#        print("invalid option")

# Write a program to print a string 10 times.
# c=1
# while c<=10:
#     print("Krishna")
#     c=c+1

# Write a program to print the series 1,2,3,4,5,6,7,...20.
# num=1
# while num<=20:
#     print(num,end=" ")
#     num+=1

# ⭐Write a program to print A TO Z.
# c="A"
# while c<="Z":
#     print(c,end=" ")
#     c=chr(ord(c)+1)

# Printing mathematic table of a number.
# num=int(input("Enter any number: "))
# i=1
# while i<=10:
#     # pr=num*i
#     print(f"{num}*{i}={num*i}")
#     i=i+1

# ⭐ Finding length of a number
# num=int(input("enter any number: "))
# c=0
# while num>0:
#     num=num//10
#     c=c+1
# print(f"length of number is {c}")

# ⭐Sum of digits of a number.
# num=int(input("Enter any number: "))
# s=0
# while num>0:
#     r=num%10
#     s=s+r
#     num=num//10
# print(f"sum of digit:{s}")

# Write a program to reverse a number
# num=int(input("enter a number: "))
# rev=0
# while num>0:
#     r=num%10
#     rev=(rev*10)+r
#     num=num//10
# print(f"reverse of number is {rev}")

# ⭐ Write a progrma to find the entered number is a palendrom number
# num=int(input("enter a number: "))
# rev=0
# num1=num
# while num>0:
#     r=num%10
#     rev=(rev*10)+r
#     num=num//10
# print(f'{num1} is palendrom') if num1==rev else print(f'{num1} is not palendrom')

# ⭐ Write a program to print input number is a Armstrong number
# num=int(input("Enter a number: "))
# s=0
# num1=num
# while num>0:
#     r=num%10
#     s=s+(r**3)
#     num=num//10
# print(f'{num}')
# print(f'{num1} is armstrong ') if s==num1 else print(f'{num1} is not armstrong')

# ⭐ Write a program to find maximum digit of input number
# num=int(input("enter any number: "))
# m=0
# while num>0:
#     r=num%10
#     if r>m:
#         m=r
#     num=num//10
# print(f'maximum digit of input number is {m}')


# ⭐ FOR LOOP

# x=input("enter your name:")
# for i in range(10):
#     print(x,end="\t")

# for loop for reading a string.
# str=input("enter a string")
# for i in str:
#     print(i,end="")

# ⭐program to convert a decimal number into binary number 
# num=int(input("Enter any number:"))
# l=[]
# while (num):
#     r=num%2
#     l.append(r)
#     num=num//2
# for i in range(len(l)-1,-1,-1):
#     print(l[i],end="")


# program to count number of vowel in an string.
# str=input("enter a string: ")
# c=0
# for ch in str:
#     if ch in ("aeiouAEIOU"):
#         c=c+1
# print(f"number of vowel inside {str} is {c}")

# Mathematic table of a number by using for loop.
# num=int(input("Enter any number: "))
# for i in range(1,11):
#     # pr=num*i
#     # print(f"{num}* {i}={pr}")
#     print(f"{num}* {i}={num*i}")

# ⭐ Write a program to count alphabet ,digit and special character in a given string.
# str1 = input("Enter any string: ")
# ac,dc,sc = 0,0,0
# for ch in str1:
#       if ch>="A" and ch<="Z" or ch>="a" and ch<="z":
#             ac+=1
#       elif ch>="0" and ch<= "9":
#             dc+=1
#       else:
#             sc+=1
# print(f"alphabet count is {ac}\ndigit count is {dc}\n special character count is {sc}")

# ⭐Write a program to find factorial of a number.
# num=int(input("Enter a number: "))
# fact=1
# for n in range(1,num+1):
#     fact=fact *n
# print(f"{num} 's factorial is {fact}")

# # Write a program to generate range of even numbers 2,4,6,8,,10...n
# n=int(input("Enter a number: "))
# for num in range(2,n+1,2):
#     print(num,end=" ")

# ⭐Write a program to find a number is prime or not.
# num=int(input("Enter a number: "))
# c=0
# for i in range(1,num+1):
#    if num%i==0:
#       c=c+1
# if c==2:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

#⭐ Write a program to generate all prime number between m to n.
# m=int(input("Enter the velue of m: "))
# n=int(input("Enter the velue of n: "))
# while m<=n:
#     i=1
#     c=0
#     while i<=m:
#         if m%i==0:
#             c=c+1
#         i=i+1
#     if c==2:
#         print(f"{m} is prime")
#     m=m+1

#⭐ Python program to display all the prime numbers within an interval
# lower = 1
# upper = 100
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

#⭐Python program to display all the prime numbers within 1 to 50.
# for num in range(1,51):
#     c=0
#     for i in range(1,num+1):
#         if num%i==0:
#             c=c+1
#     if c==2:
#         print(num)

# #⭐ Write a program to find factorial of all numbers  m to n.
# m,n=map(int,input("enter the value of m,n: ").split())
# while m<=n:
#     fact=1
#     i=1   
#     while i<=m:
#         fact=fact*i
#         i=i+1
#     print(f"factorial of {m} is {fact}")
#     m=m+1

# num=int(input("enter number:"))
# f=1
# i=1
# while i<=num:
#     f=f*i
#     i+=1
# print(f) 

# num=int(input("enter number:"))
# f=1
# for i in range(1,num+1):
#     f=f*i
#     print(i)
# print(f)

# #Write a program to show the patern 1 2 3 4 5
#                                     1 2 3 4 5
#                                     1 2 3 4 5
#                                     1 2 3 4 5
#                                     1 2 3 4 5
# i=1
# while i<=5:
#     num=1
#     while num<=5:
#         print(num,end=" ")
#         num=num+1
#     i=i+1
#     print()

# ## Using nested for loop print this parten 1 2 3 4 5
#                                            1 2 3 4 5
#                                            1 2 3 4 5
#                                            1 2 3 4 5
#                                            1 2 3 4 5
# for i in range(1,6):
#     for i in range(1,6):
#         print(i,end=" ")
#     print()

# using nested for loop print math table 1- 10.
# for num in range(1,11):
#     for i in range(1,11):
#         # print(num*i,end="")
#          print(f"{num*i:3d}",end=" ")
#     print()

# ## using nested for loop print the partern 1 1 1 1 1
#                                            2 2 2 2 2
#                                            3 3 3 3 3
#                                            4 4 4 4 4
#                                            5 5 5 5 5
# for r in range (1,6):
#     for c in range(1,6):
#         print(r,end=" ")
#     print()

# Using nesterd for loop print this patern  5 5 5 5 5
#                                            4 4 4 4 4
#                                            3 3 3 3 3
#                                            2 2 2 2 2
#                                            1 1 1 1 1
# for r in range(5,0,-1):
#     for c in range(1,6):
#         print(r,end=" ")
#     print()

# ##Write a program to print this patern 1
#                                        2 2
#                                        3 3 3
#                                        4 4 4 4
#                                        5 5 5 5 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#         # print(c,end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#         # print(c,end="")
#     print()

# for i in range(5,0,-1):              # x x x x x
#     for j in range(1,i+1):           # x x x x
#         print("x",end=" ")           # x x x
#     print()                          # x x
#                                        x
# USE OF BREAK STATEMENT
# n=1
# while n<=10:
#     print(n)
#     if n==5:
#         break
#     n=n+1

# print all odd number from 1 to 100.
# for i in range(1,101):
#     if i%2==0:
#         continue
#     print(i,end="  ")
###############################################################

# write a program to determine the character enter by user.
# char=input("enter any key: ")
# if char.isalpha():
#     print('the user has enter a alphabet')
# if char.isdigit():
#     print("the has enter a digit")
# if char.isspace():
#     print("the user has enter a space")

# finding large number in between two numbers.
# a,b=map(int,input("enter two number: ").split())
# if a>b:
#     print(f" {a} is larger")
# else:
#     print(f"{b} is larger")

# a,b=map(int,input("enter two number: ").split())
# if a>b:
#     large=a
# else:
#     large=b
# print(f"large is {large} ")
# print("large=",large)

# ⭐ DATA STRUCTURE***************** *****

# list1=list(range(1,101))
# print(list1)
# for i in range(0,100):
#     print(list1[i],end=',')
# print()
# print()

# for i in range(-1,-101,-1):
#     print(list1[i],end=',')

# Write a program to read n integers and add to a list.
# list=[]
# n=int(input("enter how many itegers:"))
# for i in range(n):
#     num=int(input("enter any numbes:"))
#     list.append(num)
# print(list)

# Write a program to read score of n players and display total scores.
# score=[]
# n=int(input("enter how many players:"))
# for i in range(n):
#     s=int(input("enter score of player:"))
#     score.append(s)
# total_score=0
# for i in range(n):
#     total_score=total_score+score[i]
# print(total_score)

# Uses of iterator and enumerete
# list=[10,20,30,40,50]
# x=iter(list)
# c1=next(x)
# c2=next(x)
# c3=next(x)
# c4=next(x)
# c5=next(x)
# print(c1,c2,c3,c4,c5)

# z=iter(list)
# for i in z:
#     print(i,end='  ')
# print()

# y=enumerate(list)
# c1=next(y)
# c2=next(y)
# c3=next(y)
# c4=next(y)
# c5=next(y)
# print(c1,c2,c3,c4,c5)
# print()

# v=enumerate(list)
# for i in v:
#     print(i,end=' ')

# Write a program to read n integers from a list,from the list separate even numbers
# to evenlist and oddnumbers to oddList.

# numList=[]
# evenList=[]
# oddList=[]
# n=int(input("how many intgers:"))
# for i in range(n):
#     value=int(input("enter the value of integer:"))
#     numList.append(value)
# print(numList)

# for value in numList:
#     if value%2==0:
#         evenList.append(value)
#     else:
#         oddList.append(value)
# print(f"even number is {evenList}")
# print(f"odd number is {oddList}"

# n=int(input())
# scores=list(map(int,input().split()[:n]))
# print(scores)

# c=[10,20,30,60,90,10]
# print(c[3],type(c),)
# j=c[:1]
# print(j)
# m=max(c)
# print(m)
# c.sort()
# print(c)
# mi=min(c)
# print(mi)

# STACK
# stack=[]
# while True:
#   print("***Stack****")
#   print("1.Push")
#   print("2.Pop")
#   print("3.View")
#   print("4.Exit")
#   opt=int(input("Enter Option:"))
#   if opt==1:
#     ele=int(input("Enter element to push"))
#     stack.append(ele)
#     print("element pushed inside stack")
#   elif opt==2:
#     if len(stack)==0:
#      print("Stack is empty")
#     else:
#      ele=stack.pop()
#      print(f'{ele} poped from stack')
#   elif opt==3:
#     print(f'Elements of stack {stack}')
#   elif opt==4:
#    break

# list=[1,2,3,4,3,5,6,7,2,8,9]
# list1=list.count(2)
# list2=list.index(4)
# # # list.reverse()
# print(list1,list2)
# list.remove(20)
# print(list)

# Nested list
# matrix=[[10,20,30,],[40,50,60],[70,80,90]]
# print(matrix[0][2])

# Creating a 3*3 matrix.
# matrix1=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         print(matrix1[i][j],end='')
#     print()

# Creating a 3*3 matrix.
# matrix1=[[1,2,3],[4,5,6],[7,8,9]]
# for row in matrix1:
#     for col in row:
#         print(col,end='  ')
#     print()

# matrix=[]
# for i in range(3):
#     row=[]
#     matrix.append(row)
#     ele=int(input("enter elements:"))
#     row.append(ele)
# print(matrix)

# Write a program to read a 3*2 matrix and diplay on run time.
# matrix=[]
# for i in range(3):
#     row=[]
#     matrix.append(row)

#     for j in range(2):
#          ele=int(input("enter element"))
#          row.append(ele)
# print(matrix)

# Write a program to add two matrices.
# matrix1=[]
# matrix2=[]
# # print("Enter the elements of first matrix1")
# for i in range(2):
#     row=[]
#     for j in range(2):
#         ele=int(input("Enter elements"))
#         row.append(ele)
#     matrix1.append(row)
# # print("Enter the elements of first matrix2")
# for i in range(2):
#     row=[]
#     for j in range(2):
#         ele=int(input("Enter elements"))
#         row.append(ele)
#     matrix2.append(row)
# matrix3=[]
# for i in range(2):
#     row=[]
#     for j in range(2):
#         row.append(matrix1[i][j]+matrix2[i][j])
#     matrix3.append(row)
# print(matrix1)
# print(matrix2)
# print(matrix3)

# Write a program to read 5 elements in a list.
# list=[]
# for i in range(5):
#     ele=int(input("enter elements"))
#     list.append(ele)
# print(list)
# list1=[int(input("enter elements"))for i in range(5)]
# print(list1)

# list=[x for x in range(1,5)]
# print(list)

# list=[chr(i) for i in range(65,97)]
# print(list)

# list=[[int(input("enter elements")) for j in range(2)] for i in range(2)]
# print(list)

# Write a program to add two matrices.
# matrix1=[[int(input("enter elements")) for j in range(2)] for i in range(2)]
# matrix2=[[int(input("enter elements")) for j in range(2)] for i in range(2)]
# matrix3=[[matrix1[i][j]+matrix2[i][j] for j in range(2)] for i in range(2)]
# print(matrix1)
# print(matrix2)
# print(matrix3)

# write a program to print even numbers.
# list1=[3,4,5,6,2,6,7,9]
# list2=[value for value in list1 if value%2==0]
# list3=[value for value in list1 if (value%2)!=0]
# print(list2)
# print(list3)

# Write a program to print list items end with "h "
# nameList=['naresh','suresh','ramesh','Ram','Krishna']
# namelist1=[name for name in nameList if name[-1]=='h']
# nameList2=[name for name in nameList if name[0]=='r']
# print(nameList2)
# print(namelist1)

# TUPLE
# v=10,
# print(v,type(v))

# a,b,c=(1,2,3)
# print(a,b,c)

# a,b,c=1,2,3
# print(a,b,c)
# print(type(a))

# l1=[10,20,30,40,50]
# a,b,*c=l1
# print(a,b,c)

# a,b=map(int,input().split())
# print(a,b)

# b=()
# c=[]
# v={}
# d=set()

# print(type(d),type(b),type(c),type(v))

# a={10,20,30,40,50}
# print(a)

# b=set('naresh')
# print(b)

# 🤖Reading elements from set using next().
# set1={10,20,30,50,40}
# a=iter(set1)
# c=next(a)
# c1=next(a)
# print(c,c1)

# set1=set(range(10,110,10))
# print(set1)

# Dictionary
# dict1={1:10,2:20,3:30,4:40,5:50}
# for k in dict1:
#     print(k)
#     # print(k,dict1[k])

# Write a program to read n number of players scores.
# n=int(input("enter how many number of players:"))
# p={input("Name: "):int(input("runs:")) for i in range(n)}
# print(p)

# l1=[1,2,3,4,5]
# l2=[10,20,30,40,50]
# d1=dict(zip(l1,l2))
# print(d1)
# d2=dict(zip(range(1,6),range(10,60,10)))
# print(d2)

# users_dict={'naresh':'r123','Rama':'k123'}
# print('******login******')
# uname=input("user name:")
# pwd=input("password:")
# if uname in users_dict:
#     p=users_dict[uname]
#     if p==pwd:
#         print(f"{uname} welcome")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")

# product_price={'mouse':500,'keyboard':600,'pendrive':300}
# price=product_price['mouse']
# print(price)
# ssd=product_price['pendrive']
# print(ssd)
# price1=product_price.get('mouse')
# print(price1)
# price2=product_price.get("joystick")
# print(price2)

# sale_list={20:5000,21:6000,22:7000,23:8000}
# sale=sale_list[21]
# print(sale)

# d2=dict(zip(range(1,6),range(10,60,10)))
# print(d2)
# k=d2.keys()
# print(k)
# v=d2.values()
# print(v)
# i=d2.items()
# print(i)

# dict={1:10,2:30,4:50}
# for k in dict:
#     print(k,dict[k])

# #🤖FUCNTION

# for i in range(20):
#     print("*",end='')
# print()
# print("python is a programming language")
# for i in range(20):
#     print("*",end="")

# t=(10,390,450)
# print(max(t))

# 1️⃣no arguement and no return value
# def greet():
#     print("this is my first fuction")
# greet()
# greet()
# greet()
# greet()
# print(" print is a pre defind fuction")

# write a program to print this
# ********************
# python
# ********************
# programming
# ********************
# def draw_line():
#     for i in range(20):
#         print("*",end="")
#     print()
# draw_line()
# print("PYTHON")
# draw_line()
# print("PROGRAMMING")
# draw_line()

# 2️⃣ with arguement and no return value
# 🔢1.required positional arguement
# def draw_line(ch,l):
#     for i in range(l):
#         print(ch,end='')
#     print()
# draw_line("*",10)
# draw_line("#",20)
# draw_line("$",30)

# def draw_line(ch,l):
#     for i in range(l):
#         print(ch,end='')
#     print()
# def main():
#   draw_line("*",20)
#   draw_line("#",20)
#   draw_line("$",20)
# main()

# def isleap(year):
#     if year%4==0:
#         print(f"{year} is a leapyear")
#     else:
#         print(f"{year} is not leap")
# def iseven(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
# def isprime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c=c+1
#     if c==2:
#         print(f"{n} is prime")
#     else:
#         print(f"{n}  is not prime")
# def main():
#    isleap(2010)
#    iseven(6)
#    isprime(5)
# main()

# 3️⃣.with arguement and with return value
# Find maximum number in between two numbers.
# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def main():
#     num1,num2=map(int,input("enter number:").split())
#     num3=maximum(num1,num2)
#     print(f"{num3} is maximum")
# main()

# def uppercase(string):
#     upstring=""
#     for ch in string:
#         if ch>="a" and  ch<="z":
#             upstring=upstring + chr(ord(ch)-32)
#         else:
#             upstring=upstring + ch
#     return upstring
# def main():
#     str1=input("Enter a string:")
#     str2=uppercase(str1)
#     print(str2)
#     print(str1)
# main()

# 2.👉default arguement or optional arguements
# def fun1(a=None,b=None):
#     print(a,b)
# def main():
#     fun1()
#     fun1(10)
#     fun1(b=20)
#     fun1(a=30)
#     fun1(a=40,b=50)
# main()

# required arguement and default argue or optional argue
# def simple_interest(amt,t,r=1.5):
#     s=(amt*t*r)/100
#     return s
# def main():
#     s1=simple_interest(5000,12)
#     s2=simple_interest(9000,24,r=1.8)
#     print(f"s1 is {s1}")
#     print(f"s2 is {s2}")
# main()

# 3.👉 variable length arguement
# list1=[10,20,30,40,50]
# a,b,*c=list1
# print(a,b,c)
# tuple=(20,30,40,50,60)
# a,b,*c=tuple
# print(a,b,c)

# def fun1(*a):
#     print(a)
#     print(type(a))
# def main():
#     fun1()
#     fun1(10)
#     fun1(10,20)
#     fun1(10,2,3,4,5,6,7,8)
# main()

# sum of values using variable length arguement
# def add(*v):
#     sum=0
#     for value in v:
#         sum =sum+value
#     return sum
# def main():
#     sum1=add(10,20)
#     sum2=add(10,20,30)
#     print("result is",sum1)
#     print(f"result is:{sum2}")
#     print(sum1)
#     print(SOUND_MIXER_DIGITAL2)
# main()

# ## Write a program to find maximum value using variable length arguement
# def maximum(*v):
#     maxi=None
#     for i in range(len(v)):
#         if i==0:
#             maxi=v[0]
#         elif v[i]>maxi:
#             maxi=v[i]
#     return maxi
# def main():
#     result=maximum(10,20,30)
#     print(f"maximum number is {result}")
# main()

# 4👉keyword arguement
# list1=[(12,23),(2,34)]
# dict1=dict(list1)
# print(dict1)

# def fun(**a):
#     print(a)
#     print(type(a))
# def main():
#     fun(k=10,k2=20)
#     fun(courses='python',name='satya')
# main()

# dict=dict(zip(range(1,6),range(10,60,10)))
# print(dict)
# k=dict.keys()
# print(k)
# v=dict.values()
# print(v)
# item=dict.items()
# print(item)
# for key in k:
#     print(key)

# def displaysales(**kwargs):
#     for name,sales in kwargs.items():
#         print(name,sales)
# def main():
#     sales_Dict={'naresh':5000,
#                 'suresh':6000,
#                 'ramesh':7000
#     }
#     displaysales(**sales_Dict)
# main()

# Local variable
# def fun1():
#     x=100
#     y=200
#     print(x)
#     print(y)
# def main():
#     fun1()
# main()
# in local varible the scope of varible limited within the function, lifetime of these variabble until execution of function
# these varibles are allocated on memory on execution of function and de-allocated after execution of function

# Global variables👉
# Lifetime of global variables is until execution of program. Once execution of
# program is completed these variables delete from memory

# a=100
# b=200
# def fun1():
#     print(f"a is a global varible{a}")
#     print(f"b is a global variable{b}")
# def fun2():
#     print(a)
#     print(b)
# def main():
#     fun1()
#     fun2()
#     print(f"value of a:{a}")
#     print(f"print value of b:{b}")
# main()

# adding ,sub,div and mult of two number using Global
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# def add():
#     print(f" sum is {a+b}")
# def sub():
#     print(f"sub is {a-b}")
# def div():
#     print(f"div is {a/b}")
# def mult():
#     print(f"mult is {a*b}")
# def main():
#     add()
#     sub()
#     div()
#     mult()
# main()

# 👉Global keyword
# ⭐global and nonlocal keyword
# a=5
# def fun():
#     b=7
#     global a
#     a=a+3
#     print(a)
#     def fun1():
#         nonlocal b
#         b=b+3
#         print(b)
#     fun1()
# fun()

# x=100
# def fun1():
#     global x
#     x=500
#     print(x)
# def fun2():
#     print(x)
# def main():
#     print(x)
#     fun1()
#     fun2()
# main()

# Finding area of triangle using global keyword
# base = None
# height = None
# def read():
#     global base,height
#     base=float(input("Enter value:"))
#     height=float(input("Enter value:"))
# def area():
#     a=0.5*base*height
#     print(f"area is {a:.2f}")
# def main():
#     read()
#     area()
# main()

# x=100
# def fun1():
#     x=200
#     print(f"local variable x={x}")
#     g=globals()
#     print(f"globals variable x={g['x']}")
# def main():
#     fun1()
# main()

# 👉 nested function (function within function is called Nested function)
# def fun1():
#     print("outer function")
#     def fun2():
#         print("Inner function")
#     def fun3():
#         print("inner function")
#     fun2()
#     fun3()
# # def main():
# fun1()
# # main()

# Making a calculator using Nested function
# def calcutor():
#     n1=int(input("enter the value:"))
#     n2=int(input("enter the number:"))
#     opr=input("enter operator:")

#     def add():
#         print(f"sum of numbers{n1+n2}")

#     def sub():
#         print(f"sub of numbers{n1-n2}")

#     def mult():
#         print(f"multi of numbers{n1*n2}")

#     def div():
#         print(f"div of numbers{n1/n2:.2f}")

#     if opr=="+":
#         add()
#     elif opr=="-":
#         sub()
#     elif opr=="*":
#         mult()
#     elif opr=="/":
#         div()
# calcutor()

# 👉None local variable same functionality as global variable
# x=100
# def fun1():
#     y=200
#     def fun2():
#         z=300
#         print(f"local variable z={z}")
#         print(f"local variable y={y}")
#         print(f"global variable x={x}")
#     def fun3():
#         k=500
#         print(f"local variable k={k}")
#         nonlocal y
#         y=400
#         print(f"local variable y={y}")
#     print(f"local varible y={y}")
#     def fun4():
#         l=900
#         print(l)
#         print(y)
#     fun2()
#     print(f"local varible y={y}")
#     fun3()
#     fun4()
# def main():
#     fun1()
# main()

# def welcome():
#     return "Krishna"
# wel=welcome()
# del welcome
# print(wel)

# 👉closure

# def outer():
#   x=3
#   def inner():
#     y=3
#     result=x+y
#     return result
#   return inner
# a=outer()
# print(a())

# 👉Decorator

# def decor(fun):
#     def inner():
#         a=fun()
#         add=a+5
#         return add
#     return inner
# @decor
# def num():
#     return 10
# # result_fun=decor(num)
# print(num())

# def decor(fun):
#     def inner():
#         a=fun()
#         add=a+5
#         return add
#     return inner

# def num():
#     return 10
# result_fun=decor(num)
# print(result_fun())


# # using normal function check a student fail or pass from a list, pass mark is 33.
# def result(marks):
#     for m in marks:
#         if m>=33:
#             pass
#         else :
#             print("FAIL")
#             break
#     else:
#         print("PASS")
# result([50,40,36,55])

# def decor_result(result_function):
#     def distinction(marks):
#         for m in marks:
#             if m>=75:
#                 print("distinction")
#         result_function(marks)
#     return distinction
# @decor_result
# def result(marks):
#     for m in marks:
#         if m>=33:
#             pass
#         else :
#             print("fail")
#             break
#     else:
#         print("pass")
# result([50,40,80,75])

# def drawline(func):
#     def newdisplay():
#         print("*"*40)
#         func()
#         print("*"*40)
#     return newdisplay
# @drawline
# def display():
#     print("Python Programming")
# display()

# def function1():
#     print("hello")
# def function2(func):
#     print("Krishan Damodaram")
#     func()
# function2(function1)

# ⭐Lambda function
# def main():
#      a=lambda:print("without arguments without return value")
#      a()
#      a()
#      a()
#      add=lambda a,b:a+b #lambda with arguments and return values
#      sub=lambda a,b:a-b
#      r1=add(10,20)
#      r2=sub(10,5)
#      print(r1,r2)
# main()

# lamda function⭐
# a=lambda c:print(c)
# a(5)

# a=lambda c,d:c+d
# print(a(5,4))

# a=lambda c:print(c)
# b=a(5)
# print(a)

# add= lambda x=10:(lambda y:x+y)
# a=add()
# print(a(20))

# def show(a):
#     print(a(8))

# show (lambda x:x)

# def add():
#     y=20
#     return (lambda x: x+y)
# a=add()
# print(a(10))

# 🤖Object orinted programming🤖👉
# Instance variable
# 1.using objectname.variblename
# 2.setattr and getattr
# 3.using constructor

# 1.using objectname.variable_name
# class student:
#     pass
# stud1=student()
# stud1.__dict__
# stud1.rollno= 101
# stud1.name='naresh'
# print(stud1.rollno,stud1.name)
# print(stud1.__dict__)
# print(type(stud1))
# print(type(stud1.name))
# print(type(stud1.rollno))

# 2.using setattr and getattr
# class player:
#     pass
# p1=player()
# p1.__dict__
# setattr(p1,"name","rahul")
# setattr(p1,"run",50)
# print(p1.__dict__)
# print(getattr(p1,"name"),getattr(p1,"run"))

# Using constroctor without arguements
# class employee:
#     def __init__(self):
#         self.empno=None
#         self.empname=None
#         self.empsalary=None
# emp1=employee()
# emp1.empno=101
# emp1.empname="naresh"
# emp1.empsalary=5000
# print(emp1.empno,emp1.empname,emp1.empsalary)

# Using constructor with arguements
# class product:
#     def __init__(self,pname,pprice):
#         self.prodname=pname
#         self.prodprice=pprice
# prod1=product("monitor",5000)
# prod2=product("keyboard",500)
# print(prod1.prodname,prod1.prodprice)
# print(prod2.prodname,prod2.prodprice)

# method
# instance method
# class Robo:
#     def talk(self):
#         print("Robo talk")
# robo1=Robo()
# robo1.talk()

# Write a calculator program using instance variable
# class calculator:
#     def __init__(self,n1,n2):
#         self.num1=n1
#         self.num2=n2
#     def add(self):
#         return self.num1 + self.num2
#     def sub(self):
#         return self.num1 - self.num2
# def main():
#     calc1=calculator(10,20)
#     res1=calc1.add()
#     res2=calc1.sub()
#     print(res1,res2)
# main()

# Write a program to find area of triangle
# class triangle:
#     def __init__(self):
#         self.base=0.0
#         self.height=0.0
#     def set_data(self,b,h):
#         self.base=b
#         self.height=h
#     def find_area(self):
#         return 0.5*self.base*self.height
# def main():
#     t1=triangle()
#     t2=triangle()
#     t1.set_data(1.2,1.3)
#     area1=t1.find_area()
#     t2.set_data(1.4,1.5)
#     area2=t2.find_area()
#     print(f"area of triangel1 is {area1}")
#     print(f"area of triangle2 is {area2:.2f}")
# main()
# private members
# class A:
#     def __init__(self):
#         self.__x=100
#         self.y=20
# def main():
#     obje1=A()
#     print(obje1.y)
# main()

# class date:
#     def __init__(self):
#         self.__dd=0
#         self.__mm=0
#         self.__yy=0
#     def date_print(self):
#         print(self.__dd,self.__mm,self.__yy)
# def main():
#     d1=date()
#     d1.date_print()
# main()

# if i want to asin value to self.__dd,self.__mm and self.__yy

# class date:
#     def __init__(self):
#         self.__dd=0
#         self.__mm=0
#         self.__yy=0
#     def date_print(self):
#         print(self.__dd,self.__mm,self.__yy)
#     def set_date(self,d,m,y):
#         self.__dd=d
#         self.__mm=m
#         self.__yy=y
# def main():
#     d1=date()
#     d1.date_print()
#     d1.set_date(10,8,2200)
#     d1.date_print()
# main()

# ⭐
# class student:
#     course="Python"
#     def __init__(self,sname,sroll):
#         self.__name=sname
#         self.__roll=sroll
#         # self.student_info=self.student_info()
#     def student_info(self):
#         print(self.__name,self.__roll,student.course)
# def main():
#     std1=student(101,"Upendra")
#     std2=student(103,"Krishna")
#     std1.student_info()
#     std2.student_info()
# main()

# ⭐
# class Collage:
#   def __init__(self):
#     self.name = 'Yale University'
#     self.show()
#     self.course = self.Course()
#   def show(self):
#     print('College/University:',self.name)
#   class Course:
#     def __init__(self):
#       self.name = 'MBA'
#       self.seats = 105
#       self.disp()
#     def disp(self):
#       print('Course Name:',self.name,' Seats:',self.seats)
# college = Collage()

# class Account:
#     def __init__(self):
#         self.__accNo=None
#         self.__accNa=None
#         self.__accbalance=None
#     def set_data(self,a,cn,b):
#         self.__accNo=a
#         self.__accNa=cn
#         self.__accbalance=b
#     def deposit(self,t):
#         self.__accbalance=self.__accbalance+t
#     def withdwral(self,t):
#         if t<self.__accbalance:
#             self.__accbalance=self.__accbalance-t
#         else:
#             print("insuficient balance")
#     def print_account(self):
#         print(f"{self.__accNo},{self.__accNa},,{self.__accbalance}")
# def main():
#     acc1=Account
#     acc1.set_data(100,"naresh",5000)
#     acc1.print_account()
#     acc1.deposit(2000)
#     acc1.print_account()
# main()

# 👉 Class level variable
# class student:
#     college_name="NIT"
#     def __init__(self,r,n):
#         self.__rollno=r
#         self.__name=n
#     def print_student(self):
#         print(self.__rollno,self.__name,student.college_name)
# def main():
#     stud1=student(101,"Rama")
#     stud2=student(102,"suresh")
#     stud1.print_student()
#     stud2.print_student()
# main()

# 👉class level method
# class Q:
#     def m1(self):
#         print("object level method")
#     @classmethod
#     def m2(cls):
#         print("class levl method ")
# print(Q.m2())
# obj=Q()
# print(obj.m1())

# class D:
#     c=200
#     f=500
#     @classmethod
#     def print_data(cls):
#         print(D.c,D.f)
# D.print_data()

# to access private data using class level method
# class A:
#     __x=100
#     @classmethod
#     def m1(cls):
#         print(A.__x)
# A.m1()

# static method
# class math:
#     @staticmethod
#     def power(num,p):
#         return num**p
#     def iseven(num):
#         return num%2==0
#     def isodd(num):
#         return num%2!=0
# print(math.power(5,2))
# math.iseven(6)
# math.isodd(8)

# Inheritance method level
# class A:
#     def m1(self):
#         print("m1 is method of class A")
# class B(A):
#     def m2(self):
#         print("m2 is method of class B")
# def main():
#     obje1=B()
#     obje1.m1()
#     obje1.m2()
# main()

# Inheritate object level varible
# class A:
#     def __init__(self):
#         self.x=100
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y=200
# def main():
#     obj=B()
#     print(obj.x)
#     print(obj.y)
# main()

# ⭐ Single level inheritance

# class A :
#     def parent(self):
#         print("parent propotries and behavior")
# class B(A):
#     def child(self):
#         print("child have method of parent and his own")
# obj1=B()
# obj1.parent()
# obj1.child()

# class parent:
#     def __init__(self):
#         self.x=100
#         print(self.x)
# class child(parent):
#     def __init__(self):
#         self.y=200
#         super().__init__()
# def main():
#     obj1=child()
#     print(obj1.x,obj1.y)
# main()

# class person:
#     def __init__(self):
#         self.__name=None
#     def set_name(self,n):
#         self.__name=n
#     def get_name(self):
#         return self.__name
# class student(person):
#     def __init__(self):
#         super().__init__()
#         self.__rollno=None
#         self.__course=None
#     def set_rollno(self,r):
#         self.__rollno=r
#     def set_course(self,c):
#         self.__course=c
#     def get_rollno(self):
#         return self.__rollno
#     def get_course(self):
#         return self.__course
# def main():
#     stud1=student()
#     stud1.set_name("suresh")
#     stud1.set_rollno("101")
#     stud1.set_course("python")
#     print(f"rollno: {stud1.get_name()}\n name: {stud1.get_rollno()}\n course: {stud1.get_course()}")
# main()

# Multilevel inheritance
# class person:
#     def __init__(self):
#         self.__name=None
#     def set_name(self,n):
#         self.__name=n
#     def get_name(self):
#         return self.__name
# class employee(person):
#     def __init__(self):
#         super().__init__()
#         self.__empno=None
#     def set_empno(self,e):
#         self.__empno=e
#     def get_empno(self):
#         return self.__empno
# class salariedemp(employee):
#     def __init__(self):
#         super().__init__()
#         self.__sal=None
#     def set_sal(self,s):
#         self.__sal=s
#     def get_sal(self):
#         return self.__sal
# def main():
#     emp1=salariedemp()
#     emp1.set_name("naredh")
#     emp1.set_empno(104)
#     emp1.set_sal(5000)
#     empname=emp1.get_name()
#     empno=emp1.get_empno()
#     empsal=emp1.get_sal()
#     print(empname,empno,empsal)
# main()

# Multiple inheritance
# class A:
#     def __init__(self):
#         self.x=100
# class B:
#     def __init__(self):
#         self.y=200
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         B.__init__(self)
#         self.z=300
# def main():
#     obj=C()
#     print(obj.x,obj.y,obj.z)
# main()

# Overriding
# class person:
#     def __init__(self):
#         self.__name=None
#     def read(self):
#         self.__name=input("Enter your name")
#     def print_info(self):
#         print(f"Name:{self.__name}")
# class employee(person):
#     def __init__(self):
#         super().__init__()
#         self.__salary=None
#     def read(self):
#         super().read()
#         self.__salary=float(input("enter salary"))
#     def print_info(self):
#         super().print_info()
#         print(f"salary:{self.__salary}")
# class Customer(person):
#     def __init__(self):
#         super().__init__()
#         self.__creadit_limit=None
#     def read(self):
#         super().read()
#         self.__credit_limit=float(input("enter credit limit"))
#     def print_info(self):
#         super().print_info()
#         print(f"creadit_limit:{self.__creadit_limit}")
# def main():
#     e1=employee()
#     e1.read()
#     e1.print_info()
#     c1=Customer()
#     c1.read()
#     c1.print_info()
# main()
