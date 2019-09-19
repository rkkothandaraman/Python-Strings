S1=input()
if(len(S1)==10):
    W=S1[:5]
    N=S1[5:9]
    P=S1[9:]
    if '0' in N:
        print('not pan')
    elif(W.isupper() and N.isnumeric() and P.isupper()):
        print('pan')
    else:
        print('not pan')
else:
    print('not pan')
    
    
    
    
