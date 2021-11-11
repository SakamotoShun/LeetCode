# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

x = 4
# sqr = pow(x. 0.5) - > maths

i = 0
while i * i <= x:
    # since only need integer, as long as i**2 <= x, increase i
    i += 1

# -1 to round down
print(i-1)
