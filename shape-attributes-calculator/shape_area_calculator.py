import abc
import logging
import logging.config
import yaml
import pprint
from pprint import pformat
import json

# logging.config.fileConfig('logging.conf')
# with open("logconf.yml", 'r') as f:
#     log_config = yaml.safe_load(f)
#     logging.config.dictConfig(log_config)
from logging_setting import *

logger = logging.getLogger(__name__)


shape_number_dict = {1: "rectangle", 2: "circle", 3: "cube", 4: "unknown"}


def calculate_area(name):

    # converting all characters into str then into lower cases
    name = str(name).lower()

    # check for the conditions
    if name.lower() == "rectangle" or str(name) == "1":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))

        # calculate area of rectangle
        rect_area = l * b
        logger.info(f"The area of rectangle is {rect_area}.")

    # elif name == "square":
    #     s = int(input("Enter square's side length: "))

    #     # calculate area of square
    #     sqt_area = s * s
    #     print(f"The area of square is {sqt_area}.")

    # elif name == "triangle":
    #     h = int(input("Enter triangle's height length: "))
    #     b = int(input("Enter triangle's breadth length: "))

    #     # calculate area of triangle
    #     tri_area = 0.5 * b * h
    #     print(f"The area of triangle is {tri_area}.")

    elif name.lower() == "circle" or str(name) == "2":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14

        # calculate area of circle
        circ_area = pi * r * r
        print(f"The area of triangle is {circ_area}.")

    elif name.lower() == "cube" or str(name) == "3":
        l = int(input("Enter cube's length: "))
        b = int(input("Enter cube's breadth: "))
        h = int(input("Enter cube's height: "))

        pi = 3.14

        # calculate area of circle
        cube_area = (l * b + b * h + l * h) * 2
        print(f"The area of triangle is {cube_area}.")

    # elif name == "parallelogram":
    #     b = int(input("Enter parallelogram's base length: "))
    #     h = int(input("Enter parallelogram's height length: "))

    #     # calculate area of parallelogram
    #     para_area = b * h
    #     print(f"The area of parallelogram is {para_area}.")

    else:
        print("Sorry! This shape is not available")


if __name__ == "__main__":

    print(f"Calculate Shape Area")
    shape_name = input(
        f"Please choose number of shapes:\n{pformat(shape_number_dict)}\nPlease Type in shape name or shape number:"
    )

    # function calling
    calculate_area(shape_name)
