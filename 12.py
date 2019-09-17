import math

def count_divisors(n):
	cnt = 0 
	for i in range(1, (int)(math.sqrt(n)) + 1):
		if (n % i == 0):
			if (n / i == i):
				cnt = cnt + 1
			else:
				cnt = cnt + 2
	return cnt

def get_triangle(n):
	tri = 0	
	for n in range(n,0,-1):
		tri = tri + n
	return tri

#print(get_triangle(7))

num = 7
tri = 0
div = 0

for num in range(num, 1000000):
	x = get_triangle(num)
	y = count_divisors(x)
	#print(x, y)
	if y > 500:
		print("triangle is:", x)
		print("# of divisors:", y)
		break
	else:
		num += 1

