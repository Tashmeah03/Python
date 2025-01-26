import numpy as np
np_height =np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight =np.array([60.5, 70.6, 56.89, 45.7, 20])
meas= np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)