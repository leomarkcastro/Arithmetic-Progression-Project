# Arithmetic-Progression-Project

Arithmetic Progression code.

Written in Python 2.7

'''
    What should the app do?

        1) Find the nth term given:
            a) A term and the a change
            b) A term and another term
            c) A sequence
        2) Find the change given:
            a) A term and another term
            b) A sequence
        3) Compute the sum of a sequence given:
            a) A term and then a change
                a) from range 1 to n
                b) from range n1 to n2
            b) A term and another term
                a) from range 1 to n
                b) from range n1 to n2
            c) A sequence
        4) Generate a list of arithmetic sequence given:
            a) A term and then a change
                a) from range 1 to n
                b) from range n1 to n2
            b) A term and another term
                a) from range 1 to n
                b) from range n1 to n2


'''

'''
        Errors, the numbers should only be Natural Numbers {1,2,3...}, no negative
                     1   2   3   4   5
        Number  :{   1   3   5   7   9  }
'''


##################################################



#computing for the change between values

#compute_change(Anum, Aterm, Bnum, Bterm)

'''
Assuming that you have a sequence {1,3,5,7,9}. Find the change(d)
You can pick anything, assuming that the number is in the right term
The {3} is in 2nd term. The {9} is in 5th tern
'''
#print AP.compute_change(3,2,9,5)               Uncomment this line to see the result

'''
Another example. Given a sequence, the 5th term has the number {20} and the 2nd tern has number {35}. Find change(d)
'''
#print AP.compute_change(20,5,35,2)             #Uncomment this line to see the result

'''
You could also try to use the function in such way:
    Given that the 6th term is 22 and the 48th term is 97. Find d
'''
#print AP.compute_change(Anum = 22, Aterm = 6, Bnum = 97, Bterm = 48)       #Uncomment this line to see the result




##################################################




#computing for the nth term of a arithmetic sequence


#compute_nterm(Anum, Aterm, change, Bterm)

'''
Given that you have a sequence {1,4,7,10,13,...} find the 48th term
    By using the compute_change function, you can see that the change in this sequence is {3}
'''
#print AP.compute_nterm(1,1,3,48)                     #Uncomment this line to see the result

'''
Given that you have the {49} as the 7th term in the sequence and a constant change of 7, find the 1st term
'''
#print AP.compute_nterm(Anum = 49, Aterm = 7, change = 7, Bterm = 1)      #Uncomment this line to see the result





##################################################



#computing the sum of a sequence given that you have a term given and the change


#compute_change(Anum, Aterm, change, count)

'''
Given that the 8th term is 24 and the constant change is 3. Find the sum of the first 15 terms
'''
#print AP.compute_sum_bychange(24,8,3,15)           #Uncomment this line to see result

'''
Given that the 8th term is 24 and the constant change is 3. Find the sum of the 15th to 25th terms.

    First, you should compute the Anum and Aterm to be the 15th number and term
    Then, set the count by computing for the range. {25 - 15} = {10} <-- this will by the 'count'

    15th term: AP.compute_nterm(24,8,3,15) -->   45
    count    : {25 - 15} = {10}

    The logic here is that the list now will start {1st term} in 45 then end at the range of 10
'''
#print AP.compute_sum_bychange(Anum = 45, Aterm = 1, change = 3, count = 10)     #Uncomment this line to see result




##################################################




#computing the sum of a sequence given that you have two terms from the sequence given, and the count of terms in the sequnce


#compute_change(Anum, Aterm, Bnum, Bterm, count = None)

'''
Find the sum of the series {1,3,5,7,9,11,13,15}
{1} 1st term
{15} 8th term <- also the last term
'''
#print AP.compute_sum_byterm(1,1,15,8)

'''
Find the sum of the series given that the {5} is the 3rd term and {11} is the 6th term. Find the sum of first 8 terms
{5} 3rd term
{11} 6th term
count = 8
'''
#print AP.compute_sum_byterm(Anum = 5, Aterm = 3, Bnum = 11, Bterm = 6, count = 8)





##################################################





#generate a list of arithmetic sequence, given that you have the first term and the range




#generate_list_bycount(Anum, Aterm, change, count)

'''
Generate a sequence given that the first term is 25 and the constant change is 4. The count of terms is upto 25
'''
#print AP.generate_list_bycount(25,1,4,25)

'''
Generate a sequence given that the second term is 4 and the constant change is 3. The count of terms is upto 25
'''
#print AP.generate_list_bycount(4,2,3,25)

'''
Generate a sequence given that the third term is 7 and the constant change is 5. The range is from 4th term to 12th term
{7} 3rd term
d = change
range = 4th to 12th

a) Find the first term (in this case, the 4th term):
    AP.compute_nterm(7,3,5,4) --> 12
b) Find the range:
    12 - 4 = 8

'''
#print AP.generate_list_bycount(12,1,5,8)




##################################################



#generate a list of arithmetic sequence, given that you have the first term and another/last term



#generate_list_bycount(Anum, Aterm, Bnum, Bterm, count = None)
# leave the count empty, the Bterm will be assumed as the last term

'''
The first term is 5 and the 20th term is 100. Generate a list
'''

#print AP.generate_list_bylastterm(5,1,100,20)

'''
The third term is 18 and the sixth term is 36. Generate a list spanning up to 20 terms
'''

#print AP.generate_list_bylastterm(Anum = 18, Aterm = 3, Bnum = 36, Bterm = 6, count = 20)




##################################################


#generate an iterable of arithmetic sequence, given that you have the first term and the change
#generate_iter_bychange(Anum, Aterm, change, count = None)

#this function is useful for infinite list generating

'''

iterab = AP.generate_iter_bychange(0,1,5)
print iterab

for i in iterab:
    print i

'''# this will generate a sequence, forever

'''

iterab = AP.generate_iter_bychange(Anum = 0, Aterm = 1, change = 5)

for i in range(50):
    print iterab.next()

'''# this will generate a sequence up to 50

'''

iterab = AP.generate_iter_bychange(Anum = 0, Aterm = 1, change = 5, count = 20)

for i in range(50):
    print iterab.next()

'''# this will generate a sequence up to 50. But since, you put a limit {20}. It can only generate up to 20 result
# the above code will generate an error

##################################################


#generate an iterable of arithmetic sequence, given that you have the first term, a second/last term and an optional count
#generate_iter_byterm(Anum, Aterm, Bnum, Bterm, count = None)

#this function is useful for infinite list generating

'''

iterab = AP.generate_iter_byterm(0,1,15,4)
print iterab

for i in iterab:
    print i

'''# this will generate a sequence

'''

iterab = AP.generate_iter_byterm(Anum = 0, Aterm = 1, Bnum = 12, Bterm = 5)

for i in range(50):
    print iterab.next()

'''# this will generate a sequence up to 50

'''

iterab = AP.generate_iter_byterm(Anum = 0, Aterm = 1, Bnum = 12, Bterm = 5, count = 20)

for i in range(50):
    print iterab.next()

'''# this will generate a sequence up to 50. But since, you put a limit {20}. It can only generate up to 20 result
# the above code will generate an error
