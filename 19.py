M = [31,28,31,30,31,30,31,31,30,31,30,31]

#1/1/1901 was a tuesday
day = 2
sundays = 0

for year in range(1901,2001):
	for m in M:
		day += m
		if year % 4 == 0 and m == 28:
			day += 1
		if (day + 1) % 7 == 0:
			sundays += 1
print(sundays)
