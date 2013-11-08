# Description:
#     The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#     Find the sum of all the primes below two million.
#     - From http://projecteuler.net/problem=10

''' SIEVE OF ERATOSTHENES '''
# Author: Jonathan Lebron (Github: jonathanlebron, Twitter: _jlebron)
# Date: 11/8/2013

import math, time

start =  time.clock()

num = 2000000
total = (num-1) * num / 2 # total of all numbers
total -= 1 # subtract 1 since it is not prime
primes = [1]*num

m = int(math.sqrt(num))+1
for i in xrange(2, m):
    if primes[i] == 1:
        # if number is prime, set all multiples to 0
        # and subtract from total
        for j in xrange(i*2, num, i):
            if primes[j] == 1:
                primes[j] = 0
                total -= j

end = time.clock() - start

print "answer is: ", total
print "took ", end, " seconds"

''' END SIEVE OF ERATOSTHENES '''
