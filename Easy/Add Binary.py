# Given two binary strings a and b, return their sum as a binary string.

a = "1010"
b = "1011"

# output = 10101

int_sum = int(a, 2) + int(b, 2)
bin_sum = bin(int_sum)
print(bin_sum[2:])