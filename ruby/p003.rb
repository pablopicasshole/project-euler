#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def getResult()

	n = 600851475143

	largestPrime = 1

	divisor = n

	i = 2
	while i < divisor
		if divisor % i == 0
			divisor = divisor / i
		end
		i = i + 1
	end
	return divisor
end

puts getResult().to_s
