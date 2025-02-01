# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re

text = sys.stdin.read().splitlines()[1:]
HEX_pattern = r"[#][0-9a-f]{3,6}"

index_list = []
line_list = []
match = ''

i = 0 
for line in text:
    if not re.search(r"^(#|{|})", line): 
        index_list.append(i)
    i+=1
                    
for index in index_list:
    line_list.append(text[index])

                        
match ='\n'.join(re.findall(HEX_pattern, ''.join(line_list), flags=re.I))
print(match)


# Sample inpit
# Selector
# {
# 	Property: Value;
# }

