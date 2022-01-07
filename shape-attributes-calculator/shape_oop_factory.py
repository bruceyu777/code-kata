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


shape_number_dict = {1: "rectangle", 2: "circle", 3: "cube", 4: "universal", 5: "unkown"}


class Base_shape(abc.ABC):
    def __init__(self, friendly_name, *args, **kwargs):
        self._friendly_name = friendly_name
        self._name = None

    @property
    @abc.abstractmethod
    def measures(self):
        pass

    @abc.abstractclassmethod
    def calculate_area(self):
        pass

    # @abc.abstractclassmethod
    def calculate_volume(self):
        """by default, no volume calculating"""
        logger.warning(f"volume not availabe for {self.get_shape_type_name()}!")
        return "N/A"

    def get_shape_type_name(self):
        return self._name

    def get_shape_friendly_name(self):
        print(f"friendly name is <{self._friendly_name}>")
        return self._friendly_name

    def __str__(self) -> str:
        return f"{self.get_attributes_of_shape()}"

    def __repr__(self) -> str:
        return "<{}.{} ({})>".format(self.__class__.__module__, self.__class__.__name__, self)

    def get_attributes_of_shape(self):
        attribute_dict = {
            "type": self.get_shape_type_name(),
            "name": self.get_shape_friendly_name(),
            "measures": self.measures,
            "area": self.calculate_area(),
            "volume": self.calculate_volume(),
        }
        return attribute_dict

    def print_attributes_json(self):
        attribute_dict = self.get_attributes_of_shape()
        # logger.info(f"{pformat(attribute_dict)}")

        print(json.dumps(attribute_dict, indent=4, sort_keys=True))

    def print_attributes_str(self):
        attribute_dict = self.get_attributes_of_shape()
        print(attribute_dict)


class Circle(Base_shape):
    def __init__(self, friendly_name=None, radius=None):
        super().__init__(friendly_name)
        self._name = "circle"
        self._radius = radius
        # self.measures = {'raduis': self.radius}

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def measures(self):
        return {"raduis": self.radius}

    def calculate_area(self):
        pi = 3.14
        circ_area = pi * self.radius * self.radius
        return round(circ_area, 2)

    def calculate_volume(self):
        return super().calculate_volume()


class Rectangle(Base_shape):
    def __init__(self, friendly_name=None, length=None, breadth=None):
        super().__init__(friendly_name)
        self._name = "rectangle"
        self._length = length
        self._breadth = breadth

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def breadth(self):
        return self._breadth

    @breadth.setter
    def breadth(self, value):
        self._breadth = value

    @property
    def measures(self):
        return {"length": self.length, "breath": self.breadth}

    def calculate_area(self):
        rect_area = self.length * self.breadth
        return round(rect_area, 2)

    def calculate_volume(self):
        return super().calculate_volume()


class Cube(Base_shape):
    def __init__(self, friendly_name=None, length=None, breadth=None, height=None, **kwargs):
        super().__init__(friendly_name)
        self._name = "cube"
        self._length = length
        self._breadth = breadth
        self._height = height

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def breadth(self):
        return self._breadth

    @breadth.setter
    def breadth(self, value):
        self._breadth = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def measures(self):
        return {"length": self.length, "breath": self.breadth, "height": self.height}

    def calculate_area(self):
        cube_area = (self.length * self.breadth + self.length * self.height + self.breadth * self.height) * 2
        cube_area = round(cube_area, 2)
        return cube_area

    def calculate_volume(self):
        cube_volume = self.length * self.breadth * self.height
        cube_volume = round(cube_volume, 2)
        return cube_volume



def generate_shape(friendly_name, *args, **kwargs):

    arglist = list()
    if len(args) > 0:
        for arg in args:
            print(arg)
            if _is_float_or_int(arg):
                arglist.append(arg)
    if len(kwargs) > 0:
        for v in kwargs.values():
            print(v)
            if _is_float_or_int(str(v)):
                arglist.append(v)

    if len(arglist) == 1:
        print(f"1 valid measurement provided, assume it is a circle!")
        return Circle(friendly_name, *tuple(arglist))

    if len(arglist) == 2:
        print(f"2 valid measurement provided, assume it is a rectangle!")
        return Rectangle(friendly_name, *tuple(arglist))
    if len(arglist) >= 3:  # stop at processing the first 3 valid inputs
        print(f"3 or more valid measurement provided, assume it is a cube!")
        return Cube(friendly_name, arglist[0], arglist[1], arglist[2])


def _is_float_or_int(arg):
    int_flag = False
    float_flag = False

    try:
        int(arg)
        # logger(f"{arg} is a int")
        int_flag = True
    except ValueError:
        pass

    try:
        float(arg)
        logger.warning(f"{arg} is a float")
        float_flag = True
    except ValueError:
        pass

    return int_flag or float_flag


# class UniversalShape(Base_shape):
#     def __init__(self, friendly_name, *args, **kwargs):
#         super().__init__(friendly_name)
#         self.arglist = list()
#         if len(args) > 0:
#             for arg in args:
#                 print(arg)
#                 if _is_float_or_int(arg):
#                     self.arglist.append(arg)
#         if len(kwargs) > 0:
#             for v in kwargs.values():
#                 print(v)
#                 if _is_float_or_int(str(v)):
#                     self.arglist.append(v)
#         if len(self.arglist) == 1:
#             self._name = "circle"
#             self.radius = self.arglist[0]
#         if len(self.arglist) == 2:
#             self._name = "rectangle"
#             self.length = self.arglist[0]
#             self.breadth = self.arglist[1]
#         if len(self.arglist) >= 3:  # stop at processing the first 3 valid inputs
#             self._name = "cube"
#             self.length = self.arglist[0]
#             self.breadth = self.arglist[1]
#             self.height = self.arglist[2]

#     @property
#     def measures(self):
#         measures_dict = {}
#         for k, v in vars(self).items():
#             if "_name" not in k.lower():
#                 measures_dict.update({k: v})

#         return measures_dict

#     def calculate_area(self):
#         if self.get_shape_type_name() == "circle":
#             pi = 3.14
#             circ_area = pi * self.radius * self.radius
#             return round(circ_area, 2)

#         if self.get_shape_type_name() == "rectangle":

#             rect_area = self.length * self.breadth
#             return round(rect_area, 2)

#         if self.get_shape_type_name() == "cube":

#             cube_area = (self.length * self.breadth + self.length * self.height + self.breadth * self.height) * 2
#             return round(cube_area, 2)

#     def calculate_volume(self):
#         if self.get_shape_type_name() == "circle" or self.get_shape_type_name() == "rectangle":
#             return super().calculate_volume()

#         if self.get_shape_type_name() == "cube":
#             cube_volume = self.length * self.breadth * self.height
#             return round(cube_volume, 2)


def shape_attributes_calculator(name):
    # converting all characters into str, then into lower cases
    name = str(name).lower()

    # check for the conditions
    if name == "rectangle" or str(name) == "1":
        length = float(input("Enter rectangle's length: "))
        breadth = float(input("Enter rectangle's breadth: "))

        rectangle = Rectangle(length=length, breadth=breadth)

        print(f"The key attributes of rectangle:\n{pformat(rectangle.get_attributes_of_shape(), sort_dicts=False)}.")

    elif name == "circle" or str(name) == "2":
        radius = float(input("Enter circle's radius length: "))
        circle = Circle(radius=radius)
        print(f"The key attributes of circle:\n{pformat(circle.get_attributes_of_shape(), sort_dicts=False)}.")

    elif name == "cube" or str(name) == "3":
        length = float(input("Enter cube's length: "))
        breadth = float(input("Enter cube's breadth: "))
        height = float(input("Enter cube's height: "))

        cube = Cube(length=length, breadth=breadth, height=height)
        print(f"The key attributes of cube:\n{pformat(cube.get_attributes_of_shape(), sort_dicts=False)}.")

    elif name == "universal" or str(name) == "4":
        args = list()
        friendly_name = input("Please give a name for the universal shape: ")
        while True:
            a = input("Enter measurement(float or int) one by one or Stop by type in q: ")
            if a == "q":
                break
            if not _is_float_or_int(a):
                print(f"{a} is not a float or int, please input float or int!!")
                continue

            args.append(float(a))

        print(f"args list is {args}, tuple is {tuple(args)}")

        args_tuple = tuple(args)

        shape = generate_shape(friendly_name, *args_tuple)  #using object creator!!
        print(f"The key attributes of cube:\n{pformat(shape.get_attributes_of_shape(), sort_dicts=False)}.")

    else:
        print("Sorry! This shape is not available yet!")


if __name__ == "__main__":

    print(f"Calculate Shape Area")
    shape_name = input(
        f"Please choose number of shapes:\n{pformat(shape_number_dict)}\nPlease Type in shape name or shape number:"
    )

    # function calling
    shape_attributes_calculator(shape_name)
