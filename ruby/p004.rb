#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def getLargestPalindrome()
	largestPalindrome = 1
	x = 1
	while x <= 999
		y = 1
		while y <= 999
			product = x * y
			if product.to_s == product.to_s.reverse!
				largestPalindrome = product
			end
			y = y + 1
		end
		x = x + 1
	end
	return largestPalindrome
end

puts getLargestPalindrome()

#just a reminder to yourself - ruby does not use indentation for scope