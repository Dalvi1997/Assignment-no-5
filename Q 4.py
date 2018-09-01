n=input("enter string")
w=input("enter word")
count=0
l=n.split()
a=len(l)
for each in l:
    if(each==w):
        count+=1
print("output:density:",count,"/",a)
