''' A Hamming number is a positive integer of the form 2**i*3**j*5**k, for some
non-negative integers i,j and k.

write a function that computes the nth smallest hamming number.
Specifically:
- the first smallest Hamming number is 1 = (2**0)*(3**0)*(5**0)
- the second smallest Hamming number is 2 = (2**1)*(3**0)*(5**0)
- the third smallest Hamming number is 3 = (2**0)*(3**1)*(5**0)
- the fourth smallest Hamming number is 4 = (2**2)*(3**0)*(5**0)
- the fifth smallest Hamming number is 5 = (2**0)*(3**0)*(5**1)

compute the first 5000 hamming numbers
'''

'''
def hamming(n):
    num = 1
    count = 0
    while True:
        a = num
        while a%2 == 0:
            a //=2
        while a%3 == 0:
            a //=3
        while a%5 == 0:
            a //=5
        if a == 1:
            count += 1
        if count == n:
            break
        num += 1
    return num
'''
'''
def hamming(n):
    num = 1
    count = 0
    while True:
        a = num
        while a%2==0 or a%3 == 0 or a%5 == 0:
            if a%2 == 0 :
                a =a//2
            if a%3 == 0:
                a //=3
            if a%5 == 0:
                a //=5
        if a == 1:
            count += 1
        if count == n:
            break
        num += 1
    return num
'''
def hamming(n):
    i2 = i3 = i5 = 0
    hamm = [1]
    nextv = 1
    for i in range(1,n):
        next2 = hamm[i2] * 2
        next3 = hamm[i3] * 3
        next5 = hamm[i5] * 5
        nextv = min(next2, next3, next5)
        hamm.append(nextv)
        if nextv == next2:
            i2 += 1
        if nextv == next3:
            i3 += 1
        if nextv == next5:
            i5 += 1
    return nextv
print(hamming(5000))
                
