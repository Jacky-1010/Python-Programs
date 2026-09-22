def prime(n):
    if n<=0:
        return "Invalid"
    elif n==1:
        return "Not Prime"
    else:
        for i in range(2,n):
            if n%i==0:
                return "Not Prime"
                exit()
        return "Prime"
n=int(input("Enter no.:"))
print(n,"is",prime(n))
        
