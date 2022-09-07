print(x[4])
#x[4].shape

import matplotlib.pyplot as plt
import numpy as np
plt.imshow(np.reshape(x[4] , (8,8)) , cmap=plt.cm.gray)
plt.show()
