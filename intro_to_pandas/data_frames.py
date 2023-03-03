import pandas as pd
import numpy as np
from utils.dataset_loader import FAKE_WHALE_DATASET_PATH

# pylint: disable=pointless-string-statement
"""
EXERCISE 1: Indexing Into DataFrames
------------------------

You will now use pandas to extract some information from a dataset of fake whales.

It's useful to `print` what you select. This will let you know if, for instance,
    you're selecting rows when you mean to select columns, etc.
"""

# YOUR CODE GOES HERE
# * Load the fake whale dataset (its path is imported above in FAKE_WHALE_DATASET_PATH)
#   * You will need to specify that column `0` contains the index
whale_df = ...

# * The pandas functions df.head(N) selects the first N rows of the DataFrame.
#     Use it (with print) to examine the dataset and familiarize yourself with it.
print(...)

# * Select the size of all whales in the dataset.
#   * If you use `whale_df.size`, what goes wrong?
whale_sizes = ...

# * Select the weight of the whale at index 567
whale_567_weight = ...

# * Select the age and whale_type of the first 100 whales.
age_whale_type_first_100 = ...

# * Select the index of the largest whale (in size) in the dataset.
#     * You can use `whale_sizes`, which contains the sizes of all whales.
#     * Use `idxmax` (index-max) on this Series to find the index of the largest whale.
largest_whale_index = ...

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert whale_sizes.shape == (whale_df.shape[0],), "Shape of whale_sizes is wrong!"
# assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
# assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
# assert largest_whale_index == 2045, "Wrong largest whale selected!"

"""
EXERCISE 2: Mathematical Operations
------------------------

You will now use pandas to compute some statistics about whales.
"""

# * Uncomment the print statements
# print()
# print('=' * 50)
# print(whale_df.describe())

# YOUR CODE GOES HERE
# * The above code prints `whale_df.describe()`.
#   What kind of object is returned by `whale_df.describe()`?
# * Assign it to `desc`.
desc = ...

# * Extract from `desc` the mean (average) size of whales
mean_size_whales = ...

# * Extract the mean age of the first 100 whales
mean_age_first_100_whales = ...

# * Extract the total weight of all whales
total_weight_all_whales = ...

# * Extract the age of the oldest whale
#     HINT: Use max on the 'age' column 
oldest_whale_age = ...

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert np.isclose(mean_size_whales, 6.621894, rtol=1e-4), "Mean size of whale is wrong!"
# assert np.isclose(mean_age_first_100_whales, 37.78, rtol=1e-2), "Mean age of first 100 whales is wrong!"
# assert np.isclose(total_weight_all_whales, 117907.7810983918, rtol=1e-5), "Total weight of all whales is wrong!"
# assert np.isclose(oldest_whale_age, 114, rtol=1e-5), "Oldest whale weight is wrong!"
