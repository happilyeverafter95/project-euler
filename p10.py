'''
problem 10 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def is_prime(n): 
    max_divisor = round(n**0.5) + 1

    for i in range(2,max_divisor): 
        if n % i == 0: 
            return False
    return True

def below_2mill():
    output_sum = 0
    for i in range(2,2000000): 
        if is_prime(i): 
            output_sum += i
    return output_sum    
    
'''
Side note: honestly did not expect this brute force-esq solution to finish running 
It takes a while to run, but gets the result in around 1 min 
--> may come back to find a solution with better performance
'''