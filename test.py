import random
from icecream import ic
matrix= [[random.randint(10, 15) for _ in range(7)] for _ in range(1000)]
indices = [0,1,2,3,4,5,6]


def swap(array, index_a, index_b):
    support = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = support

    return array

def array_comparison(matrix, matrix_length, ordering_index, previndex, index_of_index):
    current_row = 0
    next_row_to_compare = 1
    while (next_row_to_compare <= matrix_length - 1):
        if (index_of_index == 0 and matrix[current_row][ordering_index] > matrix[next_row_to_compare][ordering_index]) or (index_of_index > 0 and matrix[current_row][ordering_index] > matrix[next_row_to_compare][ordering_index] and matrix[current_row][previndex] == matrix[next_row_to_compare][previndex]):
            matrix = swap(matrix, current_row, next_row_to_compare)
        next_row_to_compare += 1
        current_row += 1

    return matrix

def matrix_iteration(index, matrix, matrix_length, previndex, index_of_index):
    next_row = 1

    while (next_row < len(matrix)):

        matrix = array_comparison(matrix, matrix_length, index, previndex, index_of_index)

        matrix_length -= 1
        next_row += 1

    return matrix

def order_matrix(indices, matrix):

    if max(indices) <= len(matrix[0]) -1:
        indices.sort()
        matrix_length = len(matrix)
        
        previndex = None
        index_of_index = 0
        for index in indices:

            matrix = matrix_iteration(index, matrix, matrix_length, previndex, index_of_index)
        
            previndex = indices[index_of_index]
            index_of_index += 1

        return matrix

    else:

        ic('Numero colonne della matrice minore di indice di ordinamento')



matrix = order_matrix(indices, matrix)

ic(matrix)

