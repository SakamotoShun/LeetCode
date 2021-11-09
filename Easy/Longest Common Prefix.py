# starswith()
strs = ["flower","flow","flight"]

longest_prefix = ""
if not strs: print(longest_prefix)
shortest_prefix = min(strs, key=len)
for i in range(len(shortest_prefix)):
    if all([x.startswith(shortest_prefix[:i+1]) for x in strs]):
        longest_prefix = shortest_prefix[:i+1]
    else:
        break
print(longest_prefix)
