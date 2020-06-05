from myRSA import *

if __name__ == '__main__':
    sender = myRSA()

    key = input("Enter the partner's key: ")
    key = key.strip('{}') # To take {} away
    key = key.split(', ') # By now the key is a list containing integers that are strings actually
    key = tuple(int(n) for n in key) # And now the integers are really integers

    sender.setPartnerKey(key)

    plaintext = input("Enter the key: ")

    print(sender.encrypt(plaintext))