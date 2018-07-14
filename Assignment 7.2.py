'''
Take a Sentence from the user and print only words which are not
in the Excluded List
'''
el,w=input('Enter an Excluded list').split(),input('Enter a Sentence').split()
print(el)
print(w)
for each in el:
 if each in w:
     w.remove(each)

print(' '.join(w))

'''el,w=input('Enter an Excluded list').split(),input('Enter a Sentence').split()
print(el)
print(w)
el.remove(w)
print(w)
s=' '.join(w)
print(s)'''


'''

el,w=input('Enter an Excluded list').split(),input('Enter a Sentence').split()
print(el)
print(w)
n=(len(el))
for i in range (n):
 w.remove(el[i])
print(w)
'''
'''el,w=input('Enter an Excluded list').split(),input('Enter a Sentence').split()
print(el)
print(w)
w.remove(el[1])
print(w)'''
