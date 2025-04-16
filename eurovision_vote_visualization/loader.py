import pandas as pd
import os


def load_data(directory: str, file_path: str):
    """
    Load the data from a CSV file and return a DataFrame.
    """
    path = os.path.join(directory, file_path)
    if not os.path.exists(path):
        # Check if the file exists in the data directory
        raise FileNotFoundError(f"File {file_path} not found in data directory.")

    df = pd.read_csv(path, delimiter=",")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError(f"The file {file_path} is empty.")

    # Drop specific columns if they exist
    columns_to_drop = ["composers", "lyricists", "performer", "lyrics", "youtube_url"]

    for col in columns_to_drop:
        if col in df.columns:
            df.drop(columns=col, inplace=True)

    return df
