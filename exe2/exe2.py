#!/usr/bin/python

from PIL import Image
import numpy as np
import sys

def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        exit(1)

    print(sys.argv[1])
    img = Image.open(sys.argv[1], mode="r", formats=['BMP'])

    


main()
