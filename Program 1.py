#WAP to take input from a user for name mobile number and address
#(we should even validate the inputs by user)
n=1
while(n==1):
 name,no,addr=input('\nEnter Your Name: '),input('Enter Your Mobile No: '),input('Enter Your Address: ')
 if(name.isalpha() and no.isdigit() and addr.isalnumspc()==True):
     print('\nName: ',name.capitalize(),'\nMobile No: ',no,'\nAddress: ',addr.capitalize())
     n=0
 else:
     print('\nThe Given Input is Incorrect: ')
     n=1
     

#Note: Ask about how to do it individually
#how to make space as 
