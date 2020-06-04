---
tags: GitHub
---
###### tags: `GitHub`

# myRSA
This is my personal version of RSA.  
It contains several simple function to implement this class.  

## \_\_init__
You can customize your range generating the two prime numbers p and q.  
Just pass the minimum and the maximum when initializing the object.  

### Example

#### `ex = myRSA(10, 1000)`. 
Note that if the maximum is not greater than the minimum, the customization will be not taken effect.  
In this case, the maximum and the minimum will be set to default values, which are 100 and 1, respectively.  

## setRange
You can still adjust your range after initializating.  
Just pass them as passing them into the initialization.  

### Example

#### `ex.setRange(1, 100)`
The rule is the same as that of the initialization.  

## generate
Since the sender does not necessarily to generate a key to send something, this part is separated.  
The return value will be a tuple containing the public-key.  

## setPartnerKey
By this function, the sender can set the public-key from the receiver up.  
The input should be a tuple, just like the output from `generate`.

## encrypt
After setting the public-key from the receiver, the sender can use this function to encrypt the message.  
The output will be a list containing several integers. And that's out ciphertext.  
The input should be a string, otherwise it will be rejected.

## decrypt
And the receiver can decrypt the ciphertext using this function.  
The input should be a list, which is the same as the output from `encrypt`.  

## showKey
Just in case you forget your public-key, you can check it by this function.  
The public-key will be shown on the screen, as well as a return value, which is a tuple.

## Functions that are not in the class

### is_prime
Used to check if a number is a prime number.  
Might be more optimized by decreasing the range in the `for-loop`.

### gcd
To calculate the greatest common divisor.  
It is not necessary to require the order of the input, since it will not cause any problem if the order is not correct, just needed one more calculation.