# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = 'MINIST.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')


# Print datatype of digits

print(digits.shape)

# Select and reshape a row
im = digits[-33, 1:]
#print(im)
print(im.shape)
im_sq = np.reshape(im, (28, 28))
#print(im_sq)
print(im_sq.shape)

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

