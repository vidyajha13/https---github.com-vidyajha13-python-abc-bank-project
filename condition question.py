#find the greatest of three numbers
'''a=int(input("enter first number:  "))
b=int(input("enter second number: "))
c=int(input("enter third number:  "))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")'''
# program calculates the sum of two numbers based on the operator entered by the user
'''a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /,//,**): ")
if operator == '+':
    print("The sum of", a, "and", b, "is", a + b)
elif operator == '-':
    print("The difference of", a, "and", b, "is", a - b)
elif operator == '*':
    print("The product of", a, "and", b, "is", a * b)
elif operator == '/':
    print("The quotient of", a, "and", b, "is", a / b)    
elif operator == '//':
    print("The floor division of", a, "and", b, "is", a // b)
elif operator == '**':
    print("The exponentiation of", a, "and", b, "is", a ** b)
else:
    print("Invalid operator. Please enter one of +, -, *, /, //, or **.")'''
#login system 
'''username=input("enter username  " )
pas = input ("enter password ")
if username == "vidya" and pas == "1234" or username == "neha" and pas == "abcd":
    print("Login successful")
else:
    print("Login failed. Please check your username and password.")'''
# Power of a number
'''a= int(input("Enter a number: "))
x=a**2
if x>=100 and x<1000:
    print("modarate power")
elif x>=1000:
    print("high power")
else:
    print("low power")'''
'''a = int(input("Enter a number: "))
b= int(input("Enter another number: "))
if a**b>1000 and a!=b and a%2==0 or b%2==0:
    print("vaild")
else:
    print("not valid")'''

'''n=input ("what is your name  ")
a= int(input("enter your age "))
if a>=18 :
    print(f"{n} you are eligible to vote")
    

else:
    print(f"{n} you are not eligible to vote and your age is {a} so you can vote after {18-a} years")'''
'''year = int(input("Enter the year: "))
if year%100==0 and year%400==0:
    print(f"{year} is a leap year")
elif year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''

'''n=int(input ("Enter a  range"))

sum=1
for i in range(1, n+1):
    sum = sum * i
    print(f"{sum}")'''
'''n=int(input("Enter a number: "))
even = 0
odd = 0
for i in range(1, n+1):
    
    
    if i % 2 == 0:
        even += i
        

              
    else:
        odd += i

        
print(even ,  odd)
n = int(input("Enter a number: "))
#even_numbers = []
#odd_numbers = []
even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
       # even_numbers.append(i)
        even_sum += i
    else:
       # odd_numbers.append(i)
        odd_sum += i

print(f" Sum: {odd_sum}")
print(f" Sum: {even_sum}")'''
'''fact=int(input("enter a number" ))
count=0
for i in range(1, fact+1):
    if fact % i == 0:
        count =count + 1
        
if count == 2:
    print(f"{fact} is a prime number")
else:
    print(f"{fact} is not a prime number ") '''
'''n="naman"
b=""
for i in range(len(n)-1, -1, -1):
    b= b + n[i]
if n == b:
    print("it is a palindrome")
else:
    
    
    print("it is not a palindrome")'''
'''n=input("Enter a string: ")
d=0
s=0
sc=0
for i in n:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        s+=1
    else:
        sc+=1
print(f"Digits: {d}, Alphabets: {s}, Special characters: {sc}")
print(dir(str))  
    
import random
number = random.randint(1, 100)
tr= 0
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == number:
        tr += 1
        print("Congratulations! You've guessed the number correctly")
        print(f"You took {tr} tries to guess the number.")
        break
    elif guess < number:
        tr += 1
        print("Your guess is too low. Try again.")
        
    elif guess > number:
        tr += 1
        print("Your guess is too high. Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    if tr >= 10:
        print("You have exceeded the maximum number of tries. The correct number was", number)
        breaka=[12,13,24,45,90]
a.append(12.45)
print(a)
a.extend([12, 13, 14, 15])
print(a)
a.insert(2, 100)
print(a)
b=a.index(12)
print(b)
c=a.count(12)
print(c)
a.sort()
print(a)
a.reverse()
print(a)
a.copy()
print(a)
a.remove(12)
print(a)
a.pop(2)
print(a)
a.clear()
print(a)
a=[-12,13.5,24,-23.89,67,9,56,0,-45,78,-90]
b=0
c=0 
for i in a:
    if i<0:
        
        b=b+1
        print(f"Negitive number is {i}") 
    else:
        
        c=c+1
        print(f"Positive number is {i}")
        
print(f"list is {a}\nTotal Positive number is {c}\nTotal negitive number is {b} ")
a=[12,13,24,45,90]
sum=0
for i in a:
    sum+=i
b=sum/len(a)
print(f"value is {a}\n sum of all value is {sum}\n mean is(sum of all value \ no. of value )is {b}")'''

'''a=[12,23,45,87,890,2345,67,999]
l=a[0]
b=0
sl=0
t=0
for i in range(len(a)):

    if a[i]>l:
         t=sl
         sl=l
         l=a[i]
         b=i

    elif a[i]>sl:
        t=sl
        b=i
        sl=a[i]
        b=i
        
         
print(f"Greatest no.is {l, b} and secord greatest is ={sl ,t}"  ) '''
'''l=[12, 13, 24, 5, 90]
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        
        continue
    else:
        print("not sorted")
        break 
else:
    print("sorted")'''
'''a=(12, 13, 24, 5, 90)
for i in range (len(a)):
    print(a[i],   i)
for i in a:
    print(i)'''


'''s={"vidya",7,8,10,45,34,6,3}
s.add("jha")
print(s)
s.remove("vidya")
print(s)
s.discard(7)
print(s)
s.pop()
print(s)
s.clear()
print(s)
d={}
print(type(d))'''
'''a={1, 2, 3, 4, 5}
b={3,5,7,8}
print(a|b)
print(a & b)
print(a - b)
print(b-a)
print(a ^ b)'''
'''a={1:100, 2:34, 3:300, 4:400}
for i in a:
    print(f"{i} : {a[i]}")
    print(f"{i}  {a.get(i)}")
    print(a.items())
    print(a.setdefault(2, 100))
    print(a.update({3: 500}))
    print(a.items())'''
'''d1 = {'name': 'vidya', 'age': 20, 'city': 'noida'}
d2 = {'n': 'neha', 'a': 22, 'c': 'delhi'}
for i in d2:
    d1[i] = d2[i]
print(d1)'''
'''d1={12:100, 2:34, 3:300, 4:400}
sum=0
s2=0
for i in d1:
    sum+= i
    s2+= d1[i]
print(f"sum of keys is {sum} and sum of values is {s2}")'''
a={1:233, 2:34, 3:300, 4:400}
d={1:456,5:789, 6:123,2:100}
for i in d:
    if i in a:
        a[i] += d[i]
    else:
        a[i] = d[i]
print(a)