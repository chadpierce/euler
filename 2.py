max = 4000000
a = 1
b = 2
f = 0
even_sum = 2 #so 2 is included in even # sum

while (a | b < max):
    f = a+b
    if f % 2 == 0:
        print(f)
        even_sum += f
    a = b
    b = f

print("Even number sum is:", even_sum)
