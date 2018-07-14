l=[]
temp=0
wo=""
for i in range (5):
 w=input('Enter a Word')
 if(len(w)>temp):
     temp=len(w)
     wo=w
 else:
     temp=temp
 l.append(w)
 print(l)
print(temp)
print(wo)

'''l=[]
temp=0
n=0

for i in range (5):
 w=input('Enter a Word')
 l.append(w)
 print(l)

if(len(a)>temp):
 temp=len(a)
else:
 temp=temp
 n+1
print(a,temp)
'''
