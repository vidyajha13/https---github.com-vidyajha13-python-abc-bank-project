print("hello bharat") #print() function # prints the string "hello bharat" to the console
"""this is a 
multi-line 
comment"""
# This is a single-line
#  comment.
variable_1 = 10    # don't start with a number but number used in after character 
# space not allowed used (_)
# and no special characters allowed like @, #, $, %, etc.
print(variable_1) 
 # variables are storage
variable_2 = 20 #snake_case variable
print(variable_2) 
VidyaJha = 3 #PascalCase variable
print(VidyaJha)
vidyaJha  = 40 #camelCase variable
print(vidyaJha) 
#in variable are store value and this is based on datatype like 
# int, float,complex string, boolean, list, tuple, set, dictionary
a = 10 #int
b = 20.5 #float
c = 1 + 2j #complex
d = "Hello, World!" #string
e = True #boolean
f = [1, 2, 3] #list
g = (1, 2, 3) #tuple
h = {1, 2, 3} #set
i = {"name": "Vidya", "age": 20} #dictionary
print(type(a)) #int
print(type(b)) #float
print(type(c)) #complex
print(type(d)) #string
print(type(e)) #boolean
print(type(f)) #list
print(type(g)) #tuple
print(type(h)) #set
print(type(i)) #dictionary
# type() function is used to check the datatype of a variable
a="A"
print(ord(a))# ord() function returns the Unicode code point of a character
a=65
print(chr(a)) # chr() function returns the string representing a character whose Unicode code point is the integer
a= "Vidya"
print(a[4])# indexing in string
b = a[::-2]# slicing in string
print(b)
num1=10.90
num2=int (float(num1)) # type conversion
print(num2) # converting float to int
name = "Vidya Jha"
age = 20
print(f"My name is {name} and my age is {age}") # f-string for formatting
print("My name is {} and my age is {}".format(name, age)) # format() method for formatting
print("My name is %s and my age is %d" % (name, age)) # old-style formatting
print("My name is", name, "and my age is", age) # concatenation
course= input ("enter your course name: ") # input() function to take input from user
print(course) # print the input value
# Python is a dynamically typed language, so you don't need to declare the type of a variable
a=10
b=3
c=a**b
print(c)# exponentiation operator(power operator) 
a+=30 
a+=10
a-=20 

print(a)
a=12
b=3
print(a<=b) 
print(a==b or a<b) # logical operators
print(not(a==b)) # not operator (true if a is not equal to b)
