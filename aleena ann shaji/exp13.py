str1=input("Enter the first string: ")
a=str1[0]
str2=input("Enter the second string: ")
b=str2[0]
new_str1=b+str1[1:]
new_str2=a+str2[1:]
print(new_str1+" "+new_str2)