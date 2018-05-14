'''

Problem 9: 

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def py_triplet(): 
    for i in range(1,1000): 
        for j in range(1, 1000-i): 
            z = (i**2 + j**2)**0.5
            if i + j + z == 1000: 
                return i*j*z