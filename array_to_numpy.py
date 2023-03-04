import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]

# make a red patch
data[1:3] = [255, 0, 0]

# make blue patch
data[3:] = [0, 0, 255]

data[:, 1:3] = [155, 0, 0] # all rows

data[1:4, 1:3] = [0, 255, 0]  # rows 1,2,3
img = Image.fromarray(data, "RGB")
img.save("canvas.png")
