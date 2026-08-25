n=int(input("Enter no.:"))
x=n
if n>0:
    for i in range(1,n):
        n =n*(x-i)
    print(f"The factorial of {x} is {n}")
elif n==0:
    print(f"The factorial of {x} is {1}")
else:
    print("Invalid Input")

