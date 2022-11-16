import csv


def main():
    path = "C:/Code/-- Fluid Mechanics/flow3d/"
    file_in = open(path + "2Timesteps_from1-39_to1-4.txt", "r")
    file_out = open(path + "test.txt", "w")

    for x in range(9):
        file_in.readline()

    file_out.write("x,y,z,u,v,w\n")
    for line in file_in.readlines():
        if(line.count("0.000") > 0) or (len(line) == 0):
            continue

        if(line.count("Mesh") > 0):
            for x in range(4):
                file_in.readline()

        words = line.strip().split(" ")
        for word in words:
            word = word.strip()

            if(len(word) > 0):
                file_out.write(word[:5] + ",")
        file_out.write("\n")

    file_in.close()
    file_out.close()


def test():
    word = " "
    stripped = word.strip()
    print(len(word))
    print(len(stripped))


# test()
main()
