import numpy as np
import matplotlib.pyplot as plt


def convolve_2d(array, kernel):
    m, n = kernel.shape
    y, x = array.shape
    y, x = y - m, x - m
    new_image = np.zeros((y, x))
    for i in range(y):
        for j in range(x):
            new_image[i, j] = np.sum(array[i:i + m, j:j + m] * kernel)
    return new_image


harvest = np.array()
fig, ax = plt.subplots(2)
im = ax[0].imshow(harvest)
fig.tight_layout()


kernel = np.array([
    [0.10, 0.10, 0.10],
    [0.10, 0.20, 0.10],
    [0.10, 0.10, 0.10]
]).T

convolved = convolve_2d(harvest, kernel)
im2 = ax[1].imshow(convolved)
fig.tight_layout()

plt.show()
