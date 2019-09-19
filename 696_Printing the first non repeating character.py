def repeatingcharacter(string,c):
    res=0
    for i in range(len(string)):
        if (string[i] == c):
            res=res+1
    if res==1:
        return c
    if res>1:
        return True
N=input()
M=[]
for i in N:
    li=repeatingcharacter(N,i)
    if (li!=True):
        M.append(li)
if(len(M)==0):
    print(-1)
else:
    print(M[0])
