fruits=["cherry","guava","guava","apple","banana","cherry","grapes","strawberry"]
print("Original list:",fruits)
unq_list=[]
for i in fruits:
    if i not in unq_list:
        unq_list.append(i)

fruits=unq_list
print("Unique list:",fruits)
