def num(a):
    if a>0:
        return "Positive"
    elif a<0:
        return "Negative"
    else:
        return "Zero"
n=int(input("Enter no.:"))
print(f"The no. {n} is {num(n)}")
