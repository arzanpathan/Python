#WAP to take 10 inputs from user and print the largest,smallest,total,average(Total/2) out of it
print('WAP to take 10 inputs from user and print the largest,smallest,total,average(Total/2) out of it')
c,b,Total=99999999,0,0
for i in range(10):
 a=int(input('Enter a New No'))
 if(a>b):
     b=a
 else:
     b=b
 if(a<c):
     c=a
 else:
     c=c
 if(a==b):
     b=a
 if(a==c):
     c=a
 Total=a+Total
     
print('Largest Number is: ',b)
print('Smallest Number is: ',c)
print('Sum of all Numbers is: ',Total)
print('Average Number is: ',Total/2)
