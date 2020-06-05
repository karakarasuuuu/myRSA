from myRSA import *

if __name__ == '__main__':
    sender = myRSA()

    pe = int(input("Enter the partner's e: "))
    pn = int(input("Enter the partner's n: "))

    key = input("Enter your key: ")

    sender.setPartnerKey((pe, pn))

    print(sender.encrypt(key))