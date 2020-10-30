#natural number
numberlist = []
n = 0
answer = 0
answer1 = 0
number = 0

while n < 100:
   n=n+1
   number = number + n
   answer = n*n
   answer1 = answer1 + answer
   print (answer1 , number*number , (number*number - answer1) )
