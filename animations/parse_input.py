import csv
import pandas as pd


def main():
    path = "G:\\Fluid Mechanics\\flow3d\\"
    file_in = open(path + "flow_output_vf.txt", "r")
    file_out = open(path + "output.txt", "w")

    # Skip first line
    file_in.readline()

    file_out.write("x,y,z,u,v,w\n")
    for line in file_in.readlines():
        words = line.strip().split(" ")

    file_in.close()
    file_out.close()


main()
