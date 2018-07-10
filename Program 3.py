#WAP take input from user for factorial (Eg3=3x2x1===6 )
print('\n Program To take Input from User and Give its Factorial\n')
no=int(input('Enter a Number: '))
i=no
while(i!=1):
 no,i=(no*(i-1)),i-1
print('Factorial of a Number is: ',no)
 
