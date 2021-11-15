# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it

def check(i, j):
    if i == j or j == 0:
        final[i].insert(j, 1)
    else:
        final[i].insert(j, final[i-1][j-1] + final[i-1][j])
        
final = [[] for y in range(numRows)]


for i in range(numRows):
    for j in range(i+1):
        check(i, j)
        
return final