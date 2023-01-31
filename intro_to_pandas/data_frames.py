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
    It's useful to `print` what you select. This will let you know if you're
        for instance selecting rows when you mean to select columns, etc.
    
    * Select the size of all whales in the dataset.
        * If you use `whale_df.size`, what goes wrong?
    * Select the weight of whale number 567
    * Select the age and whale_type of the first 100 whales.
    
    * Select the index of the largest whale (in size) in the dataset.
        * You can use `whale_sizes`, which contains the sizes of all whales.
        * Use `idxmax` on this Series to find the index of the largest whale.
        
    * Uncomment the assert statements to check your answers.
"""

whale_df = load_whale_dataset()

# YOUR CODE GOES HERE
# Print df.head(). What kind of object is it?
print(...)

whale_sizes = ...

whale_567_weight = ...

age_whale_type_first_100 = ...

largest_whale_index = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert whale_sizes.shape == (whale_df.shape[0],), "Shape of whale_sizes is wrong!"
# assert age_whale_type_first_100.shape == (100, 2), "Shape of age_whale_type_first_100 is wrong!"
# assert np.isclose(whale_567_weight, 6.641571451865368, rtol=1e-6), "Weight of whale 567 is wrong!"
# assert largest_whale_index == 2045, "Wrong largest whale selected!"

"""
EXERCISE 2: Mathematical Operations
------------------------

You will now use pandas to compute some statistics about whales.

    * The first line of code prints `df.describe`. What kind of object is `df.describe()`?
        * Assign it to a new variable, for instance `desc = df.describe()`
        * Extract from `desc` the mean size
    * Extract the mean (average) age of the first 100 whales
        HINT: You can use df.head to select the first 100 whales
    * Extract the total weight of all whales
    * Extract the age of the oldest whale
        HINT: Use max on the 'age' column 

    * Uncomment the assert statements to check your answers.
"""

# YOUR CODE GOES HERE
print()
print('=' * 50)
print(whale_df.describe())

desc = ...

mean_size_whales = ...

mean_age_first_100_whales = ...

total_weight_all_whales = ...

oldest_whale_age = ...

# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert np.isclose(mean_size_whales, 6.621894, rtol=1e-4), "Mean size of whale is wrong!"
# assert np.isclose(mean_age_first_100_whales, 37.78, rtol=1e-2), "Mean age of first 100 whales is wrong!"
# assert np.isclose(total_weight_all_whales, 117907.7810983918, rtol=1e-5), "Total weight of all whales is wrong!"
# assert np.isclose(oldest_whale_age, 114, rtol=1e-5), "Oldest whale weight is wrong!"
