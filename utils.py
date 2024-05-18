class Point:
    """
    Creates global coordinate points objects given (x,y)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def overlap(cx_1, cy_1, x_1, y_1, cx_2, cy_2, x_2, y_2):
    """
    Checks whether two rectangles overlap
    Parameters
    ----------
    cx_1: first object center (x)
    cy_1: first object center (y)
    x_1: first object dimension (x)
    y_1: first object dimension (y)
    cx_2: first object center (x)
    cy_2: second object center (y)
    x_2: second object dimension (x)
    y_2: second object dimension (y)

    Returns bool
    -------

    """
    l1 = Point(cx_1 - (x_1 / 2), cy_1 + (y_1 / 2))
    r1 = Point(cx_1 + (x_1 / 2), cy_1 - (y_1 / 2))
    l2 = Point(cx_2 - (x_2 / 2), cy_2 + (y_2 / 2))
    r2 = Point(cx_2 + (x_2 / 2), cy_2 - (y_2 / 2))
    # To check if either rectangle is actually a line
    if l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y:
        return False

    # If one rectangle is on left side of other
    if l1.x >= r2.x or l2.x >= r1.x:
        return False

    # If one rectangle is above other
    if r1.y >= l2.y or r2.y >= l1.y:
        return False

    return True

