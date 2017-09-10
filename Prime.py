def obtain_prime(num):

    for i in range(2,num): 
        if num%i != 0:
            isPrime = True
        else:
            isPrime = False
            break

    if isPrime is True:
        return num

def obtain_range(num):

    primeGenerator = (obtain_prime(num) for num in range(3,num))
    
    return primeGenerator