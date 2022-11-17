str=input("Enter the sentence: ")
print(str)
dict={}
word=str.split()
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print("The word occurence:")
for m,n in dict.items():
    print(m,n)