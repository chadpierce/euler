f = 'numbers.txt'
with open(f, "r") as ins:
	array = []
	for line in ins:
		array.append(line)

newArray = []
for i in array:
	newArray.append(int(i))

#print(newArray)

arraySum = sum(newArray)
print(arraySum)
