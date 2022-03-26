import sys
x=sys.stdin.readline()
x=int(x)
a=4294967296
for i in range(x):
    y=sys.stdin.readline()
    y=int(y)
    if(y>=34):
        print(0)
    else:
        rep=1
        for j in range(1,y+1,1):
            rep=rep*j
        print(rep%a)
