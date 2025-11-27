import numpy as np
import quiz 
# test="hello world"
# print(test)

# one_dimensional_array=np.array([10,2])
# print(one_dimensional_array)

# iin_spaced_arr=np.arange(3,75,5)
# print(iin_spaced_arr)

# gap_array=np.linspace(0,100,5)
# print(gap_array)

# c_int = np.arange(1, 20, 3, dtype=int)
# print(c_int)
# b_float = np.arange(3, dtype=float)
# print(b_float)
# char_arr = np.array(['Welcome to Math for ML!'])
# print(char_arr)
# print(char_arr.dtype) # Prints the data type of the array

# zeros_arr = np.zeros(3)
# print(zeros_arr)


one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
# multi_dim_arr = np.reshape(
#                 one_dim_arr, # the array to be reshaped
#                (2,3) # dimensions of the new array
#               )
# # Print the new 2-D array with two rows and three columns
# print(multi_dim_arr)

# Slice the array a to get the array [2,3,4]
sliced_arr = one_dim_arr[:3]
print(sliced_arr)

import quiz
import ipywidgets as widgets
q1 = quiz.mcq(quiz.question1, quiz.solution1)