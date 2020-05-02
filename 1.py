from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 
plt.gray() 
digits = load_digits()
plt.matshow(digits.images[0]) 
plt.show() 
print(digits.data.shape)