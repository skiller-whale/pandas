import pandas as pd
import numpy as np
from utils.dataset_loader import load_whale_dataset

"""
EXERCISE 1: Indexing Into DataFrames
------------------------

The code below loads a (fake) dataset of whales.
You will now use pandas to extract some information from the dataset.

    * The pandas functions df.head(N) selects the first N rows of the DataFrame.
        Use it (with print) to examine the dataset and familiarize yourself with it.

    For the next tasks, you're asked to index into a DataFrame to select some data.
    They can be done in a few different ways, using `[]`, `loc`, or `iloc`.
    If you're stuck, have a look at the recipes/examples on the slide and see if
        any are relevant.
    It's also useful to `print` what you select. This will let you know if you're
        for instance selecting rows when you mean to select columns with e.g. `iloc`.
    
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

print()
print('=' * 50)

# YOUR CODE GOES HERE
# Use df.head(N) to print the first few elements of the data frame.
print(...)

age_whale_type_first_100 = ...

whale_567_weight = ...

last_200_whales_except_gender = ...

largest_whale_index = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
# assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
# assert last_200_whales_except_gender.shape == (200, 4), "Shape of age_whale_type_first_100 is wrong!"
# assert largest_whale_index == 2045, "Wrong largest whale selected!"


"""
EXERCISE 2: Chained Indexing
------------------------

Rewrite your indexing code from EXERCISE 1 to use chained indexing.

    * Select the age and whale_type of the first 100 whales.
    * Select the weight of whale number 567
    * Select all columns, EXCEPT the whale_type of the LAST 200 whales

    * Uncomment the assert statements to check your answers.

Once you've finished the exercise:
    * Think about the order of indexing (no need to rewrite anything).
"""

# YOUR CODE GOES HERE
age_whale_type_first_100 = ...

whale_567_weight = ...

last_200_whales_except_gender = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert largest_whale_index == 2045, "Wrong largest whale selected!"
# assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
# assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
# assert last_200_whales_except_gender.shape == (200, 4), "Shape of age_whale_type_first_100 is wrong!"

"""
EXERCISE 3: Mathematical Operations
------------------------

You will now use pandas to compute some statistics about whales.

    * The first line of code prints `df.describe`. What kind of object is `df.describe()`?
        * Assign it to a new variable, for instance `desc = df.describe()`
        * Extract from `desc` the mean size and weight of whales
    * Extract the mean (average) age of the first 100 whales
    * Extract the total weight of all whales
    * Extract the weight of the oldest whale
        HINT: Use idxmax on the 'age' column to get the index of the oldest whale
    * Extract a DataFrame that contains the max age and max weight of whales.
        HINT: Use [], loc, or iloc to select the relevant columns,
            then use `max` on the resulting DataFrame.

    * Uncomment the assert statements to check your answers.
"""

print()
print('=' * 50)

# YOUR CODE GOES HERE
# Print df.describe(). What kind of object is it?
print(...)

desc = ...
mean_size_weight_whales = ...

mean_age_first_100_whales = ...

total_weight_all_whales = ...

oldest_whale_idx = ...
oldest_whale_weight = ...

max_age_weight_data_frame = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert np.isclose(mean_size_weight_whales.loc['size'], 6.621894, rtol=1e-4), "Mean size of whale is wrong!"
# assert np.isclose(mean_size_weight_whales.loc['weight'], 14.983833, rtol=1e-4), "Mean weight of whale is wrong!"
# assert np.isclose(mean_age_first_100_whales, 37.78, rtol=1e-2), "Mean age of first 100 whales is wrong!"
# assert np.isclose(total_weight_all_whales, 117907.7810983918, rtol=1e-5), "Total weight of all whales is wrong!"
# assert np.isclose(oldest_whale_weight, 0.9939764029077836, rtol=1e-5), "Oldest whale weight is wrong!"
# assert np.isclose(max_age_weight_data_frame['age'], 114.000000, rtol=1e-5), "Wrong max age!"
# assert np.isclose(max_age_weight_data_frame['weight'], 70.525739, rtol=1e-5), "Wrong max age!"

"""
EXERCISE 3, Part 1: Filtering
------------------------

You will now use Pandas to filter the whales data.

    * Find out how many whales there are of type 'humpback'.
    * Find out how many 'male' whales aged '114' there are.
    * Extract a DataFrame that contains all whales, where:
        * whale_type is 'narwhal'
        * age is '> 30'
    * Use `describe` on the new narwhal DataFrame
        * Set the value of describe to a new variable
        * What's the mean weight of narwhals aged more than 30?
            Use the DataFrame returned by describe to extract it.
    
    * Uncomment the assert statements to check your answers.
"""

# YOUR CODE GOES HERE
number_of_humpback_whales = ...

number_of_male_whales_aged_114 = ...

narwhals_older_than_30 = ...
narwhals_older_than_30_desc = ...
narwhals_older_than_30_mean_weight = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert number_of_humpback_whales == 2318, "Wrong number of humpback whales!"
# assert number_of_male_whales_aged_114 == 5, "Wrong number of male whales aged 114!"
# assert np.isclose(narwhals_older_than_30_mean_weight, 1.1897714531340777, rtol=1e-5), "Wrong mean weight of narwhals older than 30!"

"""
EXERCISE 3, Part 2: Putting it all Together
------------------------

You will now use all you learned to answer some more
    complex questions about whales with the power of Pandas!

    * What's the age of the oldest orca?
    * What's the age of the
        * Youngest humpback whale,
        * that has size > 10 meters?
    
    In the previous exercise you were asked to use .describe to find
        the mean weight of narwhals with age > 30
    * Do this without using describe?

    * Uncomment the assert statements to check your answers.
"""

# YOUR CODE GOES HERE
oldest_orca_age = ...

young_humpb_longer_than_10 = ...

narwhals_older_than_30_mean_weight = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert oldest_orca_age == 49, "Wrong oldest orca age!"
# assert young_humpb_longer_than_10 == 5, "Wrong age of youngest humpback longer than 10m."
# assert np.isclose(narwhals_older_than_30_mean_weight, 1.1897714531340777, rtol=1e-5), "Wrong mean weight of narwhals older than 30!"
