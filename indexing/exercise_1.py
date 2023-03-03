import pandas as pd
import numpy as np
from utils.dataset_loader import load_whale_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 1: Positional Indexing With `iloc`
------------------------

The code below loads a (fake) dataset of whales.
You will now use pandas to extract some information from the dataset.

    * Select the age and whale_type of the first 100 whales.
    * Select the weight of whale number 567
    * Select all columns, EXCEPT whale_type, for the LAST 200 whales
    * Select the index of the largest whale (in size) in the dataset.
        * Select the 'size' column, which is a Series
        * Use `idxmax` on this Series to find the index of the largest whale.
        * If you use `whale_df.size`, what goes wrong?
            
    * Uncomment the assert statements to check your answers.
"""

whale_df = load_whale_dataset()

# YOUR CODE GOES HERE

# * Select the age and whale_type of the first 100 whales.
age_whale_type_first_100 = whale_df.iloc[:100, [
    whale_df.columns.get_loc('age'),
    whale_df.columns.get_loc('weight')
]]

# * Select the weight of whale number 567
whale_567_weight = whale_df.iloc[
    567, whale_df.columns.get_loc('weight')
]

# * Select all columns, EXCEPT the gender of the LAST 200 whales
last_200_whales_except_gender = whale_df.iloc[
    -200:, [
        whale_df.columns.get_loc('weight'),
        whale_df.columns.get_loc('age'),
        whale_df.columns.get_loc('whale_type'),
        whale_df.columns.get_loc('size'),
    ]
]

# * Select the size of all whales in the dataset.
whale_sizes = whale_df.iloc[:, whale_df.columns.get_loc('size')]

largest_whale_index = whale_sizes.idxmax()

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
assert last_200_whales_except_gender.shape == (200, 4), "Shape of last_200_whales_except_gender is wrong!"
assert largest_whale_index == 2045, "Wrong largest whale selected!"
