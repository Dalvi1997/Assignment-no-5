n=input("enter string")
l=n.split()
longest_word = []
for each in l:
    if len(each) > len(longest_word):
        longest_word = each
print ("output:",longest_word)
