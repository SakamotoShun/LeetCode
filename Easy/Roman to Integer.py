# assign dict values
s = input('Enter Roman value: ')

roman = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000, }

sum = 0
num = 0

for i in range(len(s)-1, -1, -1):
    num = roman[s[i]]
    if num * 3 < sum:
        sum -= num
    else:
        sum += num
print(sum)