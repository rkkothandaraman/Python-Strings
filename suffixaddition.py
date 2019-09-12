N=int(input())
li=list(map(int,input().split()))
newlist=[]
if(len(li)==N):
    for i in range(N):
        sum=0
        for j in range(N-1,i-1,-1):
            sum=sum+li[j]
        newlist.append(sum)
    for i in newlist:
        print(i, end=" ")
