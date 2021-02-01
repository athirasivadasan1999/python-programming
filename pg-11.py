str=input("Enter a string : ") 
count={}
str=str.lower()
words=str.split()
for word in words:
    if word in count:
        count[word]=count[word]+1
    else: 
        count[word]=1
for k,v in count.items() :
    print(k,v)
