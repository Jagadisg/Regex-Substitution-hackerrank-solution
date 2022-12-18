# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:

# && → and
# || → or
# Both && and || should have a space " " on both sides.
import re
n = int(input())
s = ""
for i in range(n):
        s += input() + '\n'
# solution 1        
def m(matched):
    if matched.group(0) == ' &&':
        return ' and'
    else:
        return ' or'
    
print(re.sub(r'( &&)(?= )|( \|\|)(?= )',m,s))


# solution 2
s = re.sub(r'( &&)(?= )',' and',s)
s = re.sub(r'( \|\|)(?= )',' or',s)
print(s)
