n=int(input("Enter the number of elements "))
print("Enter the elements")
list1=[]
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        list1.append("Over")
    else:
        list1.append(ele)
print(list1)

