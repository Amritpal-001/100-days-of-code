
totalsunday = 0
n = 1
m2 = 10
y2 = 1901
d2 = 1

d = 31
m = 12
y = 2000

while True:
    d1 = d2
    m1 = m2
    y1 = y2
    
    dcount = d1 % 7
    if dcount == 0 and m1 == 1:
        totalsunday += 1
    if (d1 == 31) and (m1 == 12):
        m2 == 1
        d2 == 1
        y2 = y2 + 1
        pass
    if d1 == 31 and (m1 == 1 or m1 == 3 or m1 == 5 or m1 == 7 or m1 == 10 or m1 == 8 ):
      d2 = 1
      m2 += 1
    elif d1 == 30 and (m1 == 4 or m1 == 6 or m1 == 11 or m1 == 9):
      d2 = 1
      m2 += 1
    elif d1 == 29 and (m1 == 2) and (y1 % 4 == 0):
      d2 = 1
      m2 += 1
    elif d1 == 28 and (m1 == 2 )and ((y1 % 4 )!= 0):
      d2 = 1
      m2 += 1
    
    d2 += 1
    print ( d1 , m1 , y1 , totalsunday )
    if (d1 == d )and (m1 == m) and (y1 == y):
        print ("final answer is ...... " ,  d , m , y , d1 , m1 , y1 , totalsunday )
        exit()
