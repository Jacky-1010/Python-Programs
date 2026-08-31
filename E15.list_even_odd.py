#separating even and odd numbers in a list
num=[23,45,66,89,12,8,10,57,94]
print(num)
even_list=[]
odd_list=[]
for i in num:
    if i%2==0:
        even_list.append(i)
    elif i%2!=0:
        odd_list.append(i)
print("Even no. list:",even_list)
print("Odd no. list:",odd_list)
