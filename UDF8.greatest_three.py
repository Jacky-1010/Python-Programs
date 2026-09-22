def great(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
n1=int(input("Enter first no."))
n2=int(input("Enter second no."))
n3=int(input("Enter third no."))
print(great(n1,n2,n3),"is the greatest")
    
