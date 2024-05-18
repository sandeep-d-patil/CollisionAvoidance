import numpy as np
from utils import Object, Point, overlap


def computeObjects():
    """
    generates a list of random objects with centers (x,y,z) and dimensions (x,y)
    Returns: list
    -------

    """
    objects = []
    for i in range(10):
        objects.append(Object())
    return objects




def main():
    objects = computeObjects()
    # print(objects[0])
    lista = []
    for i in range(len(objects)):
        for j in range(len(objects)):
            if i != j and objects[i].c_z > objects[j].c_z:
                l1 = Point(objects[i].c_x - objects[i].d_x / 2, objects[i].c_y + objects[i].d_y / 2)
                r1 = Point(objects[i].c_x + objects[i].d_x / 2, objects[i].c_y - objects[i].d_y / 2)
                l2 = Point(objects[j].c_x - objects[j].d_x / 2, objects[j].c_y + objects[j].d_y / 2)
                r2 = Point(objects[j].c_x + objects[j].d_x / 2, objects[j].c_y - objects[j].d_y / 2)
                if overlap(l1, r1, l2, r2):
                    lista.append((objects[i], objects[j]))

if __name__ == "__main__":
    main()
# lista = []
#
#
#
# for i in range(len(objects['center_x'])):
#     for j in range(len(objects['center_x'])):
#         l1 = Point(objects['center_x'][i] - objects['x'][i] / 2, objects['center_y'][i] + objects['y'][i] / 2)
#         r1 = Point(objects['center_x'][i] + objects['x'][i] / 2, objects['center_y'][i] - objects['y'][i] / 2)
#         l2 = Point(objects['center_x'][j] - objects['x'][j] / 2, objects['center_y'][j] + objects['y'][j] / 2)
#         r2 = Point(objects['center_x'][j] + objects['x'][j] / 2, objects['center_y'][j] - objects['y'][j] / 2)
#         if doOverlap(l1, r1, l2, r2):
#             lista.append((i,j))



    alpha = {}


    def calculate(k, alpha):
        if k in alpha.keys():
            h = alpha[k]
            return 2 * object[k] - h


    for key, value in dicta.items():
        if len(value) > 1:
            h_1 = 2 * objects['center_z'][int(key)]
            h_2 = 0
            while i < len(value):
                h_2 += 2 * (objects['center_z'][value[i]] - h_1)
            h_3 = 2 * (objects['center_z'][value[1]] - (h_2 + h_1))

import numpy as np
import random


def computeObjects():
    """
    generates an example numbers for the object centers and (x,y) dimensions of the objects
    Returns
    -------

    """
    object_center_x = [25, 100, 25, 75, 125, 25, 75, 125, 25, 75, 125, 25, 75, 125, 125]
    object_center_y = [25, 25, 75, 75, 75, 125, 125, 125, 75, 75, 75, 75, 75, 75, 75]
    object_center_z = [25, 25, 25, 25, 25, 25, 25, 25, 75, 75, 75, 125, 125, 125, 185]
    object_x = [50, 100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    object_y = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

    objects = {}
    # for i in range(0, 10):
    #     object_center_x.append(random.randint(0, 800))
    #     object_center_y.append(random.randint(0, 800))
    #     object_center_z.append(random.randint(0, 200))
    #     object_x.append(random.randint(0, 400))
    #     object_y.append(random.randint(0, 400))
    objects['center_x'] = object_center_x
    objects['center_y'] = object_center_y
    objects['center_z'] = object_center_z
    objects['x'] = object_x
    objects['y'] = object_y

    return objects


objects = computeObjects()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def doOverlap(l1, r1, l2, r2):
    # To check if either rectangle is actually a line
    # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}

    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        # the line cannot have positive overlap
        return False

    # If one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    # If one rectangle is above other
    if (r1.y >= l2.y or r2.y >= l1.y):
        return False

    return True


dicta = {}

for i in range(len(objects['center_x'])):
    lista = []
    # lista.append(i)
    for j in range(len(objects['center_x'])):
        if i != j and objects['center_z'][i] < objects['center_z'][j]:
            l1 = Point(objects['center_x'][i] - objects['x'][i] / 2, objects['center_y'][i] + objects['y'][i] / 2)
            r1 = Point(objects['center_x'][i] + objects['x'][i] / 2, objects['center_y'][i] - objects['y'][i] / 2)
            l2 = Point(objects['center_x'][j] - objects['x'][j] / 2, objects['center_y'][j] + objects['y'][j] / 2)
            r2 = Point(objects['center_x'][j] + objects['x'][j] / 2, objects['center_y'][j] - objects['y'][j] / 2)
            if doOverlap(l1, r1, l2, r2):
                lista.append(j)
                dicta[str(i)] = lista


def GetMaxFlow(flows):
    maks = max(flows, key=lambda k: len(flows[k]))
    return maks


for key, value in dicta.items():
    dicta[key].insert(0, int(key))

for key, value in dicta.items():
    h_max = 0
    if key in GetMaxFlow(dicta):
        # print(key)
        h_init = 0
        i = 0
        while i < len(value):
            print(i)
            if h_init == 0:
                h_init = 2 * objects['center_z'][value[i]]
                print(h_init)
                print(value[i])
            else:
                print('h_z', objects['center_z'][value[i]])
                print('h_init', h_init)
                h_init = 2 * (objects['center_z'][value[i]] - h_init)
                print('h_init_after', h_init)
                print('value', value[i])
            i += 1
    if h_max < h_init:
        h_max = h_init

