#import wd
a = open('names.txt' , 'r')
if a.mode == 'r':
    contents = a.read()
#print(contents)

b = contents.split('","')
#print(b)
#print(len(b))

b.sort()
print(len(b))
print(b)

def Totalscore(z):
    score = 0
    c = [char for char in z]
    #print(c)
    for i in range(len(c)):
        b = c[i]
        if b == 'A':
            score += 1
        if b == 'B':
            score += 2
        if b == 'C':
            score += 3
        if b == 'D':
            score += 4
        if b == 'E':
            score += 5
        if b == 'F':
            score += 6
        if b == 'G':
            score += 7
        if b == 'H':
            score += 8
        if b == 'I':
            score += 9
        if b == 'J':
            score += 10
        if b == 'K':
            score += 11
        if b == 'L':
            score += 12
        if b == 'M':
            score += 13
        if b == 'N':
            score += 14
        if b == 'O':
            score += 15
        if b == 'P':
            score += 16
        if b == 'Q':
            score += 17
        if b == 'R':
            score += 18
        if b == 'S':
            score += 19
        if b == 'T':
            score += 20
        if b == 'U':
            score += 21
        if b == 'V':
            score += 22
        if b == 'W':
            score += 23
        if b == 'X':
            score += 24
        if b == 'Y':
            score += 25
        if b == 'Z':
            score += 26
    return(score)


ai = Totalscore("PRINT")
print(ai)

d= 0
for i in range(len(b)):
    word = b[i]
    #c = [char for char in word]
    #print(c)
    d += (i+1) * Totalscore(word)
    
print(d)
