from matplotlib import pyplot as plt  
import numpy as np
X = np.load("source_data.npy")[0][1]
Y = np.load("pred_flow.npy")[1]
plt.subplot(121)
plt.imshow(X)
plt.title("real_out_flow")
plt.subplot(122)
plt.imshow(Y)
plt.title("pred_out_flow")
# plt.colorbar()
plt.show()
print()