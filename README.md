
# Python Data Analysis with Pandas

This repository contains solutions for **Experiment 3** of the course *Advanced Computer Programming and Algorithms (ECE 2112)* at the University of Santo Tomas, Faculty of Engineering. The experiment focuses on using Python's Pandas library for data analysis.

## Objective

The goal of this experiment is to:

1. Identify and use functions within the Pandas library.
2. Apply these functions to analyze and manipulate a dataset using Python.

## Assignment Overview

The tasks in this assignment are divided into two problems, both involving operations on a dataset related to cars. The dataset can be found [here](http://bit.ly/Cars_file).

### Problem 1: Loading and Displaying Data

**File:** `Surname_Pandas-P1.py`

```python
import pandas as pd

# Load the CSV file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

# Display the first five rows of the DataFrame
# The .head() function retrieves the first five rows.
cars.head()

# Display the last five rows of the DataFrame
# The .tail() function retrieves the last five rows.
cars.tail()
```

#### Explanation:
- **`pd.read_csv()`**: Loads the dataset from a CSV file into a DataFrame object named `cars`.
- **`.head()`**: Displays the first five rows of the dataset.
- **`.tail()`**: Displays the last five rows of the dataset.

### Problem 2: Data Subsetting, Slicing, and Indexing

**File:** `Surname_Pandas-P2.py`

```python
import pandas as pd

# Load the CSV file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

### PROBLEM A
# Display the first five rows with only odd-numbered columns (1, 3, 5, 7...).
# The ":5" slices the first five rows, and "::2" selects every second column (starting from column index 0).
cars.iloc[:5, ::2]

### PROBLEM B
# Display the row that contains the 'Model' as 'Mazda RX4'.
# The .loc method is used to locate rows that match a specific condition.
cars.loc[cars['Model'] == 'Mazda RX4']

### PROBLEM C
# Find how many cylinders the 'Camaro Z28' has.
# The .loc method selects the row where 'Model' is 'Camaro Z28', and retrieves the 'cyl' column.
cars.loc[(cars['Model'] == 'Camaro Z28'), ['cyl']]

### PROBLEM D
# Create a list of car models of interest.
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']

# Use .loc and .isin to filter the DataFrame and retrieve the 'Model', 'cyl', and 'gear' columns 
# for the specified car models in the list.
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
```

#### Explanation:
- **PROBLEM A**: Uses `.iloc[]` to slice the DataFrame by selecting the first five rows and every second column (i.e., odd-numbered columns).
- **PROBLEM B**: `.loc[]` is used to filter the DataFrame and find the row where the 'Model' is 'Mazda RX4'.
- **PROBLEM C**: `.loc[]` filters the DataFrame to find the 'Camaro Z28' row and returns the value in the 'cyl' column, which corresponds to the number of cylinders.
- **PROBLEM D**: The `.isin()` method checks whether the 'Model' column contains any of the car models in the provided list. It then extracts the number of cylinders and the gear type for those models.

## How to Run

1. Download and Install the Anaconda Distribution app in your Computer
   ```
   https://www.anaconda.com/download
   ```

2. Launch the Jupiter Notebook
   ```
   ```
3. Install the required packages:
   ```
   pip install pandas
   ```

4. Copy Paste the codes and shift + enter to see the Output

## Requirements

- Python 3.x
- Pandas library

You can install the required dependencies by running:
```
pip install pandas
```

