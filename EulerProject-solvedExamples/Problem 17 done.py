#Euler 17

a = "assdfg"
print(len(a))


#def numbertotext(n):


one = [ "", "one", "two", "three", "four", 
		"five", "six", "seven", "eight", 
		"nine", "ten", "eleven", "twelve", 
		"thirteen", "fourteen", "fifteen", 
		"sixteen", "seventeen", "eighteen", 
		"nineteen"]; 

ten = [ "", "", "twenty", "thirty", "forty", 
		"fifty", "sixty", "seventy", "eighty", 
		"ninety"]; 

def numToWords(n, s): 
	str = ""; 
	if (n > 19): 
		str += ten[n // 10] + one[n % 10]; 
	else: 
		str += one[n]; 
	if (n): 
		str += s; 
	return str; 


def convertToWords(n): 
	out = "";  

	out += numToWords(((n // 1000) % 100), 
							"thousand"); 
	out += numToWords(((n // 100) % 10), 
							"hundred"); 
	if (n > 100 and n % 100): 
		out += "and"; 
	out += numToWords((n % 100), ""); 
	return out; 

n = 77764; 

print(convertToWords(n));

a = 1000
z = 0
for i in range(1, a+1):
    z = z + len(convertToWords(i))
print(z)
