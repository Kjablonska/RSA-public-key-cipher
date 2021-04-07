import math
import random

# Saves public and private RSA keys into file.
def main():
    [n, e, d] = generateKeys()

    file = open("publicKey.txt", "w")
    file.write(str(n) + '\n')
    file.write(str(e) + '\n')
    file.close()
    file = open("privateKey.txt", "w")
    file.write(str(n) + '\n')
    file.write(str(d) + '\n')
    file.close()

# Generates prime numer in range (1000, 10000+1)
def generatePrime():
    prime = []
    for num in range(1000, 10000 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    prime.append(num)
    y = len(prime)
    x = random.randint(1, y-1)
    return prime[x]

# Generates public RSA key.
def generateKeys():
    p = generatePrime()
    q = generatePrime()
    n = p * q
    totient = (p - 1) * (q - 1)
    e = getE(totient)
    x = getD(e, totient)

    # Checking if d is positive.
    if (x < 0):
        d = x + totient
    else:
        d = x

    print("Generating keys")
    print("Prime number p = ")
    print(p)
    print("Prime number q = ")
    print(q)
    print("n = p * q")
    print(n)
    print("totient(n) = (p - 1) * (q - 1)")
    print(totient)
    print("e = ")
    print(e)
    print("d = ")
    print(d)

    return [n, e, d]

# Finds coprime to totient.
def getE(totient):
    e = generatePrime()
    while greatestCommonDivisor(e, totient) != 1:
        e += 1
    return e

def getD(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        lastX, x = x, lastX - quotient * x
        lastY, y = y, lastY - quotient * y

    return lastX

# Euclid's Algorithm for finding greatest common divisor.
def greatestCommonDivisor(a, b):
    while b > 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main()

