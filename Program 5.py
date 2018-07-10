#WAP to take two guess input from user and predict whether he has guessed it correct or not give 4 chance to user.
print('Program to take two guess input from user and predict whether he has guessed it correct or not give 4 chance to user')
import random
i=1
while(i<5):
 g1,g2,a=int(input('Guess the No: ')),int(input('Guess the No: ')),random.randint(1, 6)
 print('Random Number: ',a)
 if(g1==a or g2==a):
     print('Guess is Correct')
     i=5
 else:
     print('Try Again')
     i+1
