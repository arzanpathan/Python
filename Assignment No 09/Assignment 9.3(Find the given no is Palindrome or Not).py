#To Check the Given No is Palindrome or Not(Using Type 2 Func)
def Palindrome(no):
 reverse_no,value_from_user=0,no
 while(no!=0):
     remainder=no%10
     reverse_no=reverse_no*10+remainder
     no=no//10
 if(value_from_user==reverse_no):
     print('The Given No is Palindrome')
 else:
     print('The Given No is Not Palindrome')

no=int(input('Enter a Number: '))
Palindrome(no)
'''
#Same as above 
def Palindrome(no):
 rev,temp=0,no
 while(no!=0):
     r=no%10
     rev=rev*10+r
     no=no//10
 if(temp==rev):
     print('The Given No is Palindrome')
 else:
     print('The Given No is Not Palindrome')

no=int(input('Enter a Number: '))
Palindrome(no)

'''
'''#To Check the Given No is Palindrome or Not(Using Type 1 Func)
def Palindrome(no):
 rev=0
 while(no!=0):
     r=no%10
     rev=rev*10+r
     no=no//10
 return rev

no=int(input('Enter a Number: '))
if(Palindrome(no)==no):
    print('The Given No is Palindrome')
else:
    print('The Given No is Not Palindrome')
'''















