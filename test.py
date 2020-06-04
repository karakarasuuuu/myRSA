import myRSA

if __name__ == "__main__":
    # Initialize two characters.
    sender = myRSA.myRSA()
    receiver = myRSA.myRSA()

    # Generate the public-key of the receiver.
    rpk = receiver.generate()

    # Set the public-key to the sender.
    sender.setPartnerKey(rpk)

    # Encrypting the message.
    message = input("Enter your plaintext: ")
    ciphertext = sender.encrypt(message)

    # Decrypt the message.
    plaintext = receiver.decrypt(ciphertext)

    print("Your message is:\n", plaintext)    