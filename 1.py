import sys

max = int(sys.argv[1])
sum = 0
multiples = [3,5]

for i in range(1,max):
    
    for multiple in multiples:    

        if i % multiple == 0:
            sum += i
            print(i,":",sum)
            break #need this break so #s that are multiples of BOTH 3 and 5

print ("Grand total is:",sum)
