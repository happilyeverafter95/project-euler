'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(n = 600851475143): 
    divisor = 2
    
    while n > 1: 
        if n % divisor == 0: 
            n /= divisor
        else: 
            divisor += 1
    
    return divisor