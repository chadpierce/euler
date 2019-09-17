

#read file, sort alpha
f = open('p022_names.txt','r')
n = f.read()
n = [x.strip('"') for x in n.split(',')]
n = sorted(n)

def get_score(name):
	s = 0
	for ch in name:
		s += (ord(ch)-64)	
	return s

total_score = 0
i = 1
for name in n:
	score = (get_score(name)) * i
	total_score += score
	i += 1
	
print(total_score)
