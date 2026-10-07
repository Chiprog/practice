'''Consider the string "adfa" and the following rules:

Each character MUST be changed either to the one before or the one after in alphabet.
Characters a can only be changed to b and z to y.
For some example strings, we get:

"adfa" -> ["begb","beeb","bcgb","bceb"]
"bd" -> ["ae","ac","ce","cc"]

We see that in each example, one of the outcomes is a palindrome. That is, "beeb" and "cc".

You will be given a lowercase string and your task is to return True if at least one of the outcomes is a palindrome or False otherwise.'''

def solve(st):
    if len(st) == 1:
        return True
    avchar = []
    for a in range(len(st)//2):
        print (a, a + 1)
        if not(
            ((ord(st[a])+1) == (ord(st[-(a+1)])+1)) or
            ((ord(st[a])-1) == (ord(st[-(a+1)])+1)) or
            ((ord(st[a])+1) == (ord(st[-(a+1)])-1)) or
            ((ord(st[a])-1) == (ord(st[-(a+1)])-1))
            ):
            return False
    return True
