N=int(input("Enter total number of elements in the list : "))
lists=[]
int_n0=[]
print("Enter the numbers :")
for i in range(N):
    value=int(input(" "))
    lists.append(value)
print("Entered integer numbers",lists)
for num in lists: 
    if num >= 0: 
       int_n0.append(num) 
print("Entered positive integer numbers",int_n0)