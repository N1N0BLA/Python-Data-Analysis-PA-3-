#start

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