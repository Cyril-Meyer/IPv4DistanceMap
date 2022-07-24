import numpy as np

data = np.full((256, 256, 256, 256), 255, dtype=np.uint8)
np.save('map.npy', data)
