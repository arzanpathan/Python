#WAP to combine two dictionary by adding common keys.
'''
Example: D1={'a':10,'b':20,'c':30,'d':40}
D2={'c':12,'e':15,'f':18}

OUTPUT: D={'a':10,'b':20,'c':42,'d':40,'e':15,'f':18}
'''

Dictionary_Output,First_Dictionary,Second_Dictionary={},{},{}
First_Dictionary.setdefault(input('Enter a Word in First_Dictionary: '),int(input('Enter a Value in First_Dictionary: '))),First_Dictionary.setdefault(input('Enter a Word in First_Dictionary: '),int(input('Enter a Value in First_Dictionary:'))),First_Dictionary.setdefault(input('Enter a Word in First_Dictionary: '),int(input('Enter a Value in First_Dictionary:'))),First_Dictionary.setdefault(input('Enter a Word in First_Dictionary: '),int(input('Enter a Value in First_Dictionary:'))),Second_Dictionary.setdefault(input('Enter a Word in Second_Dictionary: '),int(input('Enter a Value in Second_Dictionary: '))),Second_Dictionary.setdefault(input('Enter a Word in Second_Dictionary: '),int(input('Enter a Value in Second_Dictionary:'))),Second_Dictionary.setdefault(input('Enter a Word in Second_Dictionary: '),int(input('Enter a Value in Second_Dictionary:')))
for each in First_Dictionary.keys():
 if each in Second_Dictionary.keys():
     Dictionary_Output.setdefault(each,First_Dictionary.get(each)+Second_Dictionary.get(each))
     del Second_Dictionary[each]
 else:
     Dictionary_Output.setdefault(each,First_Dictionary.get(each))
Dictionary_Output.update(Second_Dictionary)
print(Dictionary_Output)

#Note: Never delete a dictionary or part of it since it can be use by the user
'''
D,D1,D2={},{},{}
D1.setdefault(input('Enter a Word in Dictionary 1: '),int(input('Enter a Value in Dictionary 1: '))),D1.setdefault(input('Enter a Word in Dictionary 1: '),int(input('Enter a Value in Dictionary 1:'))),D1.setdefault(input('Enter a Word in Dictionary 1: '),int(input('Enter a Value in Dictionary 1:'))),D1.setdefault(input('Enter a Word in Dictionary 1: '),int(input('Enter a Value in Dictionary 1:'))),D2.setdefault(input('Enter a Word in Dictionary 2: '),int(input('Enter a Value in Dictionary 2: '))),D2.setdefault(input('Enter a Word in Dictionary 2: '),int(input('Enter a Value in Dictionary 2:'))),D2.setdefault(input('Enter a Word in Dictionary 2: '),int(input('Enter a Value in Dictionary 2:')))
for each in D1.keys():
 if each in D2.keys():
     D.setdefault(each,D1.get(each)+D2.get(each))
     del D2[each]
 else:
     D.setdefault(each,D1.get(each))
D.update(D2)
print(D)
'''

'''
D1={'a':10,'b':20,'c':30,'d':40}
D2={'c':12,'e':15,'f':18}
D={}

for each in D1.keys():
 if each in D2.keys():
     D.setdefault(each,D1.get(each)+D2.get(each))
     del D2[each]
 else:
     D.setdefault(each,D1.get(each))
D.update(D2)
print(D)

'''
'''
if (each in D1.keys())==(each1 in D2.keys()) :
 D=D1.get(each)+D2.get(each1)
print(D)
'''



