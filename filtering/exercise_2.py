import numpy as np
from utils.dataset_loader import load_whale_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 2, Part 1: Multiple Conditions
------------------------
    * After you're done, uncomment the assert statements to check your answers.
"""

whale_df = load_whale_dataset()

# YOUR CODE GOES HERE

# * Find out how many 'humpback' whales older than '30' there are.
#     * Do NOT use a temporary 'humpback' whales table this time.
number_of_humpback_whales_older_than_30 = ...

# * Find out how many non-'humpback' whales aged '114' there are.
number_of_non_humpback_whales_aged_114 = ...

# * Find out the  age of the oldest female narwhal.
#   HINT: You can use the function `df[<colname>].max` to select
#       the maximum value of the column <colname>.
age_of_oldest_female_narwhal = ...

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert number_of_humpback_whales_older_than_30 == 1414, \
#     f"Wrong number of humpback whales older than 30 - {number_of_humpback_whales_older_than_30}!"
# assert number_of_non_humpback_whales_aged_114 == 13, \
#     f"Wrong number of non-humpback whales aged 114 - {number_of_non_humpback_whales_aged_114}!"
# assert age_of_oldest_female_narwhal == 114, \
#     f"Wrong age of oldest narwhal - {age_of_oldest_female_narwhal}!"

"""
EXERCISE 2, Part 2: Multiple Conditions, Wrong Dimension
------------------------
    * Currently the weight of male humpback whales is in kilograms (kg.),
        while for other whales it's in tonnes (1 tonne == 1000 kg.)
        * Set the weight of humpback whales to tonnes.

    What do you notice?
"""

# YOUR CODE GOES HERE
