import random 
score1=0
while True:
    user1=input('Enter any number between 1 to 6(write quit for close the game): ')
    cpu=random.randint(1,6)
    if user1==str(cpu):
        print('cpu:',cpu)
        print('match found.......')
        score1+=5
    elif user1=='quit':
        break
    elif int(user1)>6:
        print('Enter number between 1 to 6...')
    else:
        print('cpu:',cpu)
        print('No match found....')
        score1+=0
print('Your score is',score1)



