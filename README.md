# Data File Utils
Collection of  Python scripts/utils for facilitating file manipulation tasks.

- [Data File Utils](#data-file-utils)
  - [Motivation](#motivation)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Installation](#installation)
    - [Developers](#developers)
  - [Exported scripts](#exported-scripts)
    - [tsv2json](#tsv2json)
    - [jsonl2json](#jsonl2json)
  - [compare-tab-files](#compare-tab-files)
    - [analyze-record-tuples](#analyze-record-tuples)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)



## Motivation

Explain what the motivation was for developing this package OR<br>
explain how this package was improved after being forked.


## Improvements

Please see the [TODO](TODO.md) for a list of upcoming improvements.


## Use Cases

![use case diagram](use_cases.png)


## Installation

Clone this project and then run the pip installer

```bash
git clone https://github.com/jai-python3/data-file-utils.git
cd data-file-utils
virtualenv -p python3 venv
source venv/bin/activate
python setup.py sdist
pip install .
```

You can uninstall like this:

```bash
pip uninstall data-file-utils
make clean
```

### Developers

If you modify the code in this package in your local virtual environment:

```shell
pip uninstall data-file-utils
make clean
python setup.py sdist
pip install .
```
If you want to export the code in this package to the PYPI repository:

Install `twine` and `setuptools`:

```shell
pip install twine setuptools
```


Build the Distribution Package

```shell
python setup.py sdist bdist_wheel
```

Configure your ~/.pypirc:

```bash
[pypi]
  username = __token__
  password = pypi-YOUR-TOKEN
```

Upload Your Package to PyPI

```shell
twine upload dist/*
```


Now you can install your package in your Python virtual environment

```shell
pip install data-file-utils
```




![class diagrams](class_diagrams.png)



## Exported scripts

To use the following exported scripts:
- tsv2json
- jsonl2json
- compare-tab-files
- analyze-record-tuples

### tsv2json
This script will parse a tab-delimited file and write a JSON file.

### jsonl2json
This script will parse a JSONL file and write a JSON file for each line in the JSONL file.

## compare-tab-files
This script will parse two tab-delimited files and generate a report to indicate which lines and columns are different.

### analyze-record-tuples
This script will determine which records are missing from either of the two tab-delimited files. Some specified number of columns will make up the unique tuple
for each line/record.



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)
