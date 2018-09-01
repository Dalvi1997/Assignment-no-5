n=input("enter sentence")
w=input("enter word")
count=0
l=n.split()
for each in l:
    if(each==w or each==w.capitalize() or each==w.upper() or each==w.lower()):
        count+=1
print("output:",w,":",count)
