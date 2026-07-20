import math 
def nearest_neighbor(neighbors,point):

    min_distance = float('inf')
    nearest = None

    for p in neighbors:

        distance = math.sqrt((p[0]-point[0])**2+(p[1]-point[1])**2)

        if distance<min_distance:
            min_distance=distance
            nearest=p

    return nearest
neighbors=[(2,3),(5,4),(9,6),(4,7)]
point=(5,5)

print("nearest neighbor: ",nearest_neighbor(neighbors,point))

