import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / 'data'


def load_movies_dataset():
    """Loads the movies dataset.
    Returns: A pandas DataFrame containing the movies dataset,
    """
    df = pd.read_csv(DATA_PATH / 'movies' / 'movies_small.csv', index_col=0)
    
    # set the runtime of all English movies to hours
    df.loc[df['original_language'] == 'en', 'runtime'] /= 60

    return df
