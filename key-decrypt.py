from myRSA import *

if __name__ == '__main__':
    receiver = myRSA()
    
    receiver.generate()
    
    print("Enter the cipher text, -1 means EOF: ")
    ciphertext = []
    while True:
        c = int(input())
        if c == -1:
            break
        else:
            ciphertext.append(c)

    key = receiver.decrypt(ciphertext)
    
    print("The key is:", key)