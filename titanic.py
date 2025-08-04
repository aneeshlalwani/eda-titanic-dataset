#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 17:46:45 2025

@author: aneesh

"""
#%%
import pandas as pd
print(pd.__version__)
#%%
df = pd.read_csv('/home/aneesh/Desktop/data/code/Python/pandas/titanic_data.csv')
#%% Data Exploration

## Columns into List
print(df.columns.tolist())
## Data information
print(df.info())
## Check for missing values
print(df.isnull().sum())
#%% Data Cleaning

# Dropping Cabin column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Filling missing 'Embarked' values with most frequent (mode)
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarked_mode, inplace=True)

# Filling missing 'Age' Values with median which is safe for skewed data
age_median = df['Age'].median()
df['Age'].fillna(age_median, inplace=True)

# Verifying missing values
print("Verifying Data Cleaning...")
print(df.isnull().sum())
#%% Basic Analysis
# Overall Survival

survival_counts = df['Survived'].value_counts()
survival_rate = df['Survived'].mean()

print("Survival Counts:")
print(survival_counts)
print('\nOverall Survival Rate: {:.2f}%'.format(survival_rate * 100))
#%%
# Survival Rate by Gender
gender_based_survival = df.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender (%):\n")
print(gender_based_survival * 100)
#%%
# Checking how ticket class effects the survival
ticket_class_based_survial = df.groupby('Pclass')['Survived'].mean()
print('Ticket Class Based Survival Rate (%):\n')
print(ticket_class_based_survial * 100)
#%% Survival by Age Group

# Categoriesing passangers in age group
def age_group(age):
    if age < 12:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)

# Calculate survial rate by age group
age_based_survival = df.groupby('AgeGroup')['Survived'].mean() * 100

print('Age based Survival Rate is \n')
print(age_based_survival)
#%% Family Size Impact Analysis
df['FamilySize'] = df['SibSp'] + df['Parch']
print(df['FamilySize'])
# Survival rate by family size
family_based_survial = df.groupby('FamilySize')['Survived'].mean() * 100
print("Survival Rate by Family Size (%):\n")
print(family_based_survial)
#%% Fare vs Survival

# Comparing Mean Fare of Survived vs Not Survived
fare_based_survial = df.groupby('Survived')['Fare'].mean()
print("Average Fare by Survival Status:\n")
print(fare_based_survial)

#%% Data Visualization Libraries

import matplotlib.pyplot as plt
import seaborn as sns

print("matplotlib version:", matplotlib.__version__)
print("seaborn version:", seaborn.__version__)
#%% Bar Plot

# Styling
sns.set(style='whitegrid')
# Plotting survival rate by gender
ax = sns.barplot(x='Sex', y='Survived', data=df)
# Adding titles and labels
ax.set_title('Survival Rate by Gender')
ax.set_ylabel('Survival Rate')
ax.set_xlabel('Gender')
ax.set_ylim(0, 1)

plt.show()
#%% Count Plot

sns.set(style='darkgrid')

axes = sns.countplot(x='Survived', data=df, palette='Set2')

axes.set_title('Passenger Survival Counts')
axes.set_xlabel('Survived (0 = No, 1 = Yes)')
axes.set_ylabel('Number of Passengers')

plt.show()
#%% Pie Chart
survival_counts = df['Survived'].value_counts()
labels = ['Did Not Survive', 'Survived']
colors = ['lightcoral', 'lightgreen']

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(survival_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Survival Proportion (Pie Chart)')
plt.axis('equal')  # Makes pie chart a circle

plt.show()
#%%

