n=input("enter sentence")
l=n.split()
Excluded_words=['and','is','are','to']
count=0
for each in l:
    if each in Excluded_words:
        count+=1
print("output:",count)
