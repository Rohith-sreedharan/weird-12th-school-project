'''
AUTHOR - @rohithaditya
COPY WITH CREDITS
(C) ROHITH SV
'''

import random
answers = ['It is certain', 'It is decidedly so', 'Without adoubt', 'Yes – definitely', 'You may rely on it', 'As I seeit, yes', 'Most likely', 'Outlook good', 'Yes Signs point toyes', 'Reply hazy', 'try again', 'Ask again later', 'Betternot tell you now', 'Cannot predict now', 'Concentrate and askagain', 'Dont count on it', 'My reply is no', 'My sources sayno', 'Outlook not so good', 'Very doubtful']
print(' __ __ _____ _____ _____ ___ ')
print(' | \/ | /\ / ____|_ _/ ____   |   ')
print(' | \ / | / \ | | __ | || |    ')
print(' | |\/| | / /\ \| | |_ | | |  ')
print(' | | | |/ ____ \ |__| |_| |   ')
print(' |_| |_/_/ \_\_____|_____\_____')
print('')
print('')

print('')
print('Hola user, I am the Magic 8 Ball, What is your name?')
name = input()
print('Hoii ' + name)

def Magic8Ball():
    print('Ask me a question.')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    print('I hope that helped!')
    Replay()

def Replay():
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Pleaserepeat.')
    Replay()

Magic8Ball()
