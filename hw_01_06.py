# Homework 1.6
# Author: Jacob Wolf

def line_y_value(x, m, b):
    """
    This function should return the y value of the line defined by slope m and
    y-intercept b at x.

        >>> line_y_value(2, .5, 1)
        2

        >> line_y_value(0, .3, 4)
        4

    input: int/float x, int/float m, int/float b
    output: int/float
    """

    pass

def residual(point, m, b):
    """
    This function returns the residual of the given point from the line defined by slope m and
    y-intercept b. The residual is the distance between the y value of the line at x and the
    y value of the point.

        >>> distance_from_line((1,2), 0.5, 2)
        0.5

        >> distance_from_line((3,3), 0.0, 3)
        0.0

    input: (int/float, int/float) pair point, int/float m, int/float b
    output: int/float

    NOTE 1: point is an (x,y) pair. You can access the x and y values like this:
        x = point[0]
        y = point[1]

    NOTE 2: Residuals like distances should always be a positive value (what does
    it mean to have a distance of -1? 🧐). To do this, you may need to take the
    absolute value at some point in your function. You can do that using the abs()
    function:
        >>> some_value = -3
        >>> abs(some_value)
        3
    """

    pass

def closest_to_line(list_of_points, m, b):
    """
    This function should find the point from the list of points whose y value has the
    smallest distance from the line. If there are multiple points with the same distance
    from the line, any of the points can be returned.

        >>> closest_to_line([(0,0), (2,3.5)], 1, 1)
        (2,3.5)
        >>> closest_to_line([(0,0), (1,1), (2,2)], 1, 0)
        (0,0)

    input: list of (int/float,int/float) pairs list_of_points, int/float m, int/float b
    output: (int/float, int/float)
    """

    pass
