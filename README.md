This is my personal version of RSA.  
It contains several simple function to implement this class.  

## \_\_init__
You can customize your range generating the two prime numbers p and q.  
Just pass the minimum and the maximum when initializing the object.  

### Example: `ex = myRSA(10, 1000)`. 
Note that if the maximum is not greater than the minimum, the customization will be not taken effect.  
In this case, the maximum and the minimum will be set to default values, which are 100 and 1, respectively.  

## setRange
You can still adjust your range after initializating.  
Just pass them as passing them into the initialization.  

### Example: `ex.setRange(1, 100)`
The rule is the same as that of the initialization.  
