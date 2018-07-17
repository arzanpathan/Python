#WAP To get Highest Three Value in a Dictionary
'''
Example: D={'a':10,'b':20,'c':42,'d':40,'e':15,'f':18}

OUTPUT:  42,40,20

'''




Highest_Values,Dictionary,n=[],{},0
Dictionary.setdefault(input('Enter a Word in Dictionary: '),int(input('Enter a Value in Dictionary: '))),Dictionary.setdefault(input('Enter a Word in Dictionary: '),int(input('Enter a Value in Dictionary:'))),Dictionary.setdefault(input('Enter a Word in Dictionary: '),int(input('Enter a Value in Dictionary:'))),Dictionary.setdefault(input('Enter a Word in Dictionary: '),int(input('Enter a Value in Dictionary: ')))
print(Dictionary)
while(n!=3):
 Maximum=0
 for each in Dictionary.keys():
     if Dictionary.get(each)>Maximum:
         Maximum=Dictionary.get(each)
         Key_Maximum=each
 Highest_Values.append(Maximum)
 del Dictionary[Key_Maximum]
 n=n+1
print('The Highest Three Values are: ',Highest_Values)





'''
D1,D2,n=[],{},0
D2.setdefault('Maths',int(input('Enter Your Maths Marks: '))),D2.setdefault('Phy',int(input('Enter Your Phy Marks: '))),D2.setdefault('Chem',int(input('Enter Your Chem marks: '))),D2.setdefault('Bio',int(input('Enter Your Bio marks: ')))

print(D2)
while(n!=3):
 Maximum=0
 for each in D2.keys():
     if D2.get(each)>Maximum:
         Maximum=D2.get(each)
         D3=each
 print(Maximum)
 D1.append(Maximum)
 del D2[D3]
 print(D2)
 n=n+1
print('The Highest Three Values are: ',D1)
'''
 

'''D2={}
D2.setdefault('Maths',int(input('Enter Your Maths Marks: '))),D2.setdefault('Phy',int(input('Enter Your Phy Marks: '))),D2.setdefault('Chem',int(input('Enter Your Chem marks: '))),D2.setdefault('Bio',int(input('Enter Your Bio marks: ')))
Maximum,n=0,0
print(D2)
while(n!=len(D2)):
 for each in D2.keys():
     if D2.get(each)>Maximum:
         Maximum=D2.get(each)
     else:
         Maximum=Maximum
 del D2[each]
 n=n+1
 print(D2)
 print(Maximum)
 '''
 


