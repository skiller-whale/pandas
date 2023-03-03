import pandas as pd
import numpy as np
from utils.dataset_loader import load_fishguard_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 1: PART 1
------------------------

The code below loads the dataset of temperatures in the town of 'Fishguard'.
This dataset contains average temperatures for each month in a year.
You will now use pandas to extract some information about the dataset.
"""

fishguard_temps = load_fishguard_dataset()

# YOUR CODE GOES HERE
# * Print the dataset and familiarize yourself with it.
print(...)

# * Examine the size and shape of the dataset, you might notice something odd.
fishguard_temps_shape = ...
print(fishguard_temps_shape)

# * Extract the temperatures for June and July.
temps_jun_jul = ...

# * Use the function `idxmax` (index-max) on the Series to find the month (index)
#   with the highest temperature. What do you notice?
highest_temp_month = ...
print(highest_temp_month)

# * Can you fix the problem by removing a label from the dataset?
#     Once you've fixed the problem, make sure that idxmax gives the correct answer.
fishguard_temps = ...
highest_temp_month = ...

# * Uncomment the print statements.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print("=" * 50)
# print('The average temperature in June is {0} and in July it is {1} degrees'.format(*temps_jun_jul))
# print(f'The month with the highest temperature is {highest_temp_month}')
# print()

"""
[Optional] EXERCISE 1: PART 2
------------------------

In this exercise you'll compute some statistics about the data.
"""

# YOUR CODE GOES HERE

# * Find the names of the three months with the highest temperature.
#     To do so, you can first sort the Series and then take the first three
#         elements of the index of the (sorted) Series object.
# HINT: Use python's `help` function on the `sort_values` method of the Series.

fishguard_temps_sorted = ...
highest_temp_months = ...

# * Compute the average temperature for those three months.
avg_temp = ...

# * Uncomment the prints statements.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print("=" * 50)
# print('The three months with the highest temperatures are {0}, {1}, {2}'.format(*highest_temp_months))
# print(f'The average temperature in those months is {avg_temp:.1f} degrees')
# print()
