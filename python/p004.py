
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def getLargestPalindromeProduct():
	largestPalindrome = 1
	x = 1
	#y = 1
	while x <= 999:
		y = 1
		while y <= 999:
			product = x * y
			if str(product) == str(product)[::-1]:
				#print 'palindrome: '+str(product)
				largestPalindrome = product
			y = y + 1
		x = x + 1
	return largestPalindrome

if __name__ == "__main__":
	print getLargestPalindromeProduct()