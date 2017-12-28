#2520
#this is brute force. it takes some time to run. 

def is_divisible(num):
    for div in range(1,21):
        if num % div != 0:
            return False
        if div == 20:
            return True

x=20
while True:
    if is_divisible(x):
        print(x)
        break
    x+=20
