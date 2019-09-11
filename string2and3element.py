li=input().split()
newli=[]
for i in range(1,len(li)-1):
    temp=li[i]
    newli.append(temp[::-1])
li[1:len(li)-1]=newli
for i in range(len(li)):
    print(li[i],end=" ")
