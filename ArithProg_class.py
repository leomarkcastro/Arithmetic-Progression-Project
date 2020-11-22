from __future__ import division

class ArithProg():
    def __init__(self):
        '''
        Arithmetic Progression is called
        '''

    def compute_nterm(self, Anum, Aterm, change, Bterm):
        '''
            Compute the nth of a term given that you have the:
                Anum of Aterm term  = the number and its position in the progression
                change              = changes per term
                Bterm               = the position of the term you are looking for

        '''




        returnvalue = (Anum + (Bterm - Aterm) * change)

        if float(returnvalue).is_integer():
            return int(returnvalue)
        else:
            return (returnvalue)


    def compute_change(self, Anum, Aterm, Bnum, Bterm):
        '''
            Compute the d (changes per term) of the progression:
                Anum of Aterm term  = the first given number and its position in the progression
                Bnum of Bterm term  = the second given number and its position in the progression

        '''

        returnvalue = (Bnum - Anum) / (Bterm - Aterm)

        if float(returnvalue).is_integer():
            return int(returnvalue)
        else:
            return (returnvalue)


    def compute_sum_bychange(self, Anum, Aterm, change, count):
        '''
            Compute the sum of a progression given that you have the:
                Anum of Aterm term  = the number and its position in the progression
                change              = changes per term
                count               = the number of terms you have in the progression

        '''

        returnvalue = (count / 2.0) * ( 2 * (self.compute_nterm(Anum,Aterm,change,1)) + (count - 1) * change)

        if float(returnvalue).is_integer():
            return int(returnvalue)
        else:
            return (returnvalue)


    def compute_sum_byterm(self, Anum, Aterm, Bnum, Bterm, count):
        '''
            Compute the sum of a progression given that you have the:
                Anum of Aterm term  = the first given number and its position in the progression
                Bnum of Bterm term  = the second given number and its position in the progression

        '''

        returnvalue = (count / 2.0) * ( ( (self.compute_change(Anum, Aterm, Bnum, Bterm))) * (1+count-Aterm-Bterm) + (Anum + Bnum) )

        if float(returnvalue).is_integer():
            return int(returnvalue)
        else:
            return (returnvalue)

    def generate_list_bycount(self, Anum, Aterm, change, count):
        '''
            Generate a list of arithmetic sequence given that you have:
                Anum of Aterm term  = the first given number and its position in the progression
                change              = changes per term
                count               = the number of terms you have in the progression
        '''

        retlist = list()

        x = self.compute_nterm(Anum,Aterm,change,1)

        for i in range(1,count+1):
            retlist.append( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))

        return retlist

    def generate_list_bylastterm(self, Anum, Aterm, Bnum, Bterm, count = None):
        '''
            Generate a list of arithmetic sequence given that you have:
                Anum of Aterm term  = the first given number and its position in the progression
                change              = changes per term
                count               = the number of terms you have in the progression
        '''

        change = self.compute_change(Anum,Aterm,Bnum,Bterm)

        retlist = list()

        x = self.compute_nterm(Anum,Aterm,change,1)

        for i in range(1,count+1 if count!=None else Bterm + 1):
            retlist.append( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))

        return retlist

    def generate_iter_bycount(self, Anum, Aterm, change, count=None):
        '''
            Generate a list of arithmetic sequence given that you have:
                Anum of Aterm term  = the first given number and its position in the progression
                change              = changes per term
                count               = the number of terms you have in the progression
        '''

        x = self.compute_nterm(Anum,Aterm,change,1)

        if count != None:
            for i in range(1,count+1):
                yield ( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))
        else:
            i = 0
            while True:
                i += 1
                yield ( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))


    def generate_iter_bylastterm(self, Anum, Aterm, Bnum, Bterm, count = None):
        '''
            Generate a list of arithmetic sequence given that you have:
                Anum of Aterm term  = the first given number and its position in the progression
                change              = changes per term
                count               = the number of terms you have in the progression
        '''

        change = self.compute_change(Anum, Aterm, Bnum, Bterm)
        x = self.compute_nterm(Anum,Aterm,change,1)

        if count != None:
            for i in range(1,count+1 if count!=None else Bterm + 1):
                yield ( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))
        else:
            i = 0
            while True:
                i += 1
                yield ( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))



if __name__ == '__main__':
    print "Welcome to the Arithmetic Progression Module"
    print "Programs include:"
    print " > compute_nterm"
    print " > compute_change"
    print " > compute_sum_bydif"
    print " > compute_sum_byterm"
    print " > generate_list_bycount"
    print " > generate_list_bylastterm"
    print " > generate_iter_bycount"
    print " > generate_iter_bylastterm"





