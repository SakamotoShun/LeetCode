# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

s = "   fly me   to   the moon  "
arr = []
for i in s.split():
    if i != " ":
        arr.append(i)
final = len(arr[len(arr)-1])
print(final)