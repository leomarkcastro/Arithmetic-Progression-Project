from __future__ import division

def compute_nterm(Anum, Aterm, change, Bterm):
    '''
        Compute the nth of a term given that you have the:
            Anum of Aterm term  = the number and its position in the progression
            change              = changes per term
            Bterm               = the position of the term you are looking for

    '''

    #============checker
    if type(Aterm) != int or type(Bterm) != int:
        raise TypeError("Error, Aterm and Bterm must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(change) != int and type(change) != float and type(change) != str:
        raise TypeError("Error, change must be an integer or float")
    elif type(change) == str:
        raise TypeError("Error, change is a string. Convert it to integer or float first")
    #=====end of checking

    returnvalue = (Anum + (Bterm - Aterm) * change)

    if float(returnvalue).is_integer():
        return int(returnvalue)
    else:
        return (returnvalue)

def compute_change(Anum, Aterm, Bnum, Bterm):
    '''
        Compute the d (changes per term) of the progression:
            Anum of Aterm term  = the first given number and its position in the progression
            Bnum of Bterm term  = the second given number and its position in the progression

    '''

    #============checker
    if type(Aterm) != int or type(Bterm) != int:
        raise TypeError("Error, Aterm and Bterm must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(Bnum) != int and type(Bnum) != float and type(Bnum) != str:
        raise TypeError("Error, Bnum must be an integer or float")
    elif type(Bnum) == str:
        raise TypeError("Error, Bnum is a string. Convert it to integer or float first")

    if Aterm == Bterm:
        raise ValueError("Aterm and Bterm should'nt have the same value")
    #=====end of checking


    returnvalue = (Bnum - Anum) / (Bterm - Aterm)

    if float(returnvalue).is_integer():
        return int(returnvalue)
    else:
        return (returnvalue)

def compute_sum_bychange(Anum, Aterm, change, count):
    '''
        Compute the sum of a progression given that you have the:
            Anum of Aterm term  = the number and its position in the progression
            change              = changes per term
            count               = the number of terms you have in the progression

    '''

    #============checker
    if type(Aterm) != int or type(count) != int:
        raise TypeError("Error, Aterm and count must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(change) != int and type(change) != float and type(change) != str:
        raise TypeError("Error, change must be an integer or float")
    elif type(change) == str:
        raise TypeError("Error, change is a string. Convert it to integer or float first")
    #=====end of checking


    if (count < 0):
        returnvalue = ((count * -1 + Aterm + 1) / 2.0) * (compute_nterm(Anum,Aterm,change,count) + compute_nterm(Anum,Aterm,change,Aterm))
    else:
        returnvalue = (count / 2.0) * ( 2 * (compute_nterm(Anum,Aterm,change,1)) + (count - 1) * change)

    if float(returnvalue).is_integer():
        return int(returnvalue)
    else:
        return (returnvalue)

def compute_sum_byterm(Anum, Aterm, Bnum, Bterm, count):
    '''
        Compute the sum of a progression given that you have the:
            Anum of Aterm term  = the first given number and its position in the progression
            Bnum of Bterm term  = the second given number and its position in the progression

    '''

    #============checker
    if type(Aterm) != int or type(Bterm) != int or type(count) != int:
        raise TypeError("Error, Aterm, Bterm and count must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(Bnum) != int and type(Bnum) != float and type(Bnum) != str:
        raise TypeError("Error, Bnum must be an integer or float")
    elif type(Bnum) == str:
        raise TypeError("Error, Bnum is a string. Convert it to integer or float first")

    if Aterm == Bterm:
        raise ValueError("Aterm and Bterm should'nt have the same value")
    #=====end of checking


    change = compute_change(Anum,Aterm,Bnum,Bterm)
    if (count < 0):
        returnvalue = ((count * -1 + Aterm + 1) / 2.0) * (compute_nterm(Anum,Aterm,change,count) + compute_nterm(Anum,Aterm,change,Aterm))
    else:
        returnvalue = (count / 2.0) * ( ( change ) * (1+count-Aterm-Bterm) + (Anum + Bnum) )

    if float(returnvalue).is_integer():
        return int(returnvalue)
    else:
        return (returnvalue)

def generate_list_bycount(Anum, Aterm, change, count):
    '''
        Generate a list of arithmetic sequence given that you have:
            Anum of Aterm term  = the first given number and its position in the progression
            change              = changes per term
            count               = the number of terms you have in the progression
    '''

    #============checker
    if type(Aterm) != int or type(count) != int:
        raise TypeError("Error, Aterm and count must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(change) != int and type(change) != float and type(change) != str:
        raise TypeError("Error, change must be an integer or float")
    elif type(change) == str:
        raise TypeError("Error, change is a string. Convert it to integer or float first")
    #=====end of checking

    retlist = list()

    x = compute_nterm(Anum,Aterm,change,1)

    if (count > 0):
        for i in range(count):
            retlist.append( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
    elif (count < 0):
        for i in range(Aterm-1,count-2,-1):
            retlist.append( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))

    return retlist

def generate_list_bylastterm(Anum, Aterm, Bnum, Bterm, count = None):
    '''
        Generate a list of arithmetic sequence given that you have:
            Anum of Aterm term  = the first given number and its position in the progression
            change              = changes per term
            count               = the number of terms you have in the progression
    '''

    #============checker
    if type(Aterm) != int or type(Bterm) != int:
        raise TypeError("Error, Aterm and Bterm must be an integer")

    if type(Anum) != int and type(Anum) != float and type(Anum) != str:
        raise TypeError("Error, Anum must be an integer or float")
    elif type(Anum) == str:
        raise TypeError("Error, Anum is a string. Convert it to integer or float first")

    if type(Bnum) != int and type(Bnum) != float and type(Bnum) != str:
        raise TypeError("Error, Bnum must be an integer or float")
    elif type(Bnum) == str:
        raise TypeError("Error, Bnum is a string. Convert it to integer or float first")

    if Aterm == Bterm:
        raise ValueError("Aterm and Bterm should'nt have the same value")

    if count != None and type(count) != int:
        raise TypeError("Error, count must be an integer")
    #=====end of checking

    change = compute_change(Anum,Aterm,Bnum,Bterm)

    retlist = list()

    x = compute_nterm(Anum,Aterm,change,1)

    if (count != None):
        if (count > 0):
            for i in range(count):
                retlist.append( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
        elif (count < 0):
            for i in range(Aterm-1,count-2,-1):
                retlist.append( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))

    else:
        for i in range(Bterm):
            retlist.append( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))

    return retlist

def generate_iter_bycount(Anum, Aterm, change, count=None):
    '''
        Generate a list of arithmetic sequence given that you have:
            Anum of Aterm term  = the first given number and its position in the progression
            change              = changes per term
            count               = the number of terms you have in the progression
    '''

    x = compute_nterm(Anum,Aterm,change,1)

    if count != None:
        if (count > 0):
            for i in range(count):
                yield ( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
        elif (count < 0):
            for i in range(Aterm-1,count-2,-1):
                yield ( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
    else:
        i = 0
        while True:
            i += 1
            yield ( int(x + (i - 1) * change) if float(x + (i - 1) * change).is_integer() else (x + (i - 1) * change))

def generate_iter_bylastterm(Anum, Aterm, Bnum, Bterm, count = None):
    '''
        Generate a list of arithmetic sequence given that you have:
            Anum of Aterm term  = the first given number and its position in the progression
            change              = changes per term
            count               = the number of terms you have in the progression
    '''

    change = compute_change(Anum, Aterm, Bnum, Bterm)
    x = compute_nterm(Anum,Aterm,change,1)

    if count != None:
        if (count > 0):
            for i in range(count):
                yield ( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
        elif (count < 0):
            for i in range(Aterm-1,count-2,-1):
                yield ( int(x + (i) * change) if float(x + (i) * change).is_integer() else (x + (i) * change))
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





