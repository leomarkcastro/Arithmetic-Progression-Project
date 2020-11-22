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
        print 'ARITHMETIC SEQUENCE\n'
        print 'An arithmetic progression is a sequence of numbers such that the difference of any two successive members is a constant.'
        print '\n============================================================'
        print '\nSelect Action:'
        print 'a) Find the nth term of a sequence'
        print 'b) Find the change of a sequence'
        print 'c) Compute the sum of a sequence'
        print 'd) Generate a list of arithmetic sequence'
        print 'z) Quit App'

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
        elif inp == 'z':
            break


def choice_a():

    def sub_a():
        x1 = x2 = x3= x4 = None
        while True:
            try:
                clear()
                print 'Find the nth term of a sequence ~ given ~ A term and the change per term'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "What is the change per term of the sequence: ", x3
                else:x3 = float(raw_input("What is the change per term of the sequence: "))

                if x4!=None: print "What place in the sequence is the value you are looking is located: ", x4
                else:x4 = int(raw_input("What place in the sequence is the value you are looking is located: "))

                print '\n\nGiven the following values:\n'
                print 'Anum:\t', x1
                print 'Aterm:\t', x2
                print 'change:\t', x3
                print '\nThis values builds this sequence: ', AP.generate_list_bycount(x1,x2,x3,10)
                print '\nThe %dth term of this sequence is: '%(x4), AP.compute_nterm(x1, x2, x3, x4)
                print

                raw_input ("---Press enter to continue---")
                break
            except:
                "\n\n=====Wrong input\n======"

    def sub_b():
        x1 = x2 = x3= x4 = x5 = None
        while True:
            try:
                clear()
                print 'Find the nth term of a sequence ~ given ~ Two terms from the same sequence'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "Enter another number from the sequence: ", x3
                else: x3 = float(raw_input("Enter another number from the sequence: "))

                if x4!=None: print "On what place is this number can be found: ", x4
                else:x4 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x5!=None: print "What term place are you looking for: ", x5
                else: x5 = int(raw_input("What term place are you looking for: "))

                print '\n\nGiven the following values:\n'
                print '[%d] term is:\t'%(x2), x1
                print '[%d} term is:\t'%(x4), x3
                print 'change:\t', AP.compute_change(x1,x2,x3,x4)
                print '\nThis values builds this sequence: ', AP.generate_list_bycount(x1,x2,AP.compute_change(x1,x2,x3,x4),10)
                print '\nThe %dth term of this sequence is: '%(x5), AP.compute_nterm(x1, x2, AP.compute_change(x1,x2,x3,x4), x5)
                print

                raw_input ("---Press enter to continue---")
                break
            except:
                "\n\n=====Wrong input\n======"

    while True:
        clear()
        print 'Find the nth term of a sequence'
        print '\nWhat is given:'
        print 'a) A term and the change per term'
        print 'b) Two terms from the same sequence'
        print 'z) Back'

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
            print 'Find the change per term of the sequence ~ given ~ Two terms from the same sequence'

            if x1!=None: print "\nEnter a number from the sequence: ", x1
            else: x1 = float(raw_input("\nEnter a number from the sequence: "))

            if x2!=None: print "On what place is this number can be found: ", x2
            else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

            if x3!=None: print "Enter another number from the sequence: ", x3
            else: x3 = float(raw_input("Enter another number from the sequence: "))

            if x4!=None: print "On what place is this number can be found: ", x4
            else:x4 = int(raw_input("On what place is this number can be found in the sequence: "))

            print '\n\nGiven the following values:\n'
            print '[%d] term is:\t'%(x2), x1
            print '[%d} term is:\t'%(x4), x3
            print '\nThis values builds this sequence: ', AP.generate_list_bycount(x1,x2,AP.compute_change(x1,x2,x3,x4),10)
            print '\nThe constant change of this sequence is: ', AP.compute_change(x1, x2, x3, x4)
            print

            raw_input ("---Press enter to continue---")
            break
        except:
            "\n\n=====Wrong input\n======"

def choice_c():

    def sub_a():

        def sub_sub_a():
            while True:
                try:
                    clear()
                    print 'Compute the sum of a sequence ~ given ~ A term and the change per term'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "What is the change per term of the sequence: ", x3

                    x5 = int(raw_input("\nCompute sum of sequence from start to range: "))

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x2), x1
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,x3,x5)
                    print 'change:\t', x3
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,1),1,x3,x5-1)
                    print '\nThe sum of this sequence is: ', AP.compute_sum_bychange(AP.compute_nterm(x1,x2,x3,1),1,x3,x5)

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
                    print 'Compute the sum of a sequence ~ given ~ A term and the change of the sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "What is the change per term of the sequence: ", x3

                    if x5!=None: print "\nCompute sum of sequence from starting term: ", x5
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") )

                    if x6!=None: print "to ending term: ", x6
                    else: x6 = int(raw_input("to ending term: "))

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,x3,x5)
                    print '[%d] term with value :\t'%(x6), AP.compute_nterm(x1,x2,x3,x6)
                    print 'change:\t', x3
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5)
                    print '\nThe sum of this sequence is: ', AP.compute_sum_bychange(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5+1)

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print 'Compute the sum of a sequence ~ given ~ A term and the change per term'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "What is the change per term of the sequence: ", x3
                else:x3 = float(raw_input("What is the change per term of the sequence: "))

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
            while True:
                try:
                    clear()
                    print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "Enter another number from the sequence: ", x3
                    print "On what place is this number can be found: ", x4

                    x5 = int(raw_input("\nCompute sum of sequence from start to range: "))

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x2), x1
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,change,x5)

                    print 'change:\t',change
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,1),1,change,x5-1)
                    print '\nThe sum of this sequence is: ', AP.compute_sum_bychange(AP.compute_nterm(x1,x2,change,1),1,change,x5)

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
                    print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "Enter another number from the sequence: ", x3
                    print "On what place is this number can be found: ", x4

                    if x5!=None: print "\nCompute sum of sequence from starting term: ", x5
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") )

                    if x6!=None: print "to ending term: ", x6
                    else: x6 = int(raw_input("to ending term: "))

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,change,x5)
                    print '[%d] term with value :\t'%(x6), AP.compute_nterm(x1,x2,change,x6)

                    print 'change:\t',change
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5)
                    print '\nThe sum of this sequence is: ', AP.compute_sum_bychange(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5+1)

                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "Enter another number from the sequence: ", x3
                else: x3 = float(raw_input("Enter another number from the sequence: "))

                if x4!=None: print "On what place is this number can be found: ", x4
                else:x4 = int(raw_input("On what place is this number can be found in the sequence: "))

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
        print 'Compute the sum of a sequence'
        print '\nWhat is given:'
        print 'a) A term and the change per term'
        print 'b) Two terms from the same sequence'
        print 'z) Back'

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
            while True:
                try:
                    clear()
                    print 'Compute the sum of a sequence ~ given ~ A term and the change per term'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "What is the change per term of the sequence: ", x3

                    x5 = int(raw_input("\nCompute sum of sequence from start to range: "))

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x2), x1
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,x3,x5)
                    print 'change:\t', x3
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,1),1,x3,x5-1)
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
                    print 'Compute the sum of a sequence ~ given ~ A term and the change of the sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "What is the change per term of the sequence: ", x3

                    if x5!=None: print "\nCompute sum of sequence from starting term: ", x5
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") )

                    if x6!=None: print "to ending term: ", x6
                    else: x6 = int(raw_input("to ending term: "))

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,x3,x5)
                    print '[%d] term with value :\t'%(x6), AP.compute_nterm(x1,x2,x3,x6)
                    print 'change:\t', x3
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,x3,x5),1,x3,x6-x5)
                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print 'Compute the sum of a sequence ~ given ~ A term and the change per term'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "What is the change per term of the sequence: ", x3
                else:x3 = float(raw_input("What is the change per term of the sequence: "))

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
            while True:
                try:
                    clear()
                    print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "Enter another number from the sequence: ", x3
                    print "On what place is this number can be found: ", x4

                    x5 = int(raw_input("\nCompute sum of sequence from start to range: "))

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x2), x1
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,change,x5)

                    print 'change:\t',change
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,1),1,change,x5-1)

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
                    print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                    print "\nEnter a number from the sequence: ", x1
                    print "On what place is this number can be found: ", x2
                    print "Enter another number from the sequence: ", x3
                    print "On what place is this number can be found: ", x4

                    if x5!=None: print "\nCompute sum of sequence from starting term: ", x5
                    else: x5 = int( raw_input("\nCompute sum of sequence from starting term: ") )

                    if x6!=None: print "to ending term: ", x6
                    else: x6 = int(raw_input("to ending term: "))

                    change = AP.compute_change(x1,x2,x3,x4)

                    print '\n\nGiven the following values:\n'
                    print '[%d] term with value :\t'%(x5), AP.compute_nterm(x1,x2,change,x5)
                    print '[%d] term with value :\t'%(x6), AP.compute_nterm(x1,x2,change,x6)


                    print 'change:\t',change
                    print '\nThis values builds this sequence: ', AP.generate_list_bycount(AP.compute_nterm(x1,x2,change,x5),1,change,x6-x5)
                    print
                    raw_input ("---Press enter to continue---")
                    break

                except:
                    "\n\n=====Wrong input\n======"

        x1 = x2 = x3= x4 = x5 = x6 = None

        while True:

            try:
                clear()
                print 'Compute the sum of a sequence ~ given ~ Two terms from the same sequence'

                if x1!=None: print "\nEnter a number from the sequence: ", x1
                else: x1 = float(raw_input("\nEnter a number from the sequence: "))

                if x2!=None: print "On what place is this number can be found: ", x2
                else:x2 = int(raw_input("On what place is this number can be found in the sequence: "))

                if x3!=None: print "Enter another number from the sequence: ", x3
                else: x3 = float(raw_input("Enter another number from the sequence: "))

                if x4!=None: print "On what place is this number can be found: ", x4
                else:x4 = int(raw_input("On what place is this number can be found in the sequence: "))

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
        print 'Compute the sum of a sequence'
        print '\nWhat is given:'
        print 'a) A term and the change per term'
        print 'b) Two terms from the same sequence'
        print 'z) Back'

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


main_menu()
