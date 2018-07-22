#Lambda Func To Calc cube of a no
a=int(input('Enter a Number To Cube: '))
print('Cube',(lambda x:x**3)(a))

#Lambda function to filter a list in order to get no divisible by 3&5 only

L=[1,3,5,10,12,15,25,18,20,21,30]

Filter_3_5=[x for x in filter(lambda a:True if a%3==0 and a%5==0 else False,L)]
print('Filter Divisible by 3 and 5: ',Filter_3_5)
 
#Lambda Func to get sum of 4 numbers to implement for List
l1,l2,l3,l4=[1,2,3],[4,5,6],[1,2,3],[4,5,6]
L_lam=[x for x in map(lambda a,b,c,d:a+b+c+d,l1,l2,l3,l4)]
print('Sum of Four Numbers: ',L_lam)

#Create a Dictionary having Key as number L1 & Value as Square of L2
'''
l1=[7,6,4]
l2=[2,3,5]
output = {7:4,6:9,5:16}
'''
l1=[7,6,4]
l2=[2,3,5]
Lamda_Dict={x:y for x,y in map((lambda a,b:(a,b**2) if a>b else (b,a**2)),l1,l2)}
print('Dict With Key and Square as Value: ',Lamda_Dict)
