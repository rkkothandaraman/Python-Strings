S1=input()
new=''
for a in S1:
    if a.isupper() == True:
        new=new+a.lower()
    elif a.islower() ==True:
        new=new+a.upper()
print(new)
        
