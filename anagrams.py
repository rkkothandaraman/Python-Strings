S1=input()
S2=input()
count=0
new=''
if(len(S1)==len(S2)):
    for a in range(len(S1)):
        if S1[a] in S2:
            count=count+1
    if(count==4):
        print(1)
    else:
        print(0)
else:
    print(0)
