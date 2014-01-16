# Description:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
# - From http://projecteuler.net/problem=10

''' SIEVE OF ERATOSTHENES '''

# Author: Jonathan Lebron (Github: jonathanlebron, Twitter: _jlebron)
# Date: 11/8/2013

import math, time

start = time.clock()
num = 100000
primes = [True]*num
primes[0] = False
primes[1] = False

# Generate list of primes
m = int(math.sqrt(num))+1
for i in xrange(2, m):
    if primes[i]:
        # if number is prime, set all multiples to 0
        # and subtract from total
        for j in xrange(i*2, num, i):
            if primes[j]:
                primes[j] = False

count = 0
seen = {}
for i in xrange(2,num):
    if primes[i] and i not in seen:
        currNum = str(i)
        isCircularPrime = True # assume it is a circular prime
        numRotations = 1
        # iterate through each rotation and check if it is prime
        for j in xrange(1,len(currNum)):
            currRotation = currNum[j:]+currNum[:j]
            currInt = int(currRotation)
            if currInt != i:
                numRotations += 1
                seen[currInt] = True
                if not primes[currInt]:
                    isCircularPrime = False
                    break
        if isCircularPrime:
            count += numRotations

end = time.clock() - start
print "answer is: ", count
print "took ", end, " seconds"

''' END SIEVE OF ERATOSTHENES '''
