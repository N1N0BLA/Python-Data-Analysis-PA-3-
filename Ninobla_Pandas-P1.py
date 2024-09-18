#PYTHON DATA ANALYSIS (PANDAS)
#JOSE MARTIN SJ. NINOBLA             2 ECE - D | September 4, 2024


import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')

# Display the first five rows
cars.head()

# Display the last five rows
cars.tail()