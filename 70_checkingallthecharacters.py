S1,S2=input().split()
count=0
if(len(S1)==len(S2)):
    for i in range(len(S1)):
        if(S1[i]!=S2[i]):
            count=count+1
    if(count==1):
        print('yes')
    else:
        print('no')
else:
    print('no')
