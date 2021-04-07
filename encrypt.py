# Encryption alogorithm.

def main():
    # Reading public RSA key.
    try:
        file = open("publicKey.txt", 'r')
    except FileNotFoundError:
        print("No public key found.")

    n = int(file.readline())
    e = int(file.readline())
    file.close()

    # Reading message to be encrypted.
    try:
        file = open("message.txt")
    except FileNotFoundError:
        print("No message to be encrypted found.")

    message = file.read()
    file.close()

    blockSize = 2
    encryptedMessage = []
    ciphertext = -1
    if (len(message) > 0):
        ciphertext = ord(message[0])

    for i in range(1, len(message)):
        if (i % blockSize == 0):
            encryptedMessage.append(ciphertext)
            ciphertext = 0
        # ASCII code in decimal is max 3 digits - shifting by 3 places.
        ciphertext = ciphertext * 1000 + ord(message[i])

    encryptedMessage.append(ciphertext)

    for i in range(len(encryptedMessage)):
        encryptedMessage[i] = str(encryption(encryptedMessage[i], e, n))

    # Creating string.
    encryptedMessage = " ".join(encryptedMessage)

    with open("encryptedMessage.txt", "w") as file:
        file.write(str(encryptedMessage))

def encryption(m, e, n):
    return pow(m, e, n)

main()



