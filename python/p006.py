#	The sum of the squares of the first ten natural numbers is,

#	1^2+2^2+...+102^=385
#	The square of the sum of the first ten natural numbers is,

#	(1+2+...+10)^2=55^2=3025
#	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

#	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def getSumSquareDifference():
	sumSquareDifference = 0

	_sum = 0
	sumOfSquares = 0

	for i in range(1, 101):
		_sum = _sum + i
		sumOfSquares = sumOfSquares + (i ** 2)
	print(_sum)
	print(sumOfSquares)

	squareOfSum = _sum ** 2

	return squareOfSum - sumOfSquares



if __name__ == "__main__":
	print(getSumSquareDifference())