# (), {}, []
from os import close


def isValid(s):
        pairing =  dict(('()', '[]', '{}'))
        closed = []
        for i in s:
            if i in '([{':
                closed.append(i)
            elif len(closed) == 0 or i != pairing[closed.pop()]:
                return False

        return(len(closed) == 0)
    
    
print(isValid('(]'))