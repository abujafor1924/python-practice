
def id_prime(num):
    if num <2 :
        return  False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return  False
    return  True

for number in range(1,10):
    if id_prime(number):
        print(number)



