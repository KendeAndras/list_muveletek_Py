def palindrom(x):
    v=True
    for i in range(len(x)):
        if x[i]!=x[-1-i]: v=False
    return v

words=input("Adjal szavakat ").split()

palindrom_worlds=[]
for i in words:
    if palindrom(i)==True: palindrom_worlds.append(i)

palindrom_worlds2=list(filter(palindrom,words))

print("palindrom szavak: ", palindrom_worlds)