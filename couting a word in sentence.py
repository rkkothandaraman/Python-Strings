N=input().split()
count=0
S=input()
for i in N:
    if(i==S):
        count=count+1
if(count>0):
    print(count)
else:
    print(-1)
