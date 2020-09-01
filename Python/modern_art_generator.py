import random
import numpy as np
from PIL import Image

a = np.full((512,512,3), 255, np.uint8)
for s in a:
    print(len(s))
Image.fromarray(a).show()