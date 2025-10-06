import numpy as np 
import pandas as pd 


# Numpy:
# 1. Trigonometric Functions: np.sin(), np.cos(), np.tan()
# 2. Exponential Function: np.exp()
# 3. Logarithmic Functions: np.log(), np.log10()
# 4. Array Operations: +, -, *, /, **, 1/array (inverse)
# 5. Matrix Multiplication: @ or np.matmul()
# 6. Transpose: np.transpose() or .T
# 7. Min/Max Values: np.min(), np.max()
# 8. Random Number Generation: np.random.rand(), np.random.randint()
# 9. Mean & Std Dev: np.mean(), np.std()
# 10. Reshaping Arrays: array.reshape((rows, cols))
# 11. Array Creation: np.arange() (evenly spaced values), np.linspace() (over a range)
# 12. Special Arrays: np.zeros(), np.ones(), np.eye()

# Pandas:
# 13. Series: Create series from lists/arrays with optional indexing.
# 14. DataFrames: Create dataframes from lists/dictionaries, access columns/rows via names or indices.
# 15. Accessing Data: df['col_name'], df.col_name, iloc[], loc[].
# 16. Slicing & Indexing: Row/column slicing, selecting specific rows/columns.
# 17. Modifying Data: Assign new values using slicing.
# 18. Mathematical Functions: min(), max(), mean(), median(), mode().
# 19. Sorting & Aggregating: sort_values(), value_counts().
# 20. File Operations: Read CSV files (pd.read_csv()), Save CSV files (to_csv()).
# 21. Combining DataFrames: Concatenate (pd.concat()), Join (join()), Merge (merge()).


# Start: 
num_list = np.arange(0,10,2)
# print(num_list) 
# print(num_list.mean())
# print(num_list.std()) 


list_in_panda = pd.Series(num_list)
print(list_in_panda)

# You can make indexes in panda series 

list_of_indexes = ["a", "b", "c", "d", "e"]

print(pd.Series(num_list, index = list_of_indexes))

num_list_plus_two = list_in_panda + 2
print(num_list_plus_two)

num_list_2 = pd.Series(np.arange(4,14,2), index = list_of_indexes)

print("Different Series:", num_list - num_list_2)

# Two dimensional panda 

students = ["John", "Jane", "Jack"]

student_data = pd.DataFrame(students, columns = ['Names'])

grades = [85, 90, 95] 

df2 = pd.DataFrame({'Student': students, 'Grades': grades})

print(df2)


random_data_1 = pd.DataFrame(np.random.randn(5,2), columns = ['A', 'B'])
print(random_data_1)

# df3 = pd.DataFrame(np.random.randn(5,4))

# Accessing data from panda dataframe (dict), 

print(df2['Grades'])


operators = ['AT&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

#creating a Series from lists
telecom = pd.Series(revenue, index=operators)
print(telecom)
print("Print value: ",telecom[0])
print("First two values: ", telecom[0:2])


print("/" * 30)
# creating the dataframe using dictionary
store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})

print(store_data)

print('First two rows',store_data.head(2))
print('Last two rows', store_data.tail(2))
print("Print with speacific index: ", store_data[2:3])
print("Print with speacific index: ", store_data.loc[2])  # loc is used to access a row with specific index.
print("Print with speacific index: ", store_data.loc[0:2])  #

# print(store_data.describe()) # gives statistical summary of numerical columns 

# Now printting specific column 
print(store_data['location'])

print(store_data.location)  # another way to access a column


print(store_data[['location', 'type']])  # accessing multiple columns
# accessing rows with two steps. 
print(store_data[::2]) 


# Loc method to access rows and columns 

print(store_data.loc[1])
print(store_data.loc[[0],['location']])
print(store_data.loc[[0,2,3], ['location', 'type']])

print('//' * 10)
# iloc method to access rows and columns with integer index 

print(store_data.iloc[[0,2],[0,2]])


# this the way of mpdifying a value in dataframe. 
store_data.iloc[[0],[0]] = 'Hamada' 
# Or 
store_data.iloc[0,0] = 'Ahmed'
print(store_data)

print(store_data['total_bill']> 80)

print(store_data.loc[store_data['total_bill'] > 80])


# Adding new column to dataframe. 

store_data['passion'] = ['High', 'Medium', 'Medium', 'Low', 'High']
print(store_data)

# Dropping a column from dataframe. 
store_data = store_data.drop('passion', axis = 1) # axis = 1 means column, axis = 0 means row. 
print(store_data)





df3 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [24, 27, 22, 32],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']

})
print(df3)

copy_df3 = df3.copy() 

# add a new column 
copy_df3['salary'] = [70000, 80000, 60000, 90000]

print(copy_df3)

# Drop the last column // in this way you the salary still exist  
copy_df3.drop('salary', axis = 1)
print(copy_df3.drop('salary', axis = 1))


# But to remove the salary, you could use inplace = true

copy_df3.drop('salary', axis = 1, inplace = True)
print(copy_df3)

# We could also remove muliple columns simultaneously
print('/'*100)
copy_df3.drop(['city', 'age'], axis=1, inplace= True)

print(copy_df3)

# add new columns 
copy_df3['city'] = ['A', 'B', 'C', 'D']
print(copy_df3)

print("0" * 100) 

print(copy_df3.loc[[0],['city', 'name']])


copy_df3.loc[len(copy_df3)] = ['E', 'Eve']  # Assuming columns are ['city', 'name']
print(copy_df3)

# This is the way to remove the a record (row)
copy_df3.drop(2, axis = 0, inplace = True)

print(copy_df3)
print("0" * 100)
 
# After deleting a record, it is very important to reset the index using reset_index function 

copy_df3.reset_index()
print(copy_df3)

# In this case, as you could see the output nothing changes, but when you adjust 
# the paramenter of the reset_index(), you could see the changes direct 

copy_df3.reset_index(drop=True, inplace=True)

print(copy_df3)



print("/" *100)
print("*" *100)
print("?" *100)
# We will use three methods to combine the dataframe (concat, join, and marge) 

df4 = pd.DataFrame({
    'name' : ['Hamada', 'Raed'], 
    'age': [25, 40] 
}, index=[0,1]) 

df5 = pd.DataFrame({
    'name': ['Nehal', 'Mohammad'], 
    'age' : [22, 30]
}, index=[2,3])

print(df4,'\n' ,df5)

# Use concat to combine the data together! 

# axis = 0 , this means you will combine the data next down to each others 
df6 = pd.concat([df4, df5], axis=0)
print('Data Frame number 6 \n',df6)

# add new record to df6  
df6.loc[len(df6)] = ['Khalil', 67]
df6.loc[len(df6)] = ['Hamada', 25]
print('Data Frame number 6 after adding a new record \n',df6)

# The difference between add row and column is when you are adding row, you specifiy 
# the location using (loc function), then you provide the data, while when you are adding column, 
# you provide the name of the columns, the you provide the data as array. 


# **Merge and Join**

# * Merge combines dataframes using a column's values to identify common entries

# * Join combines dataframes using the index to identify common entries
# 
# we use concat to combine data frame together. 
# 
# Let use the Merge and compare it with concat to see the different between them. 
#

# how is the parameter in pd.merge as union (all), on is also a parameter, 
# we use it to know we are mergeing based on which column

df7 = pd.merge(df6, df5, how='outer', on='name')
print('data frame number 7 with merge function using outer \n ',df7)


# inner keeps only the rows with matching values in the specified column(s)
df7 = pd.merge(df6, df5, how='inner', on='name') 
df8 = pd.merge(df5, df6, how='inner', on='age') 
print('data frame number 7 with merge function using inner and name \n ',df7) 
print('data frame number 8 with merge function using inner and age \n ',df8) 



# We have four different types of merge are (outer, inner, left, and right) 

# I will exam them in new data frame. 

print("%" * 100)
df10 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [10, 20, 30]}, index=[0,1,2])
df11 = pd.DataFrame({'Key': ['B', 'C', 'D'], 'Value2': [40, 50, 60]}, index=[3,4,5])

print("Print data frame number 10 and 11 \n", df10, '\n',df11) 

print('Concat method \n', pd.concat([df10, df11], axis=0))

# outer means all record with out duplicated! 
print('Merge method using outer \n', pd.merge(df10, df11, how='outer', on='Key'))

# inner means the intersection between two dataframe 
print('Merge method using inner \n', pd.merge(df10, df11, how='inner', on='Key'))

# left inner 
print('Merge method using left inner\n', pd.merge(df10, df11, how='left', on='Key'))
print('Merge method using right inner\n', pd.merge(df10, df11, how='right', on='Key'))



print("Review " * 10)
# Review all things 

array_1 = np.arange(4)


# convert array or list to series using panda 

array_panda = pd.Series(array_1, index=['a', 'b', 'c', 'd'])
print(array_panda)

for i in array_panda:
    print(i)


list_of_student = ['Hamada', 'Ahmad', 'Khalil']
df_list = pd.DataFrame(list_of_student, columns=['Name'])

print(df_list)

grades = ['A', 'B', 'C'] 

df_dict = pd.DataFrame({'Name' : list_of_student, 'Grades': grades})
print(df_dict)

# DataFrame is a dict (assess and modify) 

# To access data in dict you need the key 



series_of_number = pd.Series(np.arange(10)) 

print('Print first element in the series\n',series_of_number[0])
print('Print first five elements in the series\n', series_of_number[:5])
print('Print last element in the series\n', series_of_number[-1:])
print('Print muliple element in ther series\n', series_of_number[[0,2,3,6,9]])
print('Print numbers using the key (index) \n', series_of_number[5])


# Now, we moved to deal with dataframe: one more time, DF is a dict 

store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})

print(store_data)

# If you want to access row use head function or index as [], you could also use [start:end:steps]
# But, if you want to access columns, use the name of the column as store_data['name_of_column']
print(store_data.head(4))


# Now, we will learn two different functions, we use them to identify the location of the entries. 
# These functions are loc, and iloc, there is a small different between them, but both of them have the same functionality


# This way if you want to return the whole columns 
print('Location of the first row\n', store_data.loc[0])
print('Location of the first two rows\n', store_data.loc[0:1])
print('Location of even rows\n', store_data.loc[::2])
# This way is you want to return data with specific columns 
print('Location of first row with specific column\n',store_data.loc[0]['gender'])

# Using iloc = index.location means instead of using words to identify the column use number. 

print('Location using iloc function of first column', store_data.iloc[0][0])
print('Location using iloc function of first column', store_data.iloc[0])

# accessing selected rows and columns using iloc method row number 1 and 4 with column index 0 and 2 
print(store_data.iloc[[1,4],[0,2]])



data_cust = pd.DataFrame({"customerID":['101','102','103','104'], 
                        'category': ['Medium','Medium','High','Low'],
                        'first_visit': ['yes','no','yes','yes'],
                        'sales': [123,52,214,663]},index=[0,1,2,3])

data_cust_new = pd.DataFrame({"customerID":['101','103','104','105'], 
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])

print('Concat the data_cust with data_cust_new', pd.concat([data_cust,data_cust_new] , axis=0))
print('Concat the data_cust with data_cust_new', pd.concat([data_cust,data_cust_new] , axis=1))

data_quarters = pd.DataFrame({'Q1': [101,102,103],
                              'Q2': [201,202,203]},
                               index=['I0','I1','I2'])

data_quarters_new = pd.DataFrame({'Q3': [301,302,303],
                                  'Q4': [401,402,403]},
                               index=['I0','I2','I3']) 

print('Join method',  data_quarters.join(data_quarters_new, how='right'))
print('Join method',  data_quarters.join(data_quarters_new, how='left'))

# The only different between merge and join, 
# in merge we specifiy the column on merge using on= 
# in join is always use the index labels 


print("/"*100)

path_file = '/Users/Hamada/Desktop/DS/test_data.csv'

data = pd.read_csv(path_file)
print(type(data))


data_cust_new_save = pd.DataFrame({"customerID":['101','103','104','105'], 
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])


data_cust_new_save.to_csv('/Users/Hamada/Desktop/DS/saved_data.csv')


# Once we have csv file, we could implement some functions on the data!



print('print first two rows from the head\n',data.head(2))
print('print last two rows from the bottom\n',data.tail(2))

# We use shape to know how much rows and columns 

print('Number of rows and columns using shape', data.shape)

# we use info function to know the data type of the 'columns 
print ('What is the data type of the column? ', data.info())


# We have some math functions like min, max, unique, value_counts, mean, mediam, mode 

# convert data to dataframe  

print('Min value of age is: ', data['Age'].min())
print('Max value of age is: ', data['Age'].max())
print('Avarage of age is: ', data['Age'].mean())
print('Mediam of age is:', data['Age'].median())
print('Mode of age is: ', data['Age'].mode())
print('Mode of age is: ', data['Age'].mode()[0])

print(data)

def add_one_of_age(a):
    return a + 1

data['new_age'] = data['Age'].apply(add_one_of_age)

data.drop('Age', axis=1, inplace=True)

print(data.head())

print('Sort the data', data.sort_values(by='new_age', ascending=True))
print('Count', data.value_counts())