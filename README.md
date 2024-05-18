# Simple Templating Engine

## Overview
This project, `assign5.py`, is a Python script that functions as a simple templating engine. It takes a generic template with placeholders, a set of input data files, and a date to produce instantiated templates. This script emphasizes the use of Python's string manipulation capabilities and file handling to automate the generation of content based on template structures.

## Features

- **Template Instantiation**: Fills placeholders in a template with actual data from input files.
- **Selective Processing**: Only processes items with an inventory level below 10% of the maximum quantity.
- **Dynamic Date Handling**: Incorporates a user-specified date into the generated output, replacing the placeholder in the template.
- **Output Management**: Writes the output to a specified directory, with each file named after the item number.

## Template and Data Format

- **Data Files**: Expected to be in a directory specified by the user, each named with a four-digit item number and `.item` extension.
  - Format: Three lines containing the item's simple name, quantities, and a descriptive body.
- **Template Format**: Includes placeholders marked with double angle brackets (e.g., `<<simple_name>>`) to be replaced by corresponding data from the input files.

## Usage

### Running the Script
Execute the script with four arguments:
1. Path to the directory containing data files.
2. Path to the template file.
3. Date in MM/DD/YYYY format.
4. Path to the output directory.

```bash
python assign5.py ./data_directory_path template_file_path MM/DD/YYYY ./output_directory_path
