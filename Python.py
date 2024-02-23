import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#READING EXCEL FILE
df = pd.read_excel("data.xlsx")
df = df.drop(df.columns[0],axis=1)
#DISPLAYING TOP FIVE ROWS OF DATASET
df.head()
#DISPLAYING SHAPE OF THE DATASET
df.shape
#DESCRIPTION OF DATASET
df.describe()
#UNIVARIATE ANALYSIS - NUMERICAL VARIABLES
# 1.PROBABILITY DENSITY FUNCTION (PDF)
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    if col != 'ID':
        plt.figure(figsize=(10, 6))
        sns.kdeplot(df[col], fill=True)
        plt.title(f'Probability Density Function (PDF) of {col}')
        plt.show()
#2.HISTOGRAMS
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    if col != 'ID':
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], kde=False, bins=20)
        plt.title(f'Histogram of {col}')
        plt.show()
#3.BOXPLOTS
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    if col != 'ID':
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()
#OUTLIERS IN EACH NUMERICAL COLUMN
q1 = df[col].quantile(0.25)
q3 = df[col].quantile(0.75)
iqr = q3 - q1
outliers = df[(df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)]
print(f'Outliers in {col} : {outliers}')
#UNIVARIATE ANALYSIS - CATEGORICAL VARIABLES
#4.COUNTPLOT
for col in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 6))
    sns.countplot( x=df[col])
    plt.title(f'Countplot of {col}')
    plt.show()
#BIVARIATE ANALYSIS
#Relationships between Numerical Columns
#1.Scatter Plot Between Salary and Computer Science
sns.scatterplot(data = df, x = 'ComputerScience', y = 'Salary', hue = 'Gender')
plt.title("Scatter plot between Salary and Computer Science ")
plt.xlabel('ComputerScience')
plt.ylabel('Salary')
plt.show()
#2.Hexbin plot between Salary and Openess_to_experience
sns.jointplot(data=df, x="openess_to_experience", y="Salary", hue="Gender")
plt.show()
#3.Pair Plots between Salary, Domain, ComputerProgramming,  ElectronicsAndSemicon, ComputerScience, MechanicalEngg, ElectricalEngg, TelecomEngg, CivilEngg
sns.pairplot(df[['Salary', 'Domain','ComputerProgramming','ElectronicsAndSemicon','ComputerScience','MechanicalEngg','ElectricalEngg','TelecomEngg','CivilEngg'
]])
plt.figure(figsize=(5, 5))
plt.show()
#Patterns between Categorical and Numerical Columns
#1.Swarm Plot between Salary and Specialization
sns.swarmplot(data=df, x = 'Salary', y = 'Degree',hue = 'Gender', orient="h")
plt.title("Swarm plot between Salary and Degree")
plt.figure(figsize=(20, 25))
plt.show()
#2. Box Plot Between Salary and Designation
sns.boxplot(data=df, x="Gender", y="Salary")
plt.title("Box plot between Salary and Gender")
plt.show()
#3. Bar Plot Between Salary and Gender
sns.barplot(df, x="Gender", y="Salary")
plt.title("Bar plot between Salary and Gender")
plt.show()
#Relationships between Categorical and Categorical Columns
#Stacked Bar Plots between Degree and Gender
sns.barplot(x='Degree', y='Gender', data=df)
plt.title('Stacked Bar Plot')
plt.show()
#Step - 5 - Research Question ( Does the preference of Specialisation depend on the Gender? )
sns.boxplot(data=df, x="Gender", y="Specialization")
plt.title("Box plot between Salary and Gender")
plt.figure(figsize=(20, 25))
plt.show()






























