def opt(a,b):
    return a+b,a-b,a*b,a/b
n1=int(input("Enter first no.:"))
n2=int(input("Enter second no.:"))
add,diff,prod,quot=opt(n1,n2)
print("Sum: ",add)
print("Difference: ",diff)
print("Product: ",prod)
print("Quotient: ",quot)
