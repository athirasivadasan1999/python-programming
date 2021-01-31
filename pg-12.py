d={}
n=int(input("Total number of elements in dictionary : "))
print("Enter elements : ")
for i in range(n):
    d[i]=input(" ")
print("Ascending order")
print(sorted(d.items(), key = lambda kv:(kv[1], kv[0])))
print("Descending order")
print(sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
