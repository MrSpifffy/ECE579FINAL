import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming


def prompt_coord():
    val = input('Enter coordinate in formate (x, y): ')
    val = val.split(',')
    val = [int(ch.strip().strip('()')) for ch in val]
    return tuple(val)



def get_distance(pointA, pointB):
    return np.sqrt(np.square(np.abs(pointA[0]-pointB[0])) + np.square(np.abs(pointA[1]-pointB[1])))

def get_distance_matrix(cities):
    N = len(cities)
    matrix = np.empty((N, N))
    for i in range(N):
        for j in range(N):
            matrix[i][j] = get_distance(cities[i], cities[j])
    return matrix
            


def solve_tsp(cities):
    distance_matrix = get_distance_matrix(cities)
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
    return permutation, distance

