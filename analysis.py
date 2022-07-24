import numpy as np
data = np.load('map.npy')

# id = (0 < data) & (data < 255)
id = np.nonzero((0 < data) & (data < 255))
assert len(id[0]) == len(id[1]) == len(id[2]) == len(id[3])
print(len(id[0]))

print('min / max ', data[id].min(), data[id].max())
print('mean      ', data[id].mean())
