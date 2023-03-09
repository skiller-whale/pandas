import numpy as np
from utils.dataset_loader import load_whale_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 1: Filtering
------------------------

You will now use Pandas to filter the whales dataset.

HINT: Before you begin, you can use `df.describe()` and `df.head()`
    to familiarize yourself with this dataset.    

HINT 2: For some queries you might need to chain two filtering operations
    and create a temporary data frame.
"""

whale_df = load_whale_dataset()

# YOUR CODE GOES HERE

# * Select all the whales of type 'orca' from the dataset.
all_orcas = ...

# * Select the age of the first `male` whale in the dataset.
age_first_male = ...

# * Find out how many whales there are of type 'humpback'
number_of_humpback_whales = ...

# * Find out how many 'humpback' whales older than '30' there are.
#   This motivates the next slide (chaining operations)
number_of_humpback_whales_older_than_30 = ...

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert all_orcas.shape == (3900, 5), f"Wrong shape of all_orcas - {all_orcas.shape}!"
# assert age_first_male == 21, f"Wrong age of first male whale - {age_first_male}!"
# assert humpback_whales_df.shape == (2318, 5), \
#     f"Wrong shape of humpback whale sub-dataset - {humpback_whales_df.shape}!"
# assert number_of_humpback_whales == 2318, \
#     f"Wrong number of humpback whales - {number_of_humpback_whales}!"
# assert number_of_humpback_whales_older_than_30 == 1414, \
#     f"Wrong number of humpback whales older than 30 - {number_of_humpback_whales_older_than_30}!"
