import sys
s=sys.stdin.readline()
nb=0
for i in range(len(s)-1):
    nb+=ord(s[i])-96    
print(nb)
