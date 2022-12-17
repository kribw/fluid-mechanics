from os import scandir
from math import sqrt, pow


def calc_length(u: float, v: float, w: float) -> float:
    # Get length of vector
    return sqrt(pow(u, 2) + pow(v, 2) + pow(w, 2))


file_dir = "G:\\Fluid Mechanics\\28.11.2022\\timesteps\\"


def parse_files():
    while True:
        line = file_in.readline()

        if (line == ""):
            print("EOF")
            break
        elif ("mesh" in line.lower()):
            line = file_in.readline()
            words = line.split()
            time = words[6]
            file_out = open(f"{file_dir}\\parsed\\{time}.txt", "w")
            file_in.readline()
            file_out.write("x,y,vel\n")
        elif (len(line.strip()) == 0):
            file_out.close()
        elif ("vf3" in line.lower()):
            # Skip line
            continue
        else:
            words = line.split()
            vf = float(words[3])

            if (0.0 < vf < 1.0):
                length = calc_length(
                    float(words[4]), float(words[5]), float(words[6]))
                file_out.write(
                    f"{float(words[0])},{float(words[1])},{length}\n")


for entry in scandir(file_dir + "raw"):
    if (entry.is_file()):
        print(entry.path)
        print(entry.name)
        file_in = open(entry.path, "r")
        parse_files()
