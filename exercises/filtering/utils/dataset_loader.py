import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data'


def load_fishguard_dataset():
    """Loads the Fishguard temperatures dataset.
    Returns: A pandas Series containing average temperatures in Fishguard over months.
    """
    df = pd.read_csv(DATA_PATH / 'fishguard_mean_temps.csv', index_col=0)
    
    # return a series of the (only) column in this dataset
    return df.iloc[:, 0]


def load_whale_dataset():
    """Loads the (fake) clean whale dataset.
    Returns: A pandas DataFrame containing the whale dataset,
    """
    return pd.read_csv(DATA_PATH / 'fake_whale_dataset_dirty_filtering.csv', index_col=0)
