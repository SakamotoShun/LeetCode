output = ""
while columnNumber:
    columnNumber -= 1
    output = chr(65 + columnNumber % 26) + output
    columnNumber //= 26
return output