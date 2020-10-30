n = 100
b = []

for i in range (2,n+1):
    for j in range (2,n+1):
        a = i**j
        #print(a)
        if a not in b:
            b.append(a)

print(len(b))
