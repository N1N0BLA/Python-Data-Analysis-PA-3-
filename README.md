
# Python Data Analysis with Pandas
JOSE MARTIN SJ. NINOBLA
2 ECE - D | September 18, 2024

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

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')

# Display the first five rows
cars.head()

# Display the last five rows
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

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')

###PROBLEM A
# the value of ":5" selects ONLY the first 5 rows of the DataFrame without including the 5th variable/value
# The double colon "::2" selects every second column.
cars.iloc[:5,::2]

###PROBLEM B
#the code ".loc" is used to locate and print the row that contains the : 'Model' that is of 'Mazda RX4'
cars.loc[cars['Model']=='Mazda RX4'] 


###PROBLEM C
#the code ".loc" is used to locates row that contains the : 'Model' that is of 'Camaro Z28' but only then prints the number of cylinders it has
cars.loc[(cars['Model']=='Camaro Z28'), ['cyl']]

###PROBLEM D
#Creates a list of car models required
models = ['Mazda RX4','Ford Pantera L','Honda Civic']

#the code ".loc" is used to locate the requirements which are the model of a car and outputs the required information with it(cylinders, gears)
#the code ".isin" checks if any 'Model' in the DataFrame matches the car models in the list.
cars.loc[cars['Model'].isin(models),['Model','cyl','gear']]

#end
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

