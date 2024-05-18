import operator
from utils import overlap


def compute_objects():
    """
    generates objects with their properties centers (object_center_x, object_center_y, object_center_z)
    and dimensions of objects (X,Y).
    The objects created here are a part of example used for explanation,should be replaced by original compute_objects()
    Returns dict of objects with their centers (object_center_x, object_center_y, object_center_z) and
    dimensions of objects (object_x,object_y)
    -------

    """
    object_center_x = [25, 100, 25, 75, 125, 25, 75, 125, 25, 75, 125, 25, 75, 125, 25]
    object_center_y = [25, 25, 75, 75, 75, 125, 125, 125, 75, 75, 75, 75, 75, 75, 25]
    object_center_z = [110, 135, 25, 25, 25, 25, 25, 25, 75, 75, 75, 125, 125, 125, 165]
    object_x = [50, 100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    object_y = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

    objects = {'center_x': object_center_x, 'center_y': object_center_y, 'center_z': object_center_z, 'x': object_x,
               'y': object_y}

    return objects


def arrange_object(objects):
    """
    Creates a dictionary of list of objects stacked on each other
    Parameters
    ----------
    objects: dict of objects with centers and dimensions

    Returns dict of objects stacked on each other
    -------

    """
    dict_objects = {}
    dict_base = {}
    list_base = []
    for i in range(len(objects['center_x'])):
        list_base.append(i)
        list_objects = [i]
        for j in range(len(objects['center_x'])):
            if i != j and objects['center_z'][i] < objects['center_z'][j]:
                if overlap(objects['center_x'][i], objects['center_y'][i], objects['x'][i], objects['y'][i],
                           objects['center_x'][j], objects['center_y'][j], objects['x'][j], objects['y'][j]):
                    list_objects.append(j)
                    dict_objects[str(i)] = list_objects
    dict_base['base'] = list_base
    dict_objects.update(dict_base)
    return dict_objects


def get_object(dict_objects, objects):
    """
    For each set of objects, the max stacked height is calculated and the object with
    tallest height is printed
    Parameters
    ----------
    dict_objects: dict of center heights(z) of the objects
    objects: dict of objects with centers and dimensions

    Returns the object_id of the tallest object which also has highest center height(z)
    -------

    """
    alpha = {}
    for key, value in dict_objects.items():
        if key != 'base':
            h_init = 0
            i = 0
            while i < len(value):
                if h_init == 0:
                    h_init = 2 * objects['center_z'][value[i]]
                else:
                    h_init += 2 * (objects['center_z'][value[i]] - h_init)
                i += 1
            alpha[str(key)] = h_init
        else:
            h_in = []
            value_list = []
            for i in range(len(value)):
                h_in.append(2 * objects['center_z'][value[i]])
                value_list.append(value[i])
            v_index = h_in.index(max(h_in))
            alpha[str(value[v_index])] = max(h_in)
    max_value = max(alpha.items(), key=operator.itemgetter(1))[0]
    print('pick object:', max_value)
    return None


def main():
    # Compute the objects
    objects = compute_objects()
    # Arrange the objects
    object_dict = arrange_object(objects)
    # Get the tallest object at the highest center height
    get_object(object_dict, objects)


if __name__ == "__main__":
    main()

# Objects = compute_objects()
#
# Where
# objects -> {'center_x': object_center_x, 'center_y': object_center_y, 'center_z': object_center_z, 'x': object_x,
#             'y': object_y}
# pallet_size = (1000,1000)
# # Obtain a list of objects which are stacked on top each other
# for i in objects
#     list_base < - i
#     list_objects = [i]
#     for j in objects['center_x']:
#         if i not equal to j and objects['center_z'][i] < ob-jects['center_z'][j]:
#         if overlap(objects['center_x'][i], objects['center_y'][i], objects['x'][i], objects['y'][i],
#                    objects['center_x'][j], objects['center_y'][j],
#                    objects['x'][j], objects['y'][j])
#             list_objects < - j
#             dict_objects[“i”] = list_objects
# dict_base['base'] = list_base
# dict_objects < - dict_objects + dict_base
#
# # For the stack of objects, calculate the height of the box with respect to surface
# # For the objects which are at the topmost in their center -> (x,y)  and obtain their heights.
#
# for key, value in dict_objects
#     if key not 'base'
#     repeat
#     if h_init = 0
#     h_init = objects['center_z'][value[i]]
# else:
#     h_init = objects['center_z'][value[i]] - h_init
# until length(value)
# min_h_box[“key”] = h_init
# else
# for i in value
#     h_in < - objects['center_z'][value[i]]
#     value_list < - value[i]
#     # v_index = index of h_in (min(h_in))
#     min_h_box[“value”] = min(h_in)
#     # From the above objects find the object with lowest height.
#
# for k in min_h_box:
#     for i in objects:
#         l1 = Point(objects['center_x'][i] - (objects['x'][i] / 2), objects['center_y'][i] + (objects['y'][i] / 2))
#         r1 = Point(objects['center_x'][i] + (objects['x'][i] / 2), objects['center_y'][i] - (objects['y'][i] / 2))
#         l2 = Point(objects['center_x'][k] - (objects['x'][k] / 2), objects['center_y'][k] + (objects['y'][k] / 2))
#         r2 = Point(objects['center_x'][k] + (objects['x'][k] / 2), objects['center_y'][k] - (objects['y'][k] / 2))
#         if not l1[0] > l2[0] and r1[0] < r2[0] and 400 - objects['center_z'][k] > objects['center_z'][i]:
#             print('pick object:', object[i])

# sort to topmost objects by their surface center heights in descending order
sorted_objects = sorted(dict_objects.values[-1], key=lambda x: max(objects['center_z'][x]))

for k in sorted_objects:
    for i in objects:
        l1 = Point(objects['center_x'][i] - (objects['x'][i] / 2),
			 objects['center_y'][i] + (objects['y'][i] / 2))
        r1 = Point(objects['center_x'][i] + (objects['x'][i] / 2),
			 objects['center_y'][i] - (objects['y'][i] / 2))
        l2 = Point(objects['center_x'][k] - (objects['x'][k] / 2),
			 objects['center_y'][k] + (objects['y'][k] / 2))
        r2 = Point(objects['center_x'][k] + (objects['x'][k] / 2),
			objects['center_y'][k] - (objects['y'][k] / 2))
        # Check if there is any collision when the box is picked based on its height.
        if not l1[0] > l2[0] and r1[0] < r2[0] and 400 - objects['center_z'][k] > objects['center_z'][i]:
            print('pick object:', object[i])
