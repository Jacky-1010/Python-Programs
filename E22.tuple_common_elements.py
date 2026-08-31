tup1=("Sun","Moon","Earth","Mars","Venus")
print(tup1)
tup2=("Mercury","Venus","Earth","Mars","Jupiter","Saturn")
print(tup2)
common_tup=[]
for i in tup1:
    if i in tup2:
        common_tup.append(i)
print("Common Elements:",tuple(common_tup))
