from myRSA import *

if __name__ == '__main__':
    receiver = myRSA()
    
    receiver.generate()
    
    ciphertext = input("Enter the ciphertext: ")
    ciphertext = ciphertext.strip('[]') # To take [] away
    ciphertext = ciphertext.split(', ') # By now the ciphertext is a list containing multiple integers that are strings actually
    ciphertext = [int(n) for n in ciphertext] # And now the integers are really integers

    key = receiver.decrypt(ciphertext)
    
    print("The plaintext is:", key)