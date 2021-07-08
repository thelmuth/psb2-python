"""
PSB2 - The Second Program Synthesis Benchmark Suite
"""

import os, json, random
import requests

PROBLEMS = ["basement",
            "bouncing-balls",
            "bowling",
            "camel-case",
            "coin-sums",
            "cut-vector",
            "dice-game",
            "find-pair",
            "fizz-buzz",
            "fuel-cost",
            "gcd",
            "indices-of-substring",
            "leaders",
            "luhn",
            "mastermind",
            "middle-character",
            "paired-digits",
            "shopping-list",
            "snow-day",
            "solve-boolean",
            "spin-words",
            "square-digits",
            "substitution-cipher",
            "twitter",
            "vector-distance"]

def load_json_lines(filename):
    """Load edn from a filename. Expects file to have multiple lines of JSON."""

    data = []
    with open(filename) as f:
        for line in f:
            example = json.loads(line)
            data.append(example)

    return data

def fetch_and_possibly_cache_data(datasets_directory, problem_name, edge_or_random):
    """Helper function for fetch_examples that does the following for edge or
    random dataset:
    1. Checks if JSON file for dataset is already downloaded.
    2. If not, downloads the dataset file to the specified location.
    3. Loads and returns list of the data from the dataset file.
    """

    # Make directory path and file path
    directory_path = os.path.join(datasets_directory, "datasets", problem_name)
    file_path = os.path.join(directory_path, "{}-{}.json".format(problem_name, edge_or_random))

    # Make directories if necessary
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)

    # 1. Check if JSON file already exists
    if not os.path.isfile(file_path):
        # Make URL
        problem_url = "{}/{}-{}.json".format(problem_name, problem_name, edge_or_random)
        s3_url = "https://psb2-datasets.s3.amazonaws.com/PSB2/datasets/{}".format(problem_url)

        # 2. Download dataset file
        fetched_data = requests.get(s3_url)
        with open(file_path, 'wb') as data_file:
            data_file.write(fetched_data.content)

    # 3. Load and return dataset
    dataset = load_json_lines(file_path)
    return dataset


def fetch_examples(datasets_directory, problem_name, n_train, n_test):
    """Downloads, fetches, and returns training and test data from a PSB2 problem.
    Caches downloaded datasets in `datasets_directory` to avoid multiple downloads.
    Returns a tuple of the form (training_examples testing_examples)
    where training-examples and testing-examples are lists of training and test
    data. The elements of these lists are dictionaries of the form:
    {'input1': first_input, 'input2': second_input, ..., "output1": first_output, ...}
    The training examples will include all hard-coded edge cases included in the suite,
    along with enough random cases to include `n-train` cases. The test examples
    will including a random sample of the random cases.
    Note that this function downloads and loads large datasets and can
    be slow, up to 1 minute.
    Parameters:
        `datasets_directory` - Location to download the PSB2 datasets.
        `problem_name` - Name of the PSB2 problem, lowercase and seperated by dashes.
            - Ex: indices-of-substring
        `n_train` - Number of training cases to return
        `n_test` - Number of test cases to return"""

    # Cannot sample more than 1 million examples for train or test
    assert n_train < 1000000, "Cannot sample more than 1 million examples"
    assert n_test < 1000000, "Cannot sample more than 1 million examples"

    # Load data
    edge_data = fetch_and_possibly_cache_data(datasets_directory, problem_name, "edge")
    random_data = fetch_and_possibly_cache_data(datasets_directory, problem_name, "random")

    # Make training and test sets
    if n_train < len(edge_data):
        train = random.sample(edge_data, n_train)
    else:
        train = edge_data
        train.extend(random.sample(random_data, n_train - len(edge_data)))

    test = random.sample(random_data, n_test)

    return (train, test)

def get_problem_names():
    """Returns a list of strings of the problem names in PSB2."""
    return PROBLEMS
