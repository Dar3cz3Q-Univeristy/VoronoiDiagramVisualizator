import numpy as np
import matplotlib.pyplot as plt
import csv

# Preparing const variables etc.

plt.axes()

plt.title("Voronoi Diagram with Delunay Triangulation")

plt.xlim(0, 1)
plt.ylim(0, 1)

triangleColor = "black"
givenPointColor = "blue"
voronoiEdgeColor = "red"
voronoiPointColor = "orange"
bestPointColor = "green"

points = []
optimalPoint = []
circumcenters = []
triangles = []
edges = []

separators = [
    "Points",
    "OptimalPoint",
    "Circumcenters",
    "Triangles",
    "Edges",
]

# Separation of data from the file into equivalent variables

with open("visualize.txt") as file:
    status = ""
    for line in file:
        line = line.strip()
        temp = line.split()

        if line == "+":
            status = ""
            continue

        if status == "":
            for separator in separators:
                if temp[0] == separator:
                    status = temp[0]
            continue

        if status == "Points":
            points.append(line)
        elif status == "OptimalPoint":
            optimalPoint.append(line)
        elif status == "Circumcenters":
            circumcenters.append(line)
        elif status == "Triangles":
            triangles.append(line)
        elif status == "Edges":
            edges.append(line)
        else:
            print("Error")

# Drawing figures on plot
# Triangles (only vertices)
for line in triangles:
    temp = line.split()
    p1 = temp[0].split(",")
    p1 = [float(i) for i in p1]

    p2 = temp[1].split(",")
    p2 = [float(i) for i in p2]

    p3 = temp[2].split(",")
    p3 = [float(i) for i in p3]

    # p1 -> p2
    x1 = [p1[0], p2[0]]
    y1 = [p1[1], p2[1]]

    # p2 -> p3
    x2 = [p2[0], p3[0]]
    y2 = [p2[1], p3[1]]

    # p1 -> p3
    x3 = [p1[0], p3[0]]
    y3 = [p1[1], p3[1]]

    plt.plot(x1, y1, color=triangleColor)
    plt.plot(x2, y2, color=triangleColor)
    plt.plot(x3, y3, color=triangleColor)

# Edges
for line in edges:
    temp = line.split()

    p1 = temp[0].split(",")
    p1 = [float(i) for i in p1]

    p2 = temp[1].split(",")
    p2 = [float(i) for i in p2]

    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]

    plt.plot(x, y, color=voronoiEdgeColor)

# Given set of points
for line in points:
    temp = line.split()
    x = float(temp[0])
    y = float(temp[1])
    plt.plot(x, y, color=givenPointColor, marker=".")

# Vertices of Voronoi Diagram
for line in circumcenters:
    temp = line.split()
    x = float(temp[0])
    y = float(temp[1])
    plt.plot(x, y, color=voronoiPointColor, marker=".")

# Found optimal point
for line in optimalPoint:
    temp = line.split(" ")
    x = float(temp[0])
    y = float(temp[1])
    plt.plot(x, y, color=bestPointColor, marker="x", markersize=10, mew=2)

plt.show()
