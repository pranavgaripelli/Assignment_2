from numpy import random;
import numpy as np;
a=random.randint(20, size=(15))
b = a.reshape(3,5)
print(b)
print(b.shape)
new_a = np.where(b == [
   [i]
   for i in np.amax(b, axis = 1)
], 0 ,b)
print(new_a)