'''Write a Program to take a Sentence as an input and take a word as input. Calculate how many times the word has occured in the sentence.
'''
#Optimal way
s,n=input('Enter a Sentence').upper(),0
while(n!=n+1):
 w=input('Enter a Word').upper()
 if w in s:
     print('Occurence of Word ',w,': ',s.count(w))
     break
 else:
     print('This Word is Not Present Please Try Again: ')












''' Simple Way
a=input('Enter a Sentence')

b=input('Enter a Word')
s=a.upper()
w=b.upper()
if w in s:
 print('Occurence of Word ',w,': ',s.count(w))
else:
 print('This Word is Not Present')'''
     
