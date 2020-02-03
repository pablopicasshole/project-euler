#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#you idiot, if 3 is a factor of n then you can start looking for only up to n/3
#so when a factor is found, just change n to n/3

def getLargestPrimeFactor():

	n = 600851475143

	divisor = n

	i = 2#
	while i < divisor:
		if divisor % i == 0:
			#if i is a factor, the remaining factors lie in divisor/3
			#drastically reduces search range by eliminating lots of redundancy
			divisor = divisor / i 
			#return i
		i = i + 1

	#dividing the number by larger and larger factors until it can't be divided anymore 
	#means what we're left with is the largest prime factor
	#we have essentially widdled down n to reveal the large prime factor
	#that lies within it
	return divisor


if __name__ == "__main__":
	print getLargestPrimeFactor()

#maybe a better way is to have a loop that finds primes and we only test if
# it's a factor of n when we land on a prime
