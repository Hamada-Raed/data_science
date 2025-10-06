# import necessary library to help with data!
import numpy as np
import pandas as pd 

# import necessary library to visualization! 
import matplotlib.pyplot as plt 
import seaborn as sns 

# head(n): Displays the first n entries of the DataFrame.
# tail(n): Displays the last n entries of the DataFrame.
# shape: Returns the number of rows and columns of the DataFrame.
# info(): Provides a concise summary of the DataFrame.
# describe(): Generates descriptive statistics that summarize a dataset's distribution's central tendency, dispersion, and shape.

# %matplotlib inline

# load  the data to start reading it and manipulating it 
df = pd.read_csv('Automobile.csv') 

# print the first 5 rows 
print(df.head()) 

# Print how many rows and columns in the file using shape function
print('Print how many rows and columns: ', df.shape )
# Output is (201, 26) which means 201 rows and 26 columns

# Use info() function to see the datatype of columns (Dtype)
print(df.info())

# Use describe(include=all) function to 
print('Describe of the data (it shows you the mean, max, min, etc) ', df.describe())
print('Describe of the data (it shows you the mean, max, min, etc) include = all, with extra values', df.describe(include='all'))

# Print the describe(include='all').T to see 
print('Print the information about the data we have using describe() function:\n ', df.describe(include='all').T)

print('Print the max value of price', df['price'].max())
print('Print the min value of price', df['price'].min())
print('Print the count of each value of price', df['price'].value_counts())

# We use histogram to understand the distribution of the continuous numerical variable
# It breaks the range of the continuous variable into a intervals of equal length nad then counts the number of observations in each interval 
# We will use the hisplot() function of seaborn to create histograms.

# The histplot() function takes two parameter the data and x-axis, y-axis will be the count
sns.histplot(data=df, x='price')

plt.title('Histogram: Price') 
plt.xlim(3000, 5000)
plt.ylim(0,70)
plt.xlabel('Price of cars')
plt.ylabel('Frequency') 
sns.histplot(data=df, x='price', color='red')






