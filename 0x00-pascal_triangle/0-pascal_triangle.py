#!/usr/bin/python3
""" module to compute paascals traingle """


def pascal_triangle(n):
    """ function to return the traingle """
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        if i == 0:
            tri.append([1])
        elif i == 1:
            tri.append([1, 1])
        elif i == 2:
            tri.append([1, 2, 1])
        elif i > 2:
            tri.append([])
            for k in range(len(tri[i - 1])):
                if tri[i - 1][k] == 1:
                    tri[i].append(1)
                if len(tri[i - 1]) > k + 1:
                    if type(tri[i - 1][k + 1]) is int:
                        val = tri[i - 1][k] + tri[i - 1][k + 1]
                        tri[i].append(val)
                    else:
                        continue
    return tri
