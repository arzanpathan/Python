#WAP to take an input from user and give Sqr root
# input should be round of
import math
no=float(input('Enter a Number: '))
if((no%1)>=0.5):
 no=math.ceil(no)
else:
 no=math.floor(no)

print(math.sqrt(no))
