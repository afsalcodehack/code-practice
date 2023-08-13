import numpy as np


class Student:
    def __init__(self, name):
        self.name = name;

    def getStudent(self, age):
        print(self.name);
        print("age:", age);

    @staticmethod
    def arrayDisplay():
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[1, 2, 3], [4, 5, 6]]
        c = np.add(a, b);
        print(np.matrix(c))
