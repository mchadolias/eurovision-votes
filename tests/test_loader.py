# Check working directory
# Test suite for the loader module
import os
import sys
import pytest

# Test which python interpreter is being used
print(f"Python interpreter: {sys.executable}")

# Set the path to the main directory to import the module, add the main directory to sys.path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path)
print(path)

# Import the function to be tested
from eurovision_vote_visualization import load_data


# Test if function is load_data is defined
def test_load_data_function_exists():
    """
    Test if the function load_data is defined.
    """
    assert "load_data" in globals(), "Function load_data is not defined."
    assert callable(load_data), "load_data is not callable."
    assert load_data.__name__ == "load_data", "Function name is not load_data."


def test_loader_columns():
    """
    Test if the columns of the loaded DataFrame are as expected.
    """

    # Load the data
    df = load_data(os.path.join(path, "data"), "contestants.csv")

    # Define the expected columns
    expected_columns = [
        "year",
        "to_country",
        "song",
        "place_final",
        "points_final",
    ]

    # Check if the columns match
    assert all(
        col in df.keys() for col in expected_columns
    ), f"Expected columns: {expected_columns}, but got: {df.keys()}"


def test_loader_shape():
    """
    Test if the shape of the loaded DataFrame is as expected.
    """

    # Load the data
    df = load_data(os.path.join(path, "data"), "contestants.csv")

    # Define the expected shape
    expected_shape = (1102, 16)

    # Check if the shape matches
    assert df.shape == expected_shape, f"Expected shape: {expected_shape}, but got: {df.shape}"


def test_loader_empty_file():
    """
    Test if loading an empty file raises a ValueError.
    """

    # Create a temporary empty file
    path = os.path.dirname(__file__)
    empty_file_path = os.path.join(path, "empty_file.csv")

    with open(empty_file_path, "w") as f:
        f.write("")

    # Check if loading the empty file raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        load_data(path, "empty_file.csv")

    # Clean up the temporary file
    os.remove(empty_file_path)


def test_loader_file_not_found():
    """
    Test if loading a non-existent file raises a FileNotFoundError.
    """

    # Define a non-existent file path
    non_existent_file_path = "non_existent_file.csv"

    # Check if loading the non-existent file raises a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        load_data(".", non_existent_file_path)
