import sys
n=int(sys.stdin.readline())
l=int(sys.stdin.readline())
s=sys.stdin.readline()
s1=""
s2="abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    if(s[i]!=" "):
        s1=s1+s2[(ord(s[i])-97+l)%26]
    else:
        s1+=" "        
print(s1)
