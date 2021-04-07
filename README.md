# RSA public key cipher 
Developed in Python 3.6.8.

# Description
Program is divided into 3 files.
- RSA.py - generate keys.
Generating keys could be optimized by inputting file with previously generated prime numbers and simply taking random number from this set.

- encrypt.py - encryption algorithm.
Takes as input txt files with public key and message to be encrypted.
Saves encrypted message to the file encryptedMessage.txt
To encrypt message there is used function pow(m, n, e), where e and n numbers are read from the file containing the key and m is text to be encrypted.   

- decrypt.py - decryption algorithm.
Takes as input txt files with private key and encrypted message to be decrypted.
Saves decrypted message to the file decryptedMessage.txt
To encrypt message there is used function pow(c, d, n), where d and n numbers are read from the file containing the key and c is text to be decrypted.


# Algorithm  
![00](https://github.com/Kjablonska/RSA-public-key-cipher/blob/assets/algorithm_description.png)
