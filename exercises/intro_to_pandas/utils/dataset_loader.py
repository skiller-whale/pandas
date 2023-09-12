import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / 'data'
MOVIES_DATASET_PATH = DATA_PATH / 'movies' / 'movies_small.csv'

def load_fishguard_dataset():
    """Loads the Fishguard temperatures dataset.
    Returns: A pandas Series containing average temperatures in Fishguard over months.
    """
    df = pd.read_csv(DATA_PATH / 'fishguard_mean_temps.csv', index_col=0)
    
    # return a series of the (only) column in this dataset
    return df.iloc[:, 0]

