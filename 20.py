
n = 100
p = 1

for i in range(n,0,-1):
	p = p * i

print(sum(map(int,str(p))))
