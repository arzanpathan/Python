#WAP to print all odd No's between 13 to 123
print('\nOdd Numbers between 13 to 123\n')
for i in range(13,125,2):
 print(i)

#WAP to print all Natural No's from 100 to 1 using For Loop
print('\nPrint All Natural Numbers from 100 to 1\n')
for j in range(100,0,-1):          #for j in range(100):       
 print(j)                         #print(100-j)   



#WAP to Check whether the given no is prime or not (Prime no means divisible by its own)
   #for k in range(2,no):c=no/k if(c!=1): print('\nIt is Not a Prime No')
print('\nProgram to Check whether the given no is prime or not (Prime no means divisible by its own)')
no=int(input('\nEnter a No: '))

for k in range(2,no):
 if(no%k==0):
     print('It is not a Prime No')
     break
if(k==no-1):
 print('It is a Prime No')


