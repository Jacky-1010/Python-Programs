def fact(n):
    for i in range(1,n):
        n=n*i
    return n
n=int(input("Enter no.:"))
print(f"The factorial of {n} is {fact(n)}")
    
