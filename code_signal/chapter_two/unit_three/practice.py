import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

titanic = sns.load_dataset('titanic') 
# print(titanic.head())

# I would like to know how many male and female were on the ship 

gender = titanic['sex'].value_counts() 
print(gender)

# Graph the gender!
# gender.plot(kind='bar', title='Sex Distribution')
# plt.show()

# We could enhance the plots by adding labels and titles 

# gender.plot(kind='bar')
# plt.xlabel('Sex')
# plt.ylabel('Count')
# plt.title('Sex Distribution')
# plt.show()

# # Another plot 
# class_data = titanic['pclass'].value_counts()
# print(class_data)
# class_data.plot(kind='bar') 
# plt.xlabel('Passenger Class')
# plt.ylabel('Count')
# plt.title('Passenger Class Distribution') 
# plt.show()

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the Titanic dataset and assign it to titanic_df
titanic_df = sns.load_dataset('titanic')

# TODO: Create a bar chart of the above data. Use 'purple' color, 0.7 as the alpha value, and enable grid lines
gneder_data = titanic_df['sex'].value_counts()
gneder_data.plot(kind='bar', colorbar='purplr', alpha=0.7, grid=True)

# TODO: Add labels and a title to the plot
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Sex Distrubtion')

# TODO: Display the plot
plt.show()
