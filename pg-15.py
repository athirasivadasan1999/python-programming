def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    return fact    
number=int(input("Please a number to find factorial: "))
result=factorial(number)
print("The factorial of %d = %d"%(number,result))


