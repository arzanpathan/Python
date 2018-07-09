
###################################
# Armstrong No From 1 to 1000
print('\nArmstrong No From 1 to 1000\n')
for i in range(1,1000):
 s=0
 t=i
 while(i!=0):
     r=i%10
     s=s+(r**3)
     i=i//10
     
 if(s==t):
     print(s)

# PATTERNS
##################################
print('\nFIRST PATTERN\n')
#  $ $ $
#  * * *
#  $ $ $
#  * * *
for i  in range(1,5):
 for j in range(1,4):
     if(i%2==0):
         print('*',end=' ')
     else:
         print('$',end=' ')
 print()


##################################
print('\nSECOND PATTERN\n')
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3

for i in range(1,5):
 for j in range(1,4):
     print(j,end=' ')
 print()


#Write an Optimal Code to check whether the given No is prime or not
print('\nWrite an Optimal Code to check whether the given No is prime or not\n')
no=int(input('\nEnter a No: '))
m=1
if(m==1):
 for i in range(2,8):
     if(no%i==0):
         print('It is Not a Prime No')
         break
 m+1     
else:
    print('It is a Prime No')

