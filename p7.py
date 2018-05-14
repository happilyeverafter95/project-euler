'''
Problem 7 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def is_prime(n): 
    max_divisor = round(n**0.5) + 1

    for i in range(2,max_divisor): 
        if n % i == 0: 
            return False
    return True

def prime_10001(num = 10000): 
    primes = 0
    n = 1

    while primes <= num: 
        n += 1
        if is_prime(n) == True: 
            primes += 1            
    return n 