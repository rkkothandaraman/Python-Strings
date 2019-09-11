N,K=input().split()
count=0
li=list(N)
li=list(map(int,li))
M=int(K)
for i in range(0,M+1,1):
    if i in li:
        count=count+1
if(count==M+1):
    print("yes")
else:
    print("no")
