num=int(input("Enter no.:"))
x=num
rev=0
while num!=0:
    y=num%10
    rev=rev*10+y
    num=num//10
print(f"The reverse of {num} is, {rev}")