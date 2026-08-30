list1=["alpha","beta","gamma","delta"]
list2=["beta","omega","delta","sigma"]
common_list=[]
print("First list:",list1)
print("Second list:",list2)
for i in list1:
    if i in list2:
        common_list.append(i)
print("Common Elements:",common_list)
