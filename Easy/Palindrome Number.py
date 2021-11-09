# checks if a number is a palindrome number.
# where it reads the same backwards

x = int(input('Enter a number:'))
numbers = [str(digits) for digits in str(x)]
pali_numbers = numbers[::-1]
print(pali_numbers == numbers)