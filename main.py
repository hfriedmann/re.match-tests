import time
import re
from re import *

def test():

    main_input = input("> ").casefold()
        #.casefold() == all lower case
    question1 = r'cookie'
            #R == raw.  
    question2 = 'milk'
    if re.match('co.kie', main_input):
        print('yes. it is a cookie, what now?')
        print('works for "CO[any word]KIE')
        # . == any word

    elif re.match('mi+lk', main_input):
        print('ok, milk')
        print('works for Miiiiiiiiiilk')
        # + any number of words

    elif re.search(r'^eat', main_input) and re.search(r'co.kie', main_input):
        print('EAT COOKIE')
        print('works for CO[any word]KIE')
        print('but dont for COOKIE EAT')
        # ^ == first word
        # $ == las word

    elif re.search(r'^drink', main_input) and re.search(r'mi+lk', main_input):
        print('DRINK MILK')
        print('works for Miilk')
        print('but dont for MILK DRINK')

    else:
        print('no. cant do it')
    test()

def startmain():
    print('ROBOTS DINNER')
    print('Try: cookie, eat cookie, milk, drink milk. or others')
    test()

startmain()
