import pandas as pd
from utils.dataset_loader import load_fishguard_dataset

"""
EXERCISE 1: PART 1
------------------------

The code below loads the dataset of temperatures in the town of 'Fishguard'.
This dataset contains average temperatures for each month in a year.
You will now use pandas to extract some information about the dataset.

    * Examine the size and shape of the dataset, you might notice something odd.
    * Print the dataset and familiarize yourself with it.
    * Extract the temperatures for June and July.
    * Use the method `idxmax` (index-max) on the Series to find the month (index)
        with the highest temperature. What do you notice?
    * Can you fix the problem by removing a label from the dataset?
        Once you've fixed the problem, make sure that idxmax gives the correct answer.

    * Uncomment the print statements.
"""

fishguard_temps = load_fishguard_dataset()

# YOUR CODE GOES HERE
fishguard_temps_shape = ...
print(fishguard_temps_shape)

temps_jun_jul = ...
highest_temp_month = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print("=" * 50)
# print('The average temperature in June is {0} and in July it is {1} degrees'.format(*temps_jun_jul))
# print(f'The month with the highest temperature is {highest_temp_month}')
# print()

"""
[Optional] EXERCISE 1: PART 2
------------------------
    * Find the names of the three months with the highest temperatures.
        To do so, you can first sort the Series and then take the first three
            elements of the index of the (sorted) Series object.
    * What's the average temperature for those three months?

HINT: Use python's `help` function on the `sort_values` method of the Series.

    * Uncomment the print statements (they also makes sure the shape of your Series is correct).
"""

# YOUR CODE GOES HERE

temps_sorted =  ...
highest_temp_months = ...
avg_temp = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# print("=" * 50)
# print('The three months with the highest temperatures are {0}, {1}, {2}'.format(*highest_temp_months))
# print(f'The average temperature in those months is {avg_temp:.1f} degrees')
# print()