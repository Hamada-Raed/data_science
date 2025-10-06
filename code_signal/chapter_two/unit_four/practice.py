# Practice 1 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")

# Setup the aesthetics
sns.set(style="whitegrid", palette="coolwarm", font_scale=1.2)

# Create a new figure with the specific size
plt.figure(figsize=(12, 6))

# Create a Seaborn countplot
sns.countplot(x='pclass', data=titanic)

# Add a title, labels, and legend
plt.title('Passenger Class Count')
plt.xlabel('Passenger Class')
plt.ylabel('Count')

# Rotate x-axis labels by 45 degrees
plt.xticks(rotation=45)

# Display the plot
plt.show()


# practice 2  
# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Set the seaborn default aesthetic parameters
sns.set_style("whitegrid")
sns.set_palette("coolwarm")
sns.set(font_scale=1.5)

# Create a new figure with a specific size
plt.figure(figsize=(8, 6))

# Create a countplot that displays the number of passengers in each class
sns.countplot(x='class', data=titanic)

# Add a title and labels for the x and y axes
plt.title('Passenger Count by Class')
plt.xlabel('Class')
plt.ylabel('Number of Passengers')

# Rotate the x-axis labels by 30 degrees
plt.xticks(rotation=30)

# Display the plot
plt.show()

