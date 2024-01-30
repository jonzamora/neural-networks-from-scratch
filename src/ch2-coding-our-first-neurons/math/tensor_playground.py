# A simple list
simple_list = [1, 5, 6, 2]

# List of lists
list_of_lists = [[1, 5, 6, 2],
                 [3, 2, 1, 3]]

# A List of lists with lists
# i.e. 3D Array
# outermost level contains 3 matrices
# each matrix contains 2 lists
# each list contains 4 elements
# therefore, shape of this array is (3, 2, 4):
# (3 matrices, 2 rows/lists, 4 columns/elements)
list_of_lists_of_lists = [[[1, 5, 6, 2],
                           [3, 2, 1, 3]],

                          [[5, 2, 1, 2],
                           [6, 4, 8, 4]],

                          [[2, 8, 5, 3],
                           [1, 1, 9, 4]]]

# Not homologous -- cannot be an array
another_list_of_lists = [[4, 2, 3], [5, 1]]

# A matrix with shape (3, 2): (3 rows, 2 columns)
list_matrix_array = [[4, 2],
                     [5, 1],
                     [8, 2]]
