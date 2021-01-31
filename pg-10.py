str1 = input("Enter a string : ")
char = str1[0]
str1 = str1.replace(char,'$')
str2 = char+str1[1:]
print(str2)