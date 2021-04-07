# Decription algorithm.

def main():
    # Reading private RSA key.
    try:
        file = open("privateKey.txt", 'r')
    except FileNotFoundError:
        print("No private key found.")

    n = int(file.readline())
    d = int(file.readline())
    file.close()

    try:
        file = open("encryptedMessage.txt", 'r')
    except FileNotFoundError:
        print("No encrypted message found.")

    encryptedMessage = []
    encryptedMessage = file.read()
    file.close()

    blockSize = 2
    decryptMessage = []

    # Create integer list from given message (string).
    listNumbers = encryptedMessage.split(' ')
    for number in listNumbers:
        decryptMessage.append(int(number))

    message = ""

    # Decrypt each integer from the decryptMessage list and save it as character (ASCII code).
    for i in range(len(decryptMessage)):
        decryptMessage[i] = decrypt(decryptMessage[i], d, n)
        tmp = ""

        # Convert each ineteger into ASCII code character.
        for j in range(blockSize):
            tmp = chr(decryptMessage[i] % 1000) + tmp
            decryptMessage[i] //= 1000
        message += tmp

    print("Decrypted message: ")
    print(message)
    with open("decryptedMessage.txt", 'w') as file:
        file.write(str(message))


def decrypt(c, d, n):
    return pow(c, d, n)


main()

