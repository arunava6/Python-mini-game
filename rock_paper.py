

# Rock, paper and scissors: 

import random
list1=['rock','paper','scissor']
score1=0
score2=0
print('.........................INSTRUCTION OF THE GAME........................\n')
print()
print('1. You have to enter that how many rounds you want to play....')
print('2. If you win in each round then you get 10 marks....')
print('3. There are 5 negative marks if you lose in any round.......')
print('3. You cannot make spelling mistake during entering your choice....')
print('4. You have to follow the below list to enter your choice.....')
print('Follow it   :',list1)
print()
print()
print('..............LET\'S   START   THE  GAME..................\n')
print()
choice=int(input('How many rounds you want to play (in integers only): '))
print()
i=0
while (i<choice):
    a=input('\nYOUR TURN: ')
    if(a not in list1):
        print('.......Please follow the rules of the game and enter the valid name........')
    else:
        b=random.choice(list1)
        print('CPU: ',b)
        if(a==b):
            print('It\'s draw......')
        elif(a=='rock' and b=='paper'):
            print('You lose....  ')
            score2+=10
            score1-=5
        elif(a=='scissor' and b=='rock'):
            print('You lose.....  ')
            score2+=10
            score1-=5
        elif(a=='paper' and b=='scissor'):
            print('You lose.....')
            score2+=10
            score1-=5
        else:
            print('You win.......')
            score1+=10
            score2-=5
    i+=1
user=score1
cpu=score2
if(score1>score2):
    print('\n......You are the winner of this game........\n')
    print('Your score:', score1)
    print('CPU score:', score2)
elif(score1==score2):
    print('\n.........The match is draw......\n')
    print('Your score:', score1)
    print('CPU score:', score2)
else:
    print('\n........You lose the game.......\n')
    print('Your score:', score1)
    print('CPU score:', score2)
print('\n...................THANK YOU.................\n')


