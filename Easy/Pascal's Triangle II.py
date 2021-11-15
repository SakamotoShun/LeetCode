# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

prev = list()

for i in range(1, rowIndex+2):
    row = [1] * i
    if len(row) > 2:
        for j in range(len(prev)-1):
            row[j+1] = prev[j] + prev[j+1]
    prev = row
return row