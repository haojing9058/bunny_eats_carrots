"""
Test cases:

>>> eat([[]])
0

>>> eat([[2]])
2

>>> eat([[3,4]])
7

>>> eat([[2, 6, 9]])
15

>>> eat([[2], [3], [5]])
8

>>> eat([[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]])
27

"""


def eat(matrix):
    """return the number of corrots the rabbit eats"""
    
    m = len(matrix) #number of rows
    n = len(matrix[0]) #number of cols

    # empty matrix
    if m == 1 and n == 0:
        return 0
    
    # helper function to identify the center of the matrix
    def find_center(length):
        if length ==1:
            return [0]
        # if length is odd, return the middle index
        elif length % 2 == 1:
            return [length/2]
        # if length is even, return the middle two indices
        elif length % 2 == 0:
            return [length/2 - 1, length/2]
    
    carrots = 0
    # Find the center of the matrix by finding the max with a given area
    # The area can be made up of 1(m and n are odd), 2(m or n is odd), 4 elements (m and n are even).
    for y in find_center(m):
        for x in find_center(n):
            if matrix[y][x] > carrots:
                carrots = matrix[y][x]
                y0, x0 = y, x
    
    # if a value is used, reset the value to 0
    matrix[y0][x0] = 0
    

    # exit if all valid values from left, right, up, or down are zeros.
    
    # helper lists to let the rabbit move left, right, up, or down.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while True:
        temp = 0
        for i in range(4):
            y_new, x_new = (y0 + dy[i]), (x0 + dx[i])
            # check if left, right, up, or down, and it's valid if it doesn't exceed index
            # get the max number among valid left, right, up, or down neighbors
            if x_new >= 0 and x_new < n and y_new >= 0 and y_new < m:
                if matrix[y_new][x_new] > temp:
                    temp = matrix[y_new][x_new]
                    y_max, x_max = y_new, x_new
        # exit if all valid values from left, right, up, or down are zeros.
        if temp == 0:
            return carrots
        else:
            # increase total carrots by the number of carrots eaten
            carrots += temp
            # reset the spot that rabbit has eaten the carrots to 0
            matrix[y_max][x_max] = 0
            # recenter the start point
            y0, x0 = y_max, x_max


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("ALL TESTS PASSED")