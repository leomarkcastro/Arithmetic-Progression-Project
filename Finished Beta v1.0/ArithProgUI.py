import ArithProg as AP
from os import system
import sys

console = True

if 'pythonw.exe' in sys.executable:
    console = False

def clear():
    if console:
        system('cls')

def main_menu():
    while True:
        clear()
        print "================================================"
        print '              ARITHMETIC SEQUENCE               '
        print ' ---------------------------------------------- '
        print '   An arithmetic progression is a sequence of   '
        print '   numbers such that the difference of any two  '
        print '         successive members is a constant.      '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   Select Action:                               '
        print '     a) Find the nth term of a sequence         '
        print '     b) Find the change of a sequence           '
        print '     c) Compute the sum of a sequence           '
        print '     d) Generate a sequence list                '
        print '                                                '
        print '     e) Generate a a quick sample               '
        print '                                                '
        print '     z) Quit App                                '
        print '                                                '
        inp = raw_input("\nEnter your (letter of) choice: ").lower().strip()

        print '\n---\n'

        if inp == 'a':
            choice_a()
        elif inp == 'b':
            choice_b()
        elif inp == 'c':
            choice_c()
        elif inp == 'd':
            choice_d()
        elif inp == 'e':
            choice_e()
        elif inp == 'z':
            break


def choice_a():

    def sub_a():
        x1 = x2 = x3= x4 = None
        while True:
            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     a) Find the nth term of a sequence         '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      a) A term and the change per term         '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          change : {0}                          '.format(x3)
                print '                                                '
                print '          Target term : {0}                     '.format(x4)
                print '                                                '


                if x1!=None: pass
                else: x1 = float(raw_input("Enter a number from the sequence: ")); continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")); continue

                if x3!=None: pass
                else:x3 = float(raw_input("What is the change per term of the sequence: ")); continue

                if x4!=None: pass
                else:x4 = int(raw_input("What place in the sequence is the value you are looking is located: ")); continue

                print '------------------------------------------------'
                print '                                                '
                print '   This values builds this sequence:            '
                print '   {0}                                          '.format(AP.generate_list_bycount(x1,x2,x3,10))
                print '                                                '
                print '   The {0}th term of this sequence is: {1}      '.format(x4,AP.compute_nterm(x1, x2, x3, x4))
                print '                                                '
                print '                                                '
                print '                                                '

                raw_input ("---Press enter to continue---")
                break
            except:
                "\n\n=====Wrong input\n======"

    def sub_b():
        x1 = x2 = x3= x4 = x5 = None
        while True:
            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     a) Find the nth term of a sequence         '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      b) Two terms from the same sequence       '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          Bnum   : {0}                          '.format(x3)
                print '          Bterm  : {0}                          '.format(x4)
                print '                                                '
                print '          Target term : {0}                     '.format(x5)
                print '                                                '

                if x1!=None: pass
                else: x1 = float(raw_input("Enter a number from the sequence: ")); continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")); continue

                if x3!=None: pass
                else: x3 = float(raw_input("Enter another number from the sequence: ")); continue

                if x4!=None: pass
                else:
                    x4 = int(raw_input("On what place is this number can be found in the sequence: "))
                    if x4 == x2:
                        raw_input("Aterm and Bterm can't be the same\n===Press Enter===")
                        x4 = None
                    continue

                if x5!=None: pass
                else: x5 = int(raw_input("What term place are you looking for: ")); continue

                print '------------------------------------------------'
                print '                                                '
                print '   This values builds this sequence:            '
                print '   {0}                                          '.format(AP.generate_list_bycount(x1,x2,AP.compute_change(x1,x2,x3,x4),10))
                print '                                                '
                print '   The {0}th term of this sequence is: {1}      '.format(x5,AP.compute_nterm(x1, x2, AP.compute_change(x1,x2,x3,x4), x5))
                print '                                                '
                print '                                                '
                print '                                                '

                raw_input ("---Press enter to continue---")
                break
            except:
                "\n\n=====Wrong input\n======"

    while True:
        clear()
        print "================================================"
        print '              ARITHMETIC SEQUENCE               '
        print ' ---------------------------------------------- '
        print '   An arithmetic progression is a sequence of   '
        print '   numbers such that the difference of any two  '
        print '         successive members is a constant.      '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   Select Action:                               '
        print '     a) Find the nth term of a sequence         '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   What is given:                               '
        print '      a) A term and the change per term         '
        print '      b) Two terms from the same sequence       '
        print '      z) Back                                   '
        print '                                                '
        print '                                                '

        inp = raw_input("\nEnter your (letter of) choice: ")

        print '\n---\n'

        if inp == 'a':
            sub_a()
            break
        elif inp == 'b':
            sub_b()
            break
        elif inp == 'z':
            break

def choice_b():

    x1 = x2 = x3 = x4 = None

    while True:
        try:
            clear()
            print "================================================"
            print '              ARITHMETIC SEQUENCE               '
            print ' ---------------------------------------------- '
            print '   An arithmetic progression is a sequence of   '
            print '   numbers such that the difference of any two  '
            print '         successive members is a constant.      '
            print '                                                '
            print ' ---------------------------------------------- '
            print '                                                '
            print '   Select Action:                               '
            print '     b) Find the change of a sequence           '
            print '                                                '
            print ' ---------------------------------------------- '
            print '                                                '
            print '    Enter the following variables:              '
            print '                                                '
            print '          Anum   : {0}                          '.format(x1)
            print '          Aterm  : {0}                          '.format(x2)
            print '          Bnum   : {0}                          '.format(x3)
            print '          Bterm  : {0}                          '.format(x4)
            print '                                                '
            print '                                                '

            if x1!=None: pass
            else: x1 = float(raw_input("\nEnter a number from the sequence: ")); continue

            if x2!=None: pass
            else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")); continue

            if x3!=None: pass
            else: x3 = float(raw_input("Enter another number from the sequence: ")); continue

            if x4!=None: pass
            else:
                x4 = int(raw_input("On what place is this number can be found in the sequence: "))
                if x4 == x2:
                    raw_input("Aterm and Bterm can't be the same\n===Press Enter===")
                    x4 = None
                continue

            print '------------------------------------------------'
            print '                                                '
            print '   This values builds this sequence:            '
            print '   {0}                                          '.format(AP.generate_list_bycount(x1,x2,AP.compute_change(x1,x2,x3,x4),10))
            print '                                                '
            print '   The change in this sequence is : {0}         '.format(AP.compute_change(x1, x2, x3, x4))
            print '                                                '

            raw_input ("---Press enter to continue---")
            break
        except:
            "\n\n=====Wrong input\n======"

def choice_c():

    def sub_a():

        def sub_sub_a():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     c) Compute the sum of a sequence           '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      a) A term and the change per term         '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          change : {0}                          '.format(x3)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(int(1))
                    print '           Ending Term   : {0}                  '.format(x5)
                    print '                                                '
                    print '                                                '

                    if x5 != None: pass
                    else:
                        x5 = int(raw_input("\nCompute sum of sequence from start to range: "))

                        continue

                    print '------------------------------------------------'
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,1),1,x3,x5))
                    print '                                                '
                    print '   The sum of the range from this sequence is : {0}'.format(AP.compute_sum_bychange(AP.compute_nterm(x1,x2,x3,1),1,x3,x5))
                    print '                                                '

                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        def sub_sub_b():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     c) Compute the sum of a sequence           '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      a) A term and the change per term         '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          change : {0}                          '.format(x3)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(x5)
                    print '           Ending Term   : {0}                  '.format(x6)
                    print '                                                '
                    print '                                                '

                    if x5!=None: pass
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") ); continue

                    if x6!=None: pass
                    else: x6 = int(raw_input("to ending term: ")); continue

                    print '------------------------------------------------'
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5+1))
                    print '                                                '
                    print '   The sum of the range from this sequence is : {0}'.format(AP.compute_sum_bychange(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5+1))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     c) Compute the sum of a sequence           '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      a) A term and the change per term         '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          change : {0}                          '.format(x3)
                print '                                                '
                print '                                                '

                if x1!=None: pass
                else: x1 = float(raw_input("\nEnter a number from the sequence: ")); continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")); continue

                if x3!=None: pass
                else:x3 = float(raw_input("What is the change per term of the sequence: ")); continue

                qu = raw_input("Compute the sum from start of the sequence? <y/n>: ").lower().strip()

                if qu == 'y':
                    sub_sub_a()
                    break

                elif qu == 'n':
                    sub_sub_b()
                    break

            except:
                "\n\n=====Wrong input\n======"

    def sub_b():
        def sub_sub_a():
            x5 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     c) Compute the sum of a sequence           '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      b) Two term from the same sequence        '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          Bnum   : {0}                          '.format(x3)
                    print '          Bterm  : {0}                          '.format(x4)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(1)
                    print '           Ending Term   : {0}                  '.format(x5)
                    print '                                                '
                    print '                                                '

                    if x5 != None: pass
                    else:
                        x5 = int(raw_input("\nCompute sum of sequence from start to range: "))
                        continue

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '------------------------------------------------'
                    print '                                                '
                    print '   The change in this sequence : {0}            '.format(change)
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,1),1,change,x5))
                    print '                                                '
                    print '   The sum of the range from this sequence is : {0}'.format(AP.compute_sum_bychange(AP.compute_nterm(x1,x2,change,1),1,change,x5))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        def sub_sub_b():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     c) Compute the sum of a sequence           '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      b) Two term from the same sequence        '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          Bnum   : {0}                          '.format(x3)
                    print '          Bterm  : {0}                          '.format(x4)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(x5)
                    print '           Ending Term   : {0}                  '.format(x6)
                    print '                                                '
                    print '                                                '

                    if x5!=None: pass
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") ); continue

                    if x6!=None: pass
                    else: x6 = int(raw_input("to ending term: ")); continue

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '------------------------------------------------'
                    print '                                                '
                    print '   The change in this sequence : {0}            '.format(change)
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5+1))
                    print '                                                '
                    print '   The sum of the sequence from the range is : {0}'.format(AP.compute_sum_bychange(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5+1))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     c) Compute the sum of a sequence           '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      b) Two term from the same sequence        '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          Bnum   : {0}                          '.format(x3)
                print '          Bterm  : {0}                          '.format(x4)
                print '                                                '


                if x1!=None: pass
                else: x1 = float(raw_input("\nEnter a number from the sequence: ")) ; continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")) ; continue

                if x3!=None: pass
                else: x3 = float(raw_input("Enter another number from the sequence: ")) ; continue

                if x4!=None: pass
                else:
                    x4 = int(raw_input("On what place is this number can be found in the sequence: "))
                    if x4 == x2:
                        raw_input("Aterm and Bterm can't be the same\n===Press Enter===")
                        x4 = None
                    continue

                qu = raw_input("Compute the sum from start of the sequence? <y/n>: ").lower().strip()

                if qu == 'y':
                    sub_sub_a()
                    break

                elif qu == 'n':
                    sub_sub_b()
                    break

            except:
                "\n\n=====Wrong input\n======"

    while True:
        clear()
        print "================================================"
        print '              ARITHMETIC SEQUENCE               '
        print ' ---------------------------------------------- '
        print '   An arithmetic progression is a sequence of   '
        print '   numbers such that the difference of any two  '
        print '         successive members is a constant.      '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   Select Action:                               '
        print '     c) Compute the sum of a sequence           '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   What is given:                               '
        print '      a) A term and the change per term         '
        print '      b) Two terms from the same sequence       '
        print '      z) Back                                   '
        print '                                                '

        inp = raw_input("\nEnter your (letter of) choice: ")

        print '\n---'

        if inp == 'a':
            sub_a()
            break
        elif inp == 'b':
            sub_b()
            break
        elif inp == 'z':
            break

def choice_d():

    def sub_a():

        def sub_sub_a():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     d) Generate a sequence list                '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      a) A term and the change per term         '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          change : {0}                          '.format(x3)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(int(1))
                    print '           Ending Term   : {0}                  '.format(x5)
                    print '                                                '
                    print '                                                '

                    if x5 != None: pass
                    else:
                        x5 = int(raw_input("\nCompute sum of sequence from start to range: "))
                        continue

                    print '------------------------------------------------'
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,1),1,x3,x5))
                    print '                                                '
                    print '                                                '

                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        def sub_sub_b():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     d) Generate a sequence list                '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      a) A term and the change per term         '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          change : {0}                          '.format(x3)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(x5)
                    print '           Ending Term   : {0}                  '.format(x6)
                    print '                                                '
                    print '                                                '

                    if x5!=None: pass
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") ); continue

                    if x6!=None: pass
                    else: x6 = int(raw_input("to ending term: ")); continue

                    print '------------------------------------------------'
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5+1))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     d) Generate a sequence list                '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      a) A term and the change per term         '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          change : {0}                          '.format(x3)
                print '                                                '
                print '                                                '

                if x1!=None: pass
                else: x1 = float(raw_input("\nEnter a number from the sequence: ")); continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")); continue

                if x3!=None: pass
                else:x3 = float(raw_input("What is the change per term of the sequence: ")); continue

                qu = raw_input("Compute the sum from start of the sequence? <y/n>: ").lower().strip()

                if qu == 'y':
                    sub_sub_a()
                    break

                elif qu == 'n':
                    sub_sub_b()
                    break

            except:
                "\n\n=====Wrong input\n======"

    def sub_b():
        def sub_sub_a():
            x5 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     d) Generate a sequence list                '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      b) Two term from the same sequence        '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          Bnum   : {0}                          '.format(x3)
                    print '          Bterm  : {0}                          '.format(x4)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(1)
                    print '           Ending Term   : {0}                  '.format(x5)
                    print '                                                '
                    print '                                                '

                    if x5 != None: pass
                    else:
                        x5 = int(raw_input("\nCompute sum of sequence from start to range: "))
                        continue

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '------------------------------------------------'
                    print '                                                '
                    print '   The change in this sequence : {0}            '.format(change)
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,1),1,change,x5))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        def sub_sub_b():
            x5 = x6 = None
            while True:
                try:
                    clear()
                    print "================================================"
                    print '              ARITHMETIC SEQUENCE               '
                    print ' ---------------------------------------------- '
                    print '   An arithmetic progression is a sequence of   '
                    print '   numbers such that the difference of any two  '
                    print '         successive members is a constant.      '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   Select Action:                               '
                    print '     d) Generate a sequence list                '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '   What is given:                               '
                    print '      b) Two term from the same sequence        '
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '    Enter the following variables:              '
                    print '                                                '
                    print '          Anum   : {0}                          '.format(x1)
                    print '          Aterm  : {0}                          '.format(x2)
                    print '          Bnum   : {0}                          '.format(x3)
                    print '          Bterm  : {0}                          '.format(x4)
                    print '                                                '
                    print ' ---------------------------------------------- '
                    print '                                                '
                    print '     Compute sum from range :                   '
                    print '                                                '
                    print '           Starting Term : {0}                  '.format(x5)
                    print '           Ending Term   : {0}                  '.format(x6)
                    print '                                                '
                    print '                                                '

                    if x5!=None: pass
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") ); continue

                    if x6!=None: pass
                    else: x6 = int(raw_input("to ending term: ")); continue

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '------------------------------------------------'
                    print '                                                '
                    print '   The change in this sequence : {0}            '.format(change)
                    print '                                                '
                    print '   This values builds this sequence:            '
                    print '   {0}                                          '.format(AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5+1))
                    print '                                                '

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print "================================================"
                print '              ARITHMETIC SEQUENCE               '
                print ' ---------------------------------------------- '
                print '   An arithmetic progression is a sequence of   '
                print '   numbers such that the difference of any two  '
                print '         successive members is a constant.      '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   Select Action:                               '
                print '     d) Generate a sequence list                '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '   What is given:                               '
                print '      b) Two term from the same sequence        '
                print '                                                '
                print ' ---------------------------------------------- '
                print '                                                '
                print '    Enter the following variables:              '
                print '                                                '
                print '          Anum   : {0}                          '.format(x1)
                print '          Aterm  : {0}                          '.format(x2)
                print '          Bnum   : {0}                          '.format(x3)
                print '          Bterm  : {0}                          '.format(x4)
                print '                                                '


                if x1!=None: pass
                else: x1 = float(raw_input("\nEnter a number from the sequence: ")) ; continue

                if x2!=None: pass
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: ")) ; continue

                if x3!=None: pass
                else: x3 = float(raw_input("Enter another number from the sequence: ")) ; continue

                if x4!=None: pass
                else:
                    x4 = int(raw_input("On what place is this number can be found in the sequence: "))
                    if x4 == x2:
                        raw_input("Aterm and Bterm can't be the same\n===Press Enter===")
                        x4 = None
                    continue

                qu = raw_input("Compute the sum from start of the sequence? <y/n>: ").lower().strip()

                if qu == 'y':
                    sub_sub_a()
                    break

                elif qu == 'n':
                    sub_sub_b()
                    break

            except:
                "\n\n=====Wrong input\n======"

    while True:
        clear()
        print "================================================"
        print '              ARITHMETIC SEQUENCE               '
        print ' ---------------------------------------------- '
        print '   An arithmetic progression is a sequence of   '
        print '   numbers such that the difference of any two  '
        print '         successive members is a constant.      '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   Select Action:                               '
        print '     d) Generate a sequence list                '
        print '                                                '
        print ' ---------------------------------------------- '
        print '                                                '
        print '   What is given:                               '
        print '      a) A term and the change per term         '
        print '      b) Two terms from the same sequence       '
        print '      z) Back                                   '
        print '                                                '

        inp = raw_input("\nEnter your (letter of) choice: ")

        print '\n---'

        if inp == 'a':
            sub_a()
            break
        elif inp == 'b':
            sub_b()
            break
        elif inp == 'z':
            break

def choice_e():

    clear()

    x1,x2 = 5,1
    x3,x4 = 10,2
    change = 5
    look_for = 6
    range_var = 6

    print "================================================"
    print '              ARITHMETIC SEQUENCE               '
    print ' ---------------------------------------------- '
    print '   An arithmetic progression is a sequence of   '
    print '   numbers such that the difference of any two  '
    print '         successive members is a constant.      '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '        f) Generate a a quick sample            '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '  >> compute_nterm({0},{1},{2},{3})             '.format(x1,x2,change,look_for)
    print '  >> {0}                                        '.format(AP.compute_nterm(x1,x2,change,look_for))
    print '                                                '
    print '  >> compute_change({0},{1},{2},{3})            '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.compute_change(x1,x2,x3,x4))
    print '                                                '
    print '  >> compute_sum_bychange({0},{1},{2},{3})      '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_bychange(x1,x2,change,range_var))
    print '                                                '
    print '  >> compute_sum_byterm({0},{1},{2},{3},{4})    '.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_byterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bylastterm({0},{1},{2},{3},{4})'.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bylastterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bycount(x1,x2,change,range_var))
    print '                                                '
    print '  >> generate_iter_bylastterm({0},{1},{2},{3})  '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.generate_iter_bylastterm(x1,x2,x3,x4))
    print '                                                '
    print '  >> generate_iter_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_iter_bycount(x1,x2,change,range_var))
    print '                                                '

    raw_input ("---Press enter to NEXT---")

    clear()

    x1,x2 = 6,2
    x3,x4 = 3,1
    change = 3
    look_for = -8
    range_var = -4

    print "================================================"
    print '              ARITHMETIC SEQUENCE               '
    print ' ---------------------------------------------- '
    print '   An arithmetic progression is a sequence of   '
    print '   numbers such that the difference of any two  '
    print '         successive members is a constant.      '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '        f) Generate a a quick sample            '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '  >> compute_nterm({0},{1},{2},{3})             '.format(x1,x2,change,look_for)
    print '  >> {0}                                        '.format(AP.compute_nterm(x1,x2,change,look_for))
    print '                                                '
    print '  >> compute_change({0},{1},{2},{3})            '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.compute_change(x1,x2,x3,x4))
    print '                                                '
    print '  >> compute_sum_bychange({0},{1},{2},{3})      '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_bychange(x1,x2,change,range_var))
    print '                                                '
    print '  >> compute_sum_byterm({0},{1},{2},{3},{4})    '.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_byterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bylastterm({0},{1},{2},{3},{4})'.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bylastterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bycount(x1,x2,change,range_var))
    print '                                                '
    print '  >> generate_iter_bylastterm({0},{1},{2},{3})  '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.generate_iter_bylastterm(x1,x2,x3,x4))
    print '                                                '
    print '  >> generate_iter_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_iter_bycount(x1,x2,change,range_var))
    print '                                                '

    raw_input ("---Press enter to NEXT---")

    clear()

    x1,x2 = 3,2
    x3,x4 = 1.5,1
    change = 1.5
    look_for = 5
    range_var = 10

    print "================================================"
    print '              ARITHMETIC SEQUENCE               '
    print ' ---------------------------------------------- '
    print '   An arithmetic progression is a sequence of   '
    print '   numbers such that the difference of any two  '
    print '         successive members is a constant.      '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '        f) Generate a a quick sample            '
    print '                                                '
    print ' ---------------------------------------------- '
    print '                                                '
    print '  >> compute_nterm({0},{1},{2},{3})             '.format(x1,x2,change,look_for)
    print '  >> {0}                                        '.format(AP.compute_nterm(x1,x2,change,look_for))
    print '                                                '
    print '  >> compute_change({0},{1},{2},{3})            '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.compute_change(x1,x2,x3,x4))
    print '                                                '
    print '  >> compute_sum_bychange({0},{1},{2},{3})      '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_bychange(x1,x2,change,range_var))
    print '                                                '
    print '  >> compute_sum_byterm({0},{1},{2},{3},{4})    '.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.compute_sum_byterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bylastterm({0},{1},{2},{3},{4})'.format(x1,x2,x3,x4,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bylastterm(x1,x2,x3,x4,range_var))
    print '                                                '
    print '  >> generate_list_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_list_bycount(x1,x2,change,range_var))
    print '                                                '
    print '  >> generate_iter_bylastterm({0},{1},{2},{3})  '.format(x1,x2,x3,x4)
    print '  >> {0}                                        '.format(AP.generate_iter_bylastterm(x1,x2,x3,x4))
    print '                                                '
    print '  >> generate_iter_bycount({0},{1},{2},{3})     '.format(x1,x2,change,range_var)
    print '  >> {0}                                        '.format(AP.generate_iter_bycount(x1,x2,change,range_var))
    print '                                                '

    raw_input ("---Press enter to NEXT---")

main_menu()
