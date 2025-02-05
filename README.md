# Data Preprocessing CLI

## Overview
This CLI tool provides a streamlined way to preprocess structured data files (CSV only) by offering various data cleaning and transformation functionalities. Users can execute individual preprocessing steps or chain multiple steps in a single command.

## Features
### Available Features ✅
1. **Load Data** (`--load <file_path>`)  
   Load a dataset from a specified CSV file.

2. **Handle Missing Values**
   - **Remove Missing Values** (`mv`)  
     Removes rows containing any missing values.
   - **Fill with Default** (`fl_<value>`)  
     Fills missing values with a specified default value (e.g., `fl_0` fills missing values with 0).

3. **Remove Duplicates** (`dp`)  
   Removes duplicate rows from the dataset.

4. **Normalization & Standardization**
   - **Normalize** (`nm`)  
     Scales data to a 0-1 range.
   - **Standardize** (`fs`)  
     Scales data to have a mean of 0 and a standard deviation of 1.

5. **Export Processed File** (`--export <output_path>`)  
   Saves the processed dataset to a specified CSV file.

6. **CLI Supports Chaining**  
   Multiple processing steps can be applied in a single command.

### Planned Features 🚧
1. **Handle Outliers**
   - Remove or replace extreme values.

2. **Convert Data Types**
   - Change data types (e.g., string to integer, float to categorical).

3. **Encode Categorical Data**
   - **One-Hot Encoding**
   - **Ordinal Encoding**

## Command Structure
### General Syntax
```sh
/usr/local/bin/python3 data_tools.py --pipe="<steps>" <inputFilePath> <outputPath>
```

### Pipe Structure
- `,` separates main and sub-services.
- `-` separates different main service lines (e.g., handling missing values, feature scaling).
- `_` separates service and parameter (e.g., `fl_0` means fill missing values with 0).

### Example Commands
#### Load and clean missing data:
```sh
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_0-fs,nm-dp" input.csv output.csv
```

#### Fill missing values and remove duplicates:
```sh
/usr/local/bin/python3 data_tools.py --pipe="fl_0-dp" input.csv output.csv
```

#### Normalize specific columns and export:
```sh
/usr/local/bin/python3 data_tools.py --pipe="nm" input.csv output.csv
```

## Installation
Ensure Python is installed, then install dependencies:
```sh
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
MIT License

