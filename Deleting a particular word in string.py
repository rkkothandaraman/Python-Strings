S1=input().split()
S2=input()
if S2 not in S1:
    for i in S1:
        print(i, end=" ")
elif S2 in S1:
    S1.remove(S2)
    for i in S1:
        print(i)
    
    
