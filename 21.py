
x = 10000

arr = [[] for z in range(x)]

def sum_div(n):
	d = []
	for i in range(1,n):
		if n % i == 0:
			d.append(i)
	return sum(d)

def get_div(n):
	arr = [[i] for i in range(n)]
	for j in range(n):
		arr[j].append(sum_div(j))
	return arr

div = get_div(x)
sum = 0

for i in range(x):
	for j in range(x):
		if i != j:		
			if div[i][0] == div[j][1] and div[i][1] == div[j][0]:			
				#print(i)			
				sum+=i
print(sum)

