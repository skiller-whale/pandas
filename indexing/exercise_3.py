import pandas as pd
import numpy as np
from utils.dataset_loader import load_whale_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 3: Chained Indexing
------------------------

This exercise has the same queries as the previous exercises.
    Write the same queries using chained indexing,
    combining `[]`, `loc`, or `iloc.

    * Select the age and whale_type of the first 100 whales.
    * Select the weight of whale number 567
    * Select all columns, EXCEPT the whale_type of the LAST 200 whales

    * Uncomment the assert statements to check your answers.

Once you've finished the exercise,
    think about the order of indexing (no need to rewrite anything).
    * Discuss this with your coach.
"""


whale_df = load_whale_dataset()
# YOUR CODE GOES HERE

# * Select the age and whale_type of the first 100 whales.
age_whale_type_first_100 = whale_df[['age', 'weight']].loc[:100]

# * Select the weight of whale number 567
whale_567_weight = whale_df['weight'].iloc[567]

# * Select all columns, EXCEPT the gender of the LAST 200 whales
last_200_whales_except_gender = whale_df.iloc[-200:].loc[:, 'size': 'gender']

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
assert last_200_whales_except_gender.shape == (200, 4), "Shape of last_200_whales_except_gender is wrong!"
