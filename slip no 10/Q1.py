def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
def sum_of_manhattan_distances(points): 
    total_distance = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            total_distance += manhattan_distance(points[i], points[j])
    return total_distance
points = [(1, 2), (4, 6), (7, 9), (3, 1)]
total_manhattan_distance = sum_of_manhattan_distances(points)
print("Sum of Manhattan distances between all pairs of points:", total_manhattan_distance)