
# PSB2 - Python Sampling Library

A Python library for fetching and sampling training and test data for experimenting with the program synthesis dataset PSB2. The library will automatically download datasets to the given location, and will cache them to avoid repeated downloads.

## Installation

Easily installed using `pip`:

```text
pip install psb2
```

## Usage

There is one constant and one function available in this library. `psb2.PROBLEMS` is the list of all problems in the benchmark suite as strings:

```python
>>> import psb2
>>> psb2.PROBLEMS
['basement', 'bouncing-balls', 'bowling', 'camel-case', 'coin-sums', 'cut-vector', 'dice-game', 'find-pair', 'fizz-buzz', 'fuel-cost', 'gcd', 'indices-of-substring', 'leaders', 'luhn', 'mastermind', 'middle-character', 'paired-digits', 'shopping-list', 'snow-day', 'solve-boolean', 'spin-words', 'square-digits', 'substitution-cipher', 'twitter', 'vector-distance']
```

The `fetch_examples` function downloads (if necessary) and samples training and test data for a specific problem in PSB2:

```python
>>> import psb2
>>> (train_data, test_data) = psb2.fetch_examples("path/to/PSB2/datasets/", "fizz-buzz", 200, 2000)
>>> train_data
[{'input1': 1, 'output1': '1'},
 {'input1': 2, 'output1': '2'},
 {'input1': 3, 'output1': 'Fizz'},
 {'input1': 4, 'output1': '4'},
 ...
 {'input1': 405919, 'output1': '405919'},
 {'input1': 405789, 'output1': 'Fizz'}]
```

Each example in the returned `train_data` and `test_data` lists is a map containing one key for each input and each output. `train_data` includes all defined edge cases for a problem, as well as enough randomly generated cases to fill the training set (200 in the example above). `test_data` will sample `n_test` cases from the randomly generated cases.

## Citation

If you use these datasets in a publication, please cite the paper *PSB2: The Second Program Synthesis Benchmark Suite* and include a link to this repository.

BibTeX entry for paper:

```bibtex
@InProceedings{Helmuth:2021:GECCO,
  author =	"Thomas Helmuth and Peter Kelly",
  title =	"{PSB2}: The Second Program Synthesis Benchmark Suite",
  booktitle =	"2021 Genetic and Evolutionary Computation Conference",
  series = {GECCO '21},
  year = 	"2021",
  isbn13 = {978-1-4503-8350-9},
  address = {Lille, France},
  size = {10 pages},
  doi = {10.1145/3449639.3459285},
  publisher = {ACM},
  publisher_address = {New York, NY, USA},
  month = {10-14} # jul,
  doi-url = {https://doi.org/10.1145/3449639.3459285},
  URL = {https://dl.acm.org/doi/10.1145/3449639.3459285},
}
```

## License

Copyright © 2021 Thomas Helmuth

This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0.
