'''
    ArithProg Sandbox

    Test the different programs of ArithProg here
'''

import ArithProg as AP

#functions
AP.compute_nterm(Anum = 1, Aterm = 2, change = 3, Bterm = 4)
AP.compute_change(Anum = 1, Aterm = 2, Bnum = 3, Bterm = 4)
AP.compute_sum_bychange(Anum = 1, Aterm = 2, change = 3, count = 4)
AP.compute_sum_byterm(Anum = 1, Aterm = 2, Bnum = 3, Bterm = 4, count = 5)
AP.generate_list_bycount(Anum = 1, Aterm = 2, change = 3, count = 4)
AP.generate_list_bylastterm(Anum = 1, Aterm = 2, Bnum = 3, Bterm = 4, count = None)
AP.generate_iter_bycount(Anum = 1, Aterm = 2, change = 3, count = None)
AP.generate_iter_bylastterm(Anum = 1, Aterm = 2, Bnum = 3, Bterm = 4, count = None)

### Start Coding here

x = AP.generate_iter_bylastterm(Anum = 1, Aterm = 1, Bnum = 2.5, Bterm = 3, count = None)

print x
for i in range(15):
    print x.next()
