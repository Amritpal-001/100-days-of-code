def getPrimesBelowN(n=100):
    """ Sieve of Eratosthenes """
    from math import ceil
    roundUp = lambda n, prime: int(ceil(float(n) / prime))

    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []

    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primeList

getPrimesBelowN(n=100)
print (primeList(1))
