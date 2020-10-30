import time
#natural number
answer = 0
n = 1
n2 = 0
n1 = 2
y = 0
length = 4000000

start = time.time()
while n2 <= (length):
   #n1 = n1 + n
   n2 = n1 + n
   if ((n2 % 2) == 0 ):
     answer = answer + n2 + 2
   n = n1
   n1 = n2
end = time.time()
totaltime = (end - start)
print (answer , totaltime)
   
