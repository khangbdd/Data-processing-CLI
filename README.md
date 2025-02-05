# Data Preprocessing CLI

## Overview
This CLI tool provides a streamlined way to preprocess structured data files (CSV only) by offering various data cleaning and transformation functionalities. Users can execute individual preprocessing steps or chain multiple steps in a single command.

## Features
### Available Features ✅
1. **Load Data**
   Load a dataset from a specified CSV file.

2. **Handle Missing Values** (`mv`)
   - **Remove Missing Values** (`rm`)  
     Removes rows containing any missing values.
   - **Fill with Default** (`fl_<value>`)  
     Fills missing values with a specified default value (e.g., `fl_0` fills missing values with 0).

3. **Remove Duplicates** (`dp`)  
   Removes duplicate rows from the dataset.

4. **Normalization & Standardization** (`fs`)
   - **Normalize** (`nm`)  
   - **Standardize** (`sd`)  

5. **Export Processed File**
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
#### Load -> missing data -> feature scaling all feature with normalization -> handle suplication -> Output to path:
```sh
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_0-fs,nm-dp" ../../input.csv ../../output_directory
```

#### Fill missing values and remove duplicates:
```sh
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_100-dp" input.csv output.csv
```

#### Standardilize specific columns (Age and Glucose) and export:
```sh
/usr/local/bin/python3 data_tools.py --pipe="fs,sd_Age_Glucose" ../../input.csv ../../output_directory
```

## Installation
Only need to ensure Python is installed. Not have any other dependencies.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
MIT License

