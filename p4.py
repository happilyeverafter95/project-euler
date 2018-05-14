# -*- coding: utf-8 -*-

''' 
Problem 4: 
    
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

''' 

def is_palindrome(n): 
    if len(n) == 1 or (len(n) == 2 and n[0] == n[1]): 
        return True 
    else: 
        if n[0] != n[-1]: 
            return False
        else: 
            return is_palindrome(n[1:len(n)-1])

def largest_palindrome(): 
    palindrome = [] 
    for i in range(0,1000): 
        for j in range(0,1000): 
            n = i*j
            if is_palindrome(str(n)): 
                palindrome.append(n) 
    return max(palindrome) 
                