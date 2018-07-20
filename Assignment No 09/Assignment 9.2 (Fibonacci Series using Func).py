#Fibonacci Series Using Function Type 2
def Fibonacci(no):
 First_Element,Second_Element=0,1
 print('''0
1''')
 for i in range (1,no-1):
     Fibo_Series=First_Element+Second_Element
     print(Fibo_Series)
     First_Element,Second_Element=Second_Element,Fibo_Series

num=int(input('How Many Elements: '))
Fibonacci(num)



'''
def Fibonacci(no):
 a,b=0,1
 print(a)
 print(b)
 for i in range (1,no-1):
     c=a+b
     print(c)
     a,b=b,c

num=int(input('How Many Elements: '))
Fibonacci(num)'''

'''Using Type 1
def Fibonacci(no):
 a,b=0,1
 print(a)
 print(b)
 for i in range (1,no-1):
     c=a+b
     a,b=b,c
 return c
num=int(input('How Many Elements: '))
print(Fibonacci(num))'''
