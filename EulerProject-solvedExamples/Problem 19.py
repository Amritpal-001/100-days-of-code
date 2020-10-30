



def daysince1901( d , m  , y):
    y1 = y - 1900
    if y % 4 == 0 :    
        tillyear = (3*365* (y1 /4) + ((y1 / 4) - 1)*366 )
        feb = 29
    if y % 4 != 0 :
        leap = (y1 - (y1%4) )/4
      #  tillyear =  ( 3*365*((y1 - (y1%4)) / 4) + (((y1 - (y1%4))/ 4) - 1)*366 + ((y1 % 4) - 1)*365 )
        tillyear = leap*366 + leap*3*365 + ((y%4)-1)*365
        feb = 28
    if m == 1 :
        tillmonth = 0
    if m == 2 :
        tillmonth = 31
    if m == 3 :
        tillmonth = 31 + feb
    if m == 4 :
        tillmonth =  0 + 31*2 + feb
    if m == 5 :
        tillmonth = 30*1 + 31 *2 + feb
    if m == 6 :
        tillmonth = 30*1 + 31 *3 + feb
    if m == 7 :
        tillmonth = 30*2 + 31 *3 + feb
    if m == 8 :
        tillmonth = 30*2 + 31 *4 + feb
    if m == 9 :
        tillmonth = 30*2 + 31 *5 + feb
    if m == 10 :
        tillmonth = 30*3 + 31 *5 + feb
    if m == 11 :
        tillmonth = 30*3 + 31 *6 + feb
    if m == 12 :
        tillmonth = 30*4 + 31 *6 + feb
        
    totaldays = tillyear+ tillmonth + d
    
    print("number of days = " , "on " , d , m , y , "is      ", totaldays , tillyear , tillmonth , d )


    return (totaldays)

def totalSundaySince1901(d , m , y):
     b = daysince1901(d,m,y) - 1
#     nameday = ('sunday , monday , tuesday , wednesday , thursday , friday , saturday )
     n = ((b-6) - ((b-6)%7) )/ 7
     #first sunday was 7th JAn 1901
     print("number of Sundays since 1 jan 1901 on  ", d, m , y  , "is" , n , b)

daysince1901( 31 , 12 , 2000)
daysince1901( 31 , 12 , 1901)
daysince1901( 31 , 12 , 1902)
daysince1901( 31 , 12 , 1903)
daysince1901( 31 , 12 , 1904)
totalSundaySince1901( 31 , 12 , 2000)  
     
