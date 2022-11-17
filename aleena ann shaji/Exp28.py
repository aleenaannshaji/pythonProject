def fact(num):
    print("Factors of 20 are: ")
    for i in range(1,num+1):
        if (num % i == 0):
            print(i)
fact(20)