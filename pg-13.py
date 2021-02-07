dict1 = {'maths': 100, 'science': 200}
dict2 = {'physics': 300, 'chemistry': 200,'computer': 50}
print("Dictionary before merging")
print(dict1)
print(dict2)
print("Dictionary after merging")
dict3 = dict1.copy() 
dict3.update(dict2)
print(dict3)


