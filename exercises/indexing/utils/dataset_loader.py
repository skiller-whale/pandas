import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / 'data'


def load_fishguard_dataset():
    """Loads the Fishguard temperatures dataset.
    Returns: A pandas Series containing average temperatures in Fishguard over months.
    """
    df = pd.read_csv(DATA_PATH / 'fishguard_mean_temps.csv', index_col=0)
    
    # return a series of the (only) column in this dataset
    return df.iloc[:, 0]


def load_movies_dataset():
    """Loads the movies dataset.
    Returns: A pandas DataFrame containing the movies dataset,
    """
    df = pd.read_csv(DATA_PATH / 'movies' / 'movies_small.csv', index_col=0)
    
    # add one to the indexing so it starts from 2
    df.index += 2
    
    return df
