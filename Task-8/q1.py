import numpy as np
n = np.array([10,11,12,13,14])
print("original array:")
print(n)
p=5
new_n = np.zeros(len(n) + (len(n)-1)*(p))
new_n[::p+1] = n
print("\nNew array:")
print(new_n)