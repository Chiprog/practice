'''
Codewariors: Nesting Structure Comparison

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''
def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) != len(other):
        return False
    for ori, oth in zip (original,other):
        if isinstance(ori,list) and isinstance(oth,list):
            if not same_structure_as(ori,oth):
                return False
        elif isinstance(ori,list) and not isinstance(oth,list):
            return False
        elif not isinstance(ori,list) and isinstance(oth,list):
            return False
    return True

#ps: this is my first use of recursion outside of learning. I prefer the use of logic stayements as they are easy to track. this kata had a test case against that
