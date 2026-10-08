num=int(input("Enter no.:"))
x=num
digit=0
while num!=0:
    num=num//10
    digit+=1
num=x
a=[]
for i in range(digit):
    a.append(num%10)
    num=num//10
print(f"Sum of all digits in {x} is {sum(a)}")
