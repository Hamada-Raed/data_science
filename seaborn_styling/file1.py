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