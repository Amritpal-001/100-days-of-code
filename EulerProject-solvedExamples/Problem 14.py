MaxRepetition = 0
repetition = 0
InitialN = 0

for n in range(1 , 1000 ):
    InitialN = n
    print(n)
    while (n != 1) :
        if n%2 == 0 :
            n = int(n/2)
            repetition += 1
            print( InitialN , n , repetition)
        if n%2 != 0:
            n = int(3*n + 1)
            repetition += 1
            print( InitialN , n ,  repetition)
        if n == 1:
            break
    if n == 1:
        if MaxRepetition <= repetition:
            print (InitialN , MaxRepetition )
            MaxRepetition = repetition
            repetition  = 0 
