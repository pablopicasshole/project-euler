
#	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#	What is the 10 001st prime number?

def get10001stPrime():

	primes = [2]
	count = 1
	check = 1

	while count < 10001:
		isPrime = True
		for prime in primes:
			if check % prime == 0: 
				isPrime = False
				break
		if isPrime == True:
			count = count + 1
			primes.append(count)
			# print(primes)
		check = check + 1
	return check



if __name__ == "__main__":
	print(get10001stPrime())