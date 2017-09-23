def gini(list_of_values):
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2.
    return (fair_area - area) / fair_area


# def gini(values):
#     '''
#     Source: http://dilumb.blogspot.com/2012/07/python-code-to-calculate-gini.html
#     Calculate Gini index, Gini coefficient, Robin Hood index, and points of
#     Lorenz curve based on the instructions given in
#     www.peterrosenmai.com/lorenz-curve-graphing-tool-and-gini-coefficient-calculator
#     Lorenz curve values as given as lists of x & y points [[x1, x2], [y1, y2]]
#     @param values: List of values
#     @return: [Gini index, Gini coefficient, Robin Hood index, [Lorenz curve]]
#     '''
#     n = len(values)
#     assert (n > 0), 'Empty list of values'
#     sortedValues = sorted(values)  # Sort smallest to largest
#
#     # Find cumulative totals
#     cumm = [0]
#     for i in range(n):
#         cumm.append(sum(sortedValues[0:(i + 1)]))
#
#     # Calculate Lorenz points
#     LorenzPoints = [[], []]
#     sumYs = 0  # Some of all y values
#     robinHoodIdx = -1  # Robin Hood index max(x_i, y_i)
#     for i in range(1, n + 2):
#         x = 100.0 * (i - 1) / n
#         y = 100.0 * (cumm[i - 1] / float(cumm[n]))
#         LorenzPoints[0].append(x)
#         LorenzPoints[1].append(y)
#         sumYs += y
#         maxX_Y = x - y
#         if maxX_Y > robinHoodIdx: robinHoodIdx = maxX_Y
#
#     giniIdx = 100 + (100 - 2 * sumYs) / n  # Gini index
#
#     return giniIdx / 100