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

7. **Handle Outliers by Z-score** (`ol`)
   - Remove outliers (`rm`)
   - Replace outliers (`rp`)
   You could choose feature to apply check outlier. (e.g., ol,rm_Age_Glucose)
   If you not give the feature to apply, then the tool will check outlier for all feature in csv.

8. **Encode Categorical Data** (`ec`)
   - **One-Hot Encoding** (`oh`)
   - **Ordinal Encoding** (`od`)
Please noted that you need to provide feature name as parameter to start encoding process or the tools'll raise a issue.
Example:
```sh
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_0-fs,nm-ec,oh" ../../input.csv ../../output_directory
```
Will throw a request to add a feature name as params for `oh`.

```sh
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_0-fs,nm-ec,oh_Age_Glucose" ../../input.csv ../../output_directory
```
This will work.

### Planned Features 🚧
None, all plan features finished. (Will update more if have a request)

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
/usr/local/bin/python3 data_tools.py --pipe="mv,fl_100-dp" ../../input.csv ../../output_directory
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

