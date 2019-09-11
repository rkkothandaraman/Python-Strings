N=int(input())
li=[int(x) for x in input().split()]
if(len(li)==N):
    li.sort(reverse = True)
    newli=map(str,li)
    number=("".join(newli))
    print(int(number))