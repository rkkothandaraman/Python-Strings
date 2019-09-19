N=input()
count=0
for i in range(1,len(N)-1):
    if(N[i]==N[i-1] and N[i]==N[i+1]):
        N=N[:i]+'@'+N[i:]
        count=count+1
print(count)
