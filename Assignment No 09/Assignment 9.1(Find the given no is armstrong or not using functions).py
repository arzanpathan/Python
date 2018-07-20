#WAP to find whether the given NO is armstrong or NOt using functions

def Armstrong(NO):
 SUM,TEMP=0,NO
 while(NO!=0):
     REMAINDER=NO%10
     SUM+=(REMAINDER**3)
     NO=NO//10
 return SUM==TEMP

no=int(input('Enter a Number: '))
if(Armstrong(no)):
    print('It is an Armstrong Number ')
else:
    print('It is Not an Armstrong Number ')




#Optimal Code (Without using Temp):
'''
def Armstrong(NO):
 SUM=0
 while(NO!=0):
     REMAINDER=NO%10
     SUM+=(REMAINDER**3)
     NO=NO//10
 return SUM

no=int(input('Enter a Number: '))
if(Armstrong(no)==no):
    print('It is an Armstrong Number ')
else:
    print('It is Not an Armstrong Number ')



'''

'''NO=int(input('Enter a Number '))
s=0
t=NO
while(NO!=0):
 r=NO%10
 s+=(r**3)
 NO=NO//10

if(s==t):
 print('It is an Armstrong Number ')
else:
     print('It is NOt an Armstrong Number ')'''
