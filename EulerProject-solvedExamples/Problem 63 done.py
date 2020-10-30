
# Problem 63

#Brute force approach
Answerlist = []

for x in range(1,50):
    for n in range(1,50):
        y = x**n
        if len(str(y)) == n:
            if y not in Answerlist:
                Answerlist.append(y)
                print(y , n )

print(len(Answerlist))