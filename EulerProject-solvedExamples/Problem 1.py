import time
#natural number
answer = 0
answer1 = 0
answer2 = 0
n = 0

start = time.time()
while n+1< 1000:
   n=n+1
   if ((n %3) == 0 ):
     answer = n + answer
   if (( n %5) == 0):
     answer1 = n + answer1
   if ((n %3) == 0) and (( n %5) == 0):
     answer2 = n + answer2
end = time.time()
print (n , answer + answer1 - answer2 , end - start)
   
