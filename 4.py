def is_Palindrome(num):
    a=str(num)
    b=str(num)[::-1] #extended slice [begin:end:step]

    if a == b:
        return True
    else:
        return False

p = 0
min = 100
max = 1000

for x in range(min,max):
    for y in range (min,max):
        if is_Palindrome(x*y):
            if x*y > p:
                p = x*y
                print(p)
        y += 1
    x += 1
