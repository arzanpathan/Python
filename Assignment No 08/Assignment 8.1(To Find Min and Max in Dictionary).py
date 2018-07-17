#WAP to get max and min value in a dictionary
''' Eg: D={'Maths':78,'Chem':76,'Phy':77,'Mech':67,'Java':72}
    OUTPUT: min:67
            max:78
'''

Marks_Dictionary={}
Marks_Dictionary.setdefault('Maths',int(input('Enter Your Maths Marks: '))),Marks_Dictionary.setdefault('Phy',int(input('Enter Your Phy Marks: '))),Marks_Dictionary.setdefault('Chem',int(input('Enter Your Chem marks: '))),Marks_Dictionary.setdefault('Bio',int(input('Enter Your Bio marks: ')))
Maximum,Minimum=0,999999999
print(Marks_Dictionary)
for each in Marks_Dictionary.values():
 if each>Maximum:
     Maximum=each
     
 if(each<Minimum):
     Minimum=each

print('Maximum Value in a Dctionary: ',Maximum)
print('Minimum Value in a Dctionary: ',Minimum)



#Note: Ask Why else can't be use here
'''
D2={}
D2.setdefault('Maths',int(input('Enter Your Maths Marks: '))),D2.setdefault('Phy',int(input('Enter Your Phy Marks: '))),D2.setdefault('Chem',int(input('Enter Your Chem marks: '))),D2.setdefault('Bio',int(input('Enter Your Bio marks: ')))
Maximum,Minimum=0,999999999
print(D2)
for each in D2.values():
 if each>Maximum:
     Maximum=each
 else:
     Maximum=Maximum
 if(each<Minimum):
     Minimum=each
 else:
     Minimum=Minimum

print('Maximum Value in a Dctionary: ',Maximum)
print('Minimum Value in a Dctionary: ',Minimum)

'''

'''
My Way"Converting Dictionary Values into list"
D2,b,c={'Maths':78,'Chem':76,'Phy':64,'Mech':64,'Java':67},0,999999999
print(D2)
D1=list(D2.values()) 
for each in D1:
 if each>b:
     b=each
 else:
     b=b
 if(each<c):
     c=each
 else:
     c=c

print('Maximum Value in a Dctionary: ',b)
print('Minimum Value in a Dctionary: ',c)
'''     
'''
My Way"Without Converting Dictionary Values into list"
D2,b,c={'Maths':78,'Chem':76,'Phy':64,'Mech':64,'Java':67},0,999999999
print(D2) 
for each in D2.values():
 if each>b:
     b=each
 else:
     b=b
 if(each<c):
     c=each
 else:
     c=c

print('Maximum Value in a Dctionary: ',b)
print('Minimum Value in a Dctionary: ',c)
'''
'''
 if(each==b):
     b=each
  if(each==c):
     c=each
    
'''
