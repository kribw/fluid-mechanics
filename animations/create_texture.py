import numpy
import imageio
import random
from os import scandir

X, Y = 184, 206
x_max = 53.556301
x_min = -60.432556
y_max = 66.366714
y_min = -61.222099
# image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)

# Colors
# 25.0 -> 250, 0, 0
# 21.875 -> 242, 161, 0
# 18.75 -> 220, 220, 0
# 15.625 -> 161, 242, 0
# 12.5 -> 0, 250, 0
# 9.375 -> 0, 242, 161
# 6.25 -> 0, 220, 220
# 3.125 -> 0, 161, 242


def get_color(vol_frac: float) -> tuple:
    # Get color for volume fraction
    if (vol_frac >= 25.0):
        return (250, 0, 0)
    elif (vol_frac >= 21.875):
        return (242, 161, 0)
    elif (vol_frac >= 18.75):
        return (220, 220, 0)
    elif (vol_frac >= 15.625):
        return (161, 242, 0)
    elif (vol_frac >= 12.5):
        return (0, 250, 0)
    elif (vol_frac >= 9.375):
        return (0, 242, 161)
    elif (vol_frac >= 6.25):
        return (0, 220, 220)
    elif (vol_frac >= 3.125):
        return (0, 161, 242)
    else:
        return (0, 207, 207)


def gen_random() -> None:
    # Generate texture with random pixels (testing)
    for i in range(Y):
        for j in range(X):
            image[i, j] = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
    imageio.imwrite('output.png', image)


def gen_rgb() -> None:
    # Generate texture with stripes colors (testing)
    # print(image[1:100])
    image[:200] = (255.0, 0.0, 0.0, 0.0)
    image[200:400] = (255.0, 255.0, 0.0, 0.0)
    image[400:600] = (255.0, 255.0, 255.0, 0.0)
    image[600:800] = (0.0, 255.0, 255.0, 1.0)
    image[800:] = (0.0, 0.0, 255.0, 1.0)

    imageio.imwrite('output.png', image)


def set_index(x: float, y: float, vf: float) -> None:
    # Find index for coordinates in image

    # x_index = abs(abs(int((x - abs(x_max)) / 0.62)) - X + 1)
    # y_index = abs(int((y - abs(y_max)) / 0.62))
    x_index = abs(abs(int((x - x_max) / 0.62)) - X + 1)
    y_index = abs(int((y - y_max) / 0.62))
    # print(f"x: {x_index}, y: {y_index}")
    image[y_index, x_index] = get_color(vf)


def fill_test():
    # Test function to partially fill image
    for i in range(int(Y / 2)):
        for j in range(int(X / 3)):
            image[i][j] = (255, 0, 0)


def fill_empty_values():
    # First we fill x-direction
    for i in range(Y):
        if (numpy.all(image[i][0:X-1] == 0)):
            continue

        for j in range(X):
            if (numpy.all(image[i][j] == 0)):
                if (j > X / 2):
                    # Go left
                    for k in reversed(range(0, j)):
                        if not (numpy.all(image[i][k] == 0)):
                            image[i][j] = image[i][k]
                            break
                else:
                    # Go right
                    for k in range(j, X):
                        if not (numpy.all(image[i][k] == 0)):
                            image[i][j] = image[i][k]
                            # image[i][j] = (255, 0, 0)
                            break

    # Then we fill y-direction
    for i in range(X):
        if (numpy.all(image[0:Y-1][i] == 0)):
            continue

        for j in range(Y):
            if (numpy.all(image[j][i] == 0)):
                if (j > Y / 2):
                    # Go up
                    for k in reversed(range(0, j)):
                        if not (numpy.all(image[k][i] == 0)):
                            image[j][i] = image[k][i]
                            break
                else:
                    # Go down
                    for k in range(j, Y):
                        if not (numpy.all(image[k][i] == 0)):
                            image[j][i] = image[k][i]
                            # image[i][j] = (255, 0, 0)
                            break


def create_texture():
    file_in.readline()

    for line in file_in.readlines():
        # x, y, vel
        words = line.split(",")
        set_index(float(words[0]), float(words[1]), float(words[2]))

    fill_empty_values()
    imageio.imwrite(f"animations/textures/{file_name}.png", image)


path = "G:\\Fluid Mechanics\\28.11.2022\\timesteps\\parsed\\"

for entry in scandir(path):
    if (entry.is_file()):
        image = numpy.zeros((Y, X, 3), dtype=numpy.uint8)
        print(entry.name)
        file_in = open(entry.path, "r")
        file_name = entry.name
        create_texture()
