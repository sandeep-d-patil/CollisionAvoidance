import numpy as np
import random
def computeObjects():
    """
    generates random numbers for the object centers and (x,y) dimensions of the objects
    Returns
    -------
    """
    object_center_x = [25, 100, 25, 75, 125, 25, 75, 125, 25, 75, 125, 25, 75, 125, 25]
    object_center_y = [25, 25, 75, 75, 75, 125, 125, 125, 75, 75, 75, 75, 75, 75, 25]
    object_center_z = [110, 135, 25, 25, 25, 25, 25, 25, 75, 75, 75, 125, 125, 125, 135]
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
dictb={}
listb=[]
for i in range(len(objects['center_x'])):
    listb.append(i)
    lista = []
    lista.append(i)
    for j in range(len(objects['center_x'])):
        if i != j and objects['center_z'][i] < objects['center_z'][j]:
            l1 = Point(objects['center_x'][i] - objects['x'][i] / 2, objects['center_y'][i] + objects['y'][i] / 2)
            r1 = Point(objects['center_x'][i] + objects['x'][i] / 2, objects['center_y'][i] - objects['y'][i] / 2)
            l2 = Point(objects['center_x'][j] - objects['x'][j] / 2, objects['center_y'][j] + objects['y'][j] / 2)
            r2 = Point(objects['center_x'][j] + objects['x'][j] / 2, objects['center_y'][j] - objects['y'][j] / 2)
            if doOverlap(l1, r1, l2, r2):
                lista.append(j)
                dicta[str(i)] = lista
dictb['base'] = listb
dicta.update(dictb)
alpha = {}
for key, value in dicta.items():
    if key != 'base':
        h_max = 0
        # if key in GetMaxFlow(dicta):
        print(key)
        h_init = 0
        i = 0
        while i < len(value):
            # print(i)
            if h_init == 0:
                h_init = 2 * objects['center_z'][value[i]]
                # print(h_init)
                # print(value[i])
            else:
                # print('h_z', objects['center_z'][value[i]])
                # print('h_init', h_init)
                h_init += 2 * (objects['center_z'][value[i]] - h_init)
                # print('h_init_after', h_init)
                # print('value', value[i])
            i += 1
        alpha[str(key)] = h_init
    else:
        h_in = []
        value_list =[]
        for i in  range(len(value)):
            h_in.append(2 * objects['center_z'][value[i]])
            value_list.append(value[i])
        v_index = h_in.index(max(h_in))
        alpha[str(value[v_index])] = max(h_in)