# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

n = 1

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
short_steps = 1
long_steps = 2

if n in (0, 1, 2):
    print(n)
else:
    for i in range(n-2):
        # level 4 = lvl 3 + level 2
        short_steps, long_steps = long_steps, short_steps+long_steps
    
    print(long_steps)