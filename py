python practical:

1A:create a program that that ask the user to enter their name and age and also calculate and find the year when he/she will turn 100 years.

name = input("Enter your Name:")
age = int(input("Enter your age:"))
year = str(2024 - age + 100)
print(name + ", you will be 100 years old in " + year)


1B:create a program to ask input from user and find the number is even or odd


A=int(input("Enter any number:"))
if A%2==0:
    print("it is an even number")
else:
    print("it is an odd number")


1C:write a python program to generate Fibonacci series


a=int(input("Enter any number:"))
x=0
y=1

for n in range(0,a):
    if (n<=1):
        c=n
    else:
        c=x+y
        x=y
        y=c
        print(c)

        

1D:write a function that reverse the user define input.


def revnum(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = rem + sum * 10
        num = num // 10
    return sum

num = int(input("Enter any number: "))
print("Reverse number is:", revnum(num))


1E:write a python program to check the input is an Armstrong number or not,
   and also find it is Palindrome or not


def armstrong(num):
    sum1=0				 
    temp=num				
    while temp>0:			         
        digit=temp%10	
        sum1=sum1+digit**3		
        temp//=10			
    if num==sum1:			
        print(num,"is a armstrong")	
    else:			
        print(num,"not a armstrong")

num=int(input("entre any number:"))
armstrong(num)

print("To check palindrome")

def palindrom(num1):					
    temp=num1						
    sum=0						
    while(temp!=0):						
        rem=temp%10					
        sum=sum*10+rem					
        temp=temp//10
    if(num1==sum):
        print("the number is a palindrome")
    else:
        print("the number is not a palindrome")

num1=int(input("Enter any number:"))
palindrom(num1)


1F:write a program to find factorial of a given number.

print("Name:Aryan 031")
def fact(n):
    if(n==1):
        return 1
    elif(n<0):
        print("factorial does not exist for nagetive number")
    else:
        return(n*fact(n-1))

n=int(input("enter any number:"))
print("factorial of given number is :",fact(n))



2A:write a function to find whether the character is a vowel or not.


def letter(char):
    if char in ('a','A','e','E','I','i','o','O','u','U'):
        print("It is a vowal")
    else:
        print("It is not a vowal ")
char=input("Enter any charater:")
letter(char)


2B: define a function that computer the length of a given list or string.


def string(st):
    count=0
    for char in st:
        count+=1
    return count
st=input("Enter the string values:")
print(string(st))


2C:Define a histogram:
	****
	*********
	*******
print("Name:Aryan 031")
def histogram(input):
    for i in range(len(input)):
        print(input[i]*'*')
L=[4,9,7]
histogram(L)


3A:write a program to check whether the sentence is pangram or not.

print("Name:Aryan 031")
def fun (str):
    a="abcdefghijklmnopqrstuvwxyz"
    for char in a:
        if char not in str.lower():
            return False
    return True
str=input("enter any sentance:")
if(fun(str)==True):
    print("the string is pangram")
else:
    print("the string is not pangram")



OTHER METHOD:


print("Name:Aryan 031")
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("the quick brown fox jumps over the lazy dog"))
print(ispangram("hello world"))



3B: take a list and write a program to point all element of list that are less then 5.


print("Name:Aryan 031")
a=[1,2,3,4,55,6,7,8,8,9,4]
for i in a:
    if i<5:
        print("the number is less then 5")
        print(i)
    

4a:WRITE A PROGRAM TO TAKE TWO LIST AND RETURN TRUEIF THEY HAVE ATLEAST ONE COMMON NUMBER.

print("Name:Aryan 031")
def common_data (list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[6,7,8,9]))
print(common_data([4,6,8,10],[10,8,7,6]))


4B:WRITE A PYTHON PROGRAM TO PRINT A SPECIFIED LIST AFTER REMOVING 0th,2nd,4th,and 5th element.

print("Name:Aryan 031")
color=['red','green','white','black','pink','yellow']
color=[x for(i,x) in enumerate(color) if i not in (0,2,4,5)]
print(color)


4C:write a python program to clone or copy list.

print("Name:Aryan 031")
orignal_file=[10,20,30,40]
new_file=list(orignal_file)
print(orignal_file)
print(new_file)



5a:write a python program to short a dictionary by value.


print("Name:Aryan 031")
import operator
d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print ("original dictinary")
t=sorted(d.items(), key = operator.itemgetter(0))
print("dictionary in ascending order by values:",t)
t=sorted(d.items(), key = operator.itemgetter(0),reverse=True)
print("dictionary is desending order:",t)



5b:write a python program to concatenate two dictionaries to create  a new one.


print(Name:Aryan 031")
dic1={1:10 ,2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


 
5c:write a python program to sum all the item in a dictionary .


print("Name:Aryan 031")
m={"data":1, "data2":4, "data3":1}
print(sum(m.values()))



6a:write a python program to read on entire text.



f=open('6a.txt','r')
t=f.read()
print(t)
f.close()



6b:



f = open('6a.txt','a+')
f.write('This line is been appended.practical no 6-B\n')
f =open('6a.txt','r')
t =f.read()
print(t)
f.close()


6c:write a python program to append text to a find and display the text.

f = open('6a.txt', 'r')
t=f.readlines()
print(t[-1])
f.close()


7a:write a python program to read last "n"  line of a file.


class student:
    def info(self,student_Name,student_rollno):
        print("Name:",student_Name , "Roll no:",student_rollno)

obj=student()
obj.info("Aryan",31)
obj.info("sumit",131)
obj.info("misa",133)
obj.info("komal",120)



7B:implement the concept the inheritance using python.

print("Name:Aryan 031")
class st:
    def s1(self):
        print("base class")
class st1(st):
    def s2(self):
        print("derived class")

t=st1()
t.s1()
t.s2()




8a:write a program to implement exception handling.


print("Name:Aryan 031")
try:
    num=int(input("Enter the number:"))
    re=100/num
except(ValueError,ZeroDivisionError):
    print("something wrong")
else:
    print("the result is:",re)
        


9a:write a program to configure the widget various option like
bg=red, family="time", size=20




import tkinter as tk
win = tk.Tk()
win.title("Practical 9A")

def redClick():
    label.config(text="Helvetica Font")
    label.config(bg= "red")
    label.config(font=("Helvetica", 26))

def greenClick():
    label.config(text="Cambria Font")
    label.config(bg= "green")
    label.config(font=("Cambria", 18))

def yellowClick():
    label.config(text="Arial Font")
    label.config(bg= "yellow")
    label.config(font=("Arial", 14))

label = tk.Label(win, text="Practical 9A", bg="white")
label.pack()

label = tk.Label(win, text="Name:denzil 06", bg="pink")
label.pack()

B1=tk.Button(win, text="RED CLICK", relief="raised", command=redClick)
B1.pack(side="left")

B2=tk.Button(win, text="GREEN CLICK", relief="raised", command=greenClick)
B2.pack(side="left")

B3=tk.Button(win, text="YELLOW CLICK", relief="raised", command=yellowClick)
B3.pack(side="left")

win.mainloop()
