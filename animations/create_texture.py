import numpy
import imageio
import random

X, Y = 1000, 1000
image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)


def gen_random():
    for i in range(X):
        for j in range(Y):
            image[i, j] = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
    imageio.imwrite('output.png', image)


def gen_rgb():
    # print(image[1:100])
    image[:300] = (255, 0, 0)
    image[300:600] = (0, 255, 0)
    image[600:] = (0, 0, 255)

    imageio.imwrite('output.png', image)


gen_rgb()
# print(image[600:601])