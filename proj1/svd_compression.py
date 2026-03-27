import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
# load image 
img = Image.open("image.jpg").convert("L") #convert to grayscale
img_matrix=np.array(img)

# apply SVD
U, S, VT=np.linalg.svd(img_matrix)

# choose number of singular values
k =  100 

# Reconstruct compressed image
compressed = U[:, :k] @ np.diag(S[:k]) @ VT[:k, :    ]

# plot images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("original image")
plt.imshow(img_matrix, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title(f"Compressed Image (k={k})")
plt.imshow(compressed, cmap='gray')
plt.axis('off')

plt.show()