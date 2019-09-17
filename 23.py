# awful brute force code that takes forever
M = 28123

def	is_abundant(n):
	sum = 0	
	for i in range(1,n+1):
		if n % i == 0 and i != n:
			sum += i	
	if sum > n:
		return True
	else:
		return False

def def_range(x):
	sub_max = 0
	sub_min = 0 
	for i in range(len(a)):	
		#note should remove the lower limit here. this should just return a max
		if a[i] < (x):
			#if sub_min == 0:
			#	sub_min = i
			sub_max = i
	return sub_min, sub_max

def is_sum_of_abun(x):
	#this is the slow part...whatever!
	sub_min, sub_max = def_range(x)
	for i in range(sub_min, sub_max+1):
		for j in range(sub_min, sub_max+1):
			if a[i] + a[j] == x:
				return True
	return False
	
#get all abundant #s less than M
a = []
for i in range(1,M+1):
	if is_abundant(i):
		a.append(i)

total = 0
for i in range(1,M+1):
	if not is_sum_of_abun(i):
		#printing may slow it down..but i wanted to make sure it was actually running!
		print('nope:',i)
		total += i
	else:
		print('yuup:',i)

print('TOTAL:', total)
