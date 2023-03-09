import numpy as np
from utils.dataset_loader import load_whale_dataset

# pylint: disable=pointless-string-statement
"""
EXERCISE 3, Filtering With `loc` and `iloc`
------------------------
In this exercise you will write the same queries as exercise_2,
    this time using `loc` and `iloc` instead of `[]`.

    * After you're done, uncomment the assert statements to check your answers.
"""

whale_df = load_whale_dataset()

# YOUR CODE GOES HERE
# * Find out how many 'humpback' whales older than '30' there are.
number_of_humpback_whales_older_than_30 = ...

# * Find out how many non-'humpback' whales aged '114' there are.
number_of_non_humpback_whales_aged_114 = ...

# * Find out the  age of the oldest female narwhal.
#     HINT: You can use the function `df[<colname>].max` to select
#         the maximum value of the column <colname>.
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
EXERCISE 3, Part 2: Multiple Conditions, Wrong Dimension
------------------------
    * Currently the weight of male humpback whales is in kilograms (kg.),
        while for other whales it's in tonnes (1 tonne == 1000 kg.)
        * Set the weight of humpback whales to tonnes.
"""

# YOUR CODE GOES HERE

"""
EXERCISE 3, Part 3: Putting it all Together
------------------------

You will now use all you've learned to answer some more
    complex questions about whales with the power of Pandas!
    
    * After you're done, uncomment the assert statements to check your answers.
"""

# YOUR CODE GOES HERE
# * What's the age of the youngest humpback whale that has size > 10 meters?
young_humpb_longer_than_10 = ...

# * What's the mean weight of narwhals with age > 30?
#     HINT: You can use the `mean` function.
narwhals_older_than_30_mean_weight = ...

# * What's the age of the heaviest orca?
#     HINT: You can use either `sort_values(by='weight', ascending=False)` to sort orcas
#         OR you can use `idxmax` to find the index of the heaviest.
heaviest_orca_age = ...

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert heaviest_orca_age == 8, f"Wrong heaviest orca age - {heaviest_orca_age}!"
# assert young_humpb_longer_than_10 == 5, \
#     f"Wrong age of youngest humpback longer than 10m - {young_humpb_longer_than_10}."
# assert np.isclose(narwhals_older_than_30_mean_weight, 1.1897714531340777, rtol=1e-5), \
#     f"Wrong mean weight of narwhals older than 30 - {narwhals_older_than_30_mean_weight:.5f}!"
