# Data File Utils

Collection of  Python scripts/utils for facilitating file manipulation tasks.

- [Data File Utils](#data-file-utils)
  - [Motivation](#motivation)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Installation](#installation)
  - [Exported scripts](#exported-scripts)
    - [analyze-record-tuples](#analyze-record-tuples)
    - [archive-dir](#archive-dir)
    - [backup-dir](#backup-dir)
    - [backup-file](#backup-file)
    - [compare-tab-files](#compare-tab-files)
    - [create-tmp-dir](#create-tmp-dir)
    - [delete-old-files](#delete-old-files)
    - [jsonl2json](#jsonl2json)
    - [tsv2json](#tsv2json)
    - [xlsx2tsv](#xlsx2tsv)
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

<img src="use_cases.png" width="400" height="400" alt="Use Cases diagram">


## Installation

See the install [instructions](INSTALL.md).


## Exported scripts

To use the following exported scripts:
- analyze-record-tuples
- archive-dir
- backup-dir
- backup-file
- compare-tab-files
- create-tmp-dir
- delete-old-files
- jsonl2json
- tsv2json
- xlsx2tsv
 
### analyze-record-tuples
This script will determine which records are missing from either of the two tab-delimited files. Some specified number of columns will make up the unique tuple
for each line/record.

### archive-dir

This script will archive the directory in-place using tar -zcvf and will apply suffix TIMESTAMP.tgz to the directory.

Sample invocation:

```shell
archive-dir /tmp/test-123/test-abc
test-abc/
test-abc/file-1
test-abc/file-2
test-abc/file-3
test-abc/file-4
Directory '/tmp/test-123/test-abc' successfully archived to 'test-abc_2024-01-02-212243.tgz'
```

### backup-dir

This script will backup the directory in-place and will apply suffix TIMESTAMP.bak to the directory.

Sample invocation:

```shell
backup-dir /tmp/test-123                                              
Backed-up '/tmp/test-123' to '/tmp/test-123.2024-01-02-210517.bak'
```

### backup-file

This script will backup the file in-place and will apply suffix TIMESTAMP.bak to the file.

Sample invocation:

```shell
backup-file setup.py                                                  
Backed-up 'setup.py' to 'setup.py.2024-01-02-205756.bak'
```

### compare-tab-files
This script will parse two tab-delimited files and generate a report to indicate which lines and columns are different.

### create-tmp-dir
This script will prompt the user for the following information and then create a temporary directory:
- root directory (default is /tmp)
- user directory (default is $USER)
- purpose

Sample invocation:

```shell
create-tmp-dir        
Enter the root directory: [/tmp]: 
Enter the user directory: [sundaram]: 
Enter the purpose of the directory: stock-checker
Created output directory '/tmp/sundaram/stock-checker/2024-01-02-213509'
```


### delete-old-files
This script will delete all old files belonging to the current or specified username in the /tmp or specified directory.

### jsonl2json
This script will parse a JSONL file and write a JSON file for each line in the JSONL file.

### tsv2json
This script will parse a tab-delimited file and write a JSON file.

### xlsx2tsv
This script will parse an Excel file and write a tab-delimited file for each worksheet.

Sample invocation:


```shell
xlsx2tsv --infile ~/projects/experiments/xlsx2tsv/genetics.xlsx 
--config_file was not specified and therefore was set to '/home/sundaram/projects/experiments/xlsx2tsv/venv/lib/python3.10/site-packages/data_file_utils/conf/config.yaml'
--outdir was not specified and therefore was set to '/tmp/xlsx2tsv/2023-12-22-142224'
Created output directory '/tmp/xlsx2tsv/2023-12-22-142224'
--logfile was not specified and therefore was set to '/tmp/xlsx2tsv/2023-12-22-142224/xlsx2tsv.log'
Sheet 'genes' has been written to '/tmp/xlsx2tsv/2023-12-22-142224/genes.tsv'
Sheet 'transcripts' has been written to '/tmp/xlsx2tsv/2023-12-22-142224/transcripts.tsv'
Sheet 'proteins' has been written to '/tmp/xlsx2tsv/2023-12-22-142224/proteins.tsv'
The log file is '/tmp/xlsx2tsv/2023-12-22-142224/xlsx2tsv.log'
Execution of '/home/sundaram/projects/experiments/xlsx2tsv/venv/lib/python3.10/site-packages/data_file_utils/xlsx2tsv.py' completed
```


## Contributing

Pull requests are welcome.<br>
For major changes, please open an issue first to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)
