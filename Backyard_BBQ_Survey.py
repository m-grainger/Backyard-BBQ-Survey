def start(good = 0, bad = 0, name=''):
    name = welcome_message_check(name)
    good,bad,name = good_or_bad(good,bad,name)

bio = 'yes'

#float assigned to variable below
version_number = (float(1.20))
#use of += operator
version_number += (float(0.01))
print('True or False: Are we running the newest software version?')
#use of NOT operator 
print(not version_number == (float(1.20)))


a_m = '\nConsole application written by:'                         
author = 'matt grainger'
#string assigned to a variable below

version_message = '\nCurrent version number:'
c_m = '\nCopywrite:'

copywrite_year = '2017'
#int assigned to a variable below
copywrite_year = int(copywrite_year)


print(a_m)
print(author.title())
#use of AND operator
#use of if statement

if author == 'matt grainger' and bio == 'yes':
    print('\nMatt is pretty new to this coding stuff- so go easy on him!')
#use of elif conditional statement    
elif author != 'matt grainger' and bio == 'yes':
    print('')
        
print(version_message)
print(version_number)
print(c_m)
print(copywrite_year)


#created (a short) list and used a for loop to iterate through it
w_message = ['\nWelcome to Backyard BBQ\'s Survey System!', 'We look forward to hearing about your experience']
for words in w_message:
    print "%s" % words

#created (a short) tuple and used a for loop to iterate through it    
t_message = ('\nWe will ask you a simple math-related question below.', 'This is to ensure that you are not a bot.')
for words in t_message:
    print "%s" % words

def welcome_message_check(name):
    if name =='':
        name = input('\nWhat is (5 x 2) + ( 6 / 3) - the remainder of (3 / 2)?  \nWrite your answer here: ')
        #HINT the ansewer should be 11
        #use of all operators EXCEPT for +=
        if name == (5*2)+(6/3)-(3%2):
            name = raw_input('\nWhat is your name? '.capitalize())
            return name
        #use of else statement
        else:
            print('The survey will now close')
            exit()
           
              

                            
def good_or_bad(good, bad, name):
    stop = True
    #use of a while loop
    while stop:
        show_score(good, bad, name)
        pick = raw_input('\nQuestion #1: Were you seated promptly?  Please answer yes or no: '.lower())
        if pick =='yes':
            print('\nGlad to hear you were seated promptly!')
            good = (good + 1)
            stop = False
        if pick == 'no':
            print('\nSorry to hear that.  We will speak with the staff about this issue.')
            bad = ( bad + 1)
            stop = False
        stop = True
        pick = raw_input('\nQuestion #2: Did a waiter take your drink order within \n 2 minutes of being seated?  Please answer yes or no: '.lower())
        if pick =='yes':
            print('\nGood to hear that we were able to take your drink order in a timely fashion!')
            good = (good + 1)
            stop = False
        if pick == 'no':
            print('\nSorry to hear that.  Being thirsty is awful.')
            bad = ( bad + 1)
            stop = False
        pick = raw_input('\nQuestion #3: Was your food order taken within 4 minutes of being seated?  Please answer yes or no: '.lower())
        if pick =='yes':
            print('\nAwesome- we always try to take orders as soon as possible!')
            good = (good + 1)
            stop = False
        if pick == 'no':
            print('\nWe apologize for making you wait over 4 minutes to take your food order.')
            bad = ( bad + 1)
            stop = False
        stop = True
        pick = raw_input('\nQuestion #4: Did you enjoy your food and/or drink(s)?  Please answer yes or no: '.lower())
        if pick =='yes':
            print('\nGreat!')
            good = (good + 1)
            stop = False
        #use of OR below
        if pick == 'no' or 'yes':
            print('\nThis is subjective, but we appreciate the feedback nonetheless.')
            bad = (bad + 1)
            good = (good + 1)
            stop = False
        pick = raw_input('\nQuestion #5: Did your check arrive promptly?  Please answer yes or no: '.lower())
        if pick =='yes':
            print('\nWe pride ourselves in taking your money.')
            good = (good + 1)
            stop = False
        if pick == 'no':
            print('\nApologies for not taking your money sooner.')
            bad = ( bad + 1)
            stop = False
            
    score(good, bad, name)        

def show_score(good, bad, name):
    #.format() notation
    print('\n{}, you currently have us rated with ({}, Good) and ({}, Bad) points.'.format(name, good, bad))

def score(good, bad, name):
    if good == 5:
        great_experience(good, bad, name)
    if good >= 3: 
        good_experience(good, bad, name)
    if bad >= 3: 
        sub_par_experience(good, bad, name)
    if bad == 5:
        bad_experience(good, bad, name)
    else:        
        good_or_bad(good, bad, name)


def great_experience(good, bad, name):
    print ('\nIt sounds like you had an excellent time at our restaurant- thanks for your feedback!')
    again(good, bad, name)
def good_experience(good, bad, name):
    print ('\nGlad you had a good time, {}! \nWe will address the issues you brought up.'.format(name))
    again(good, bad, name) 
def sub_par_experience(good, bad, name):
    print ('\nWe apologize, it sounds like you had a sub-par experience, {}. \nAt least we did SOME things right!'.format(name))
    again(good, bad, name)                  
def bad_experience(good, bad, name):
    print ('\nWe apologize, it sounds like you had a bad experience, {}. \nWe will use your feedback to better our staff and service.'.format(name))
    again(good, bad, name)                   

def again(good, bad, name):
    stop = True
    while stop:
        choice = raw_input('\nDo you want to take the survey again?  Please type yes or no ').lower()
        if choice =='yes':
            stop = False
            reset(good, bad, name)
        if choice == 'no':
            print ('\nThank you for taking the survey!')
            stop = False
            exit()
        else:
            print ('\nPlease enter y for YES and n for NO')


def reset(good, bad, name):
    good = 0
    bad = 0
    start(good, bad, name)
        

    

if __name__ == '__main__':
    start()
    
