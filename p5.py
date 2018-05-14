'''
problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def smallest_multiple(): 
    lst = [19,18,17,16,15,14,13,12,11,10] # only needs to be divisible by these numbers to be divisible by all nums 1-20 s
    max_num = 1
    for i in lst: 
        max_num *= i 
    for i in range(210, max_num,210): 
        is_divisible = True
        for j in lst:
            if i % j != 0: 
                is_divisible = False 
        if is_divisible: 
            return i 

