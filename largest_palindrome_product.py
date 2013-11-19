# Problem:
#   A palindromic number reads the same both ways. The largest palindrome made
#   from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest 
#   palindrome made from the product of two 3-digit numbers.
#
#   - From: http://projecteuler.net/problem=4

''' BRUTE FORCE '''

# Author: Jonathan Lebron (Github: jonathanlebron, Twitter: @_jlebron)
# Date: 11/8/2013

maxOut = 0

def isPalindrome(num):
    return str(num) == str(num)[::-1]
    
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        curr = i*j
        if isPalindrome(curr) and curr > maxOut:
            maxOut = curr
            
print maxOut

''' END BRUTE FORCE '''
