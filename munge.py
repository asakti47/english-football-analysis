# Importing pandas
import pandas as pd

# Read text file into pandas DataFrame
# Seperate each columns by "," and make the first row of txt file the header
df = pd.read_csv("englandFootballData.txt", sep=",", header=0)

# Delete the first column of dates because it is irrelevant in our analysis
# because we already have the column specifying "Season"
del df['Date']

# For my analysis, I am only concerned about games in Tier 1
# So, I am going to delete all the games that are not in Tier 1
df.drop(df.loc[df['tier']!=1].index, inplace=True)


# Since "division" and "tier" are redundant considering all the games are from
# tier 1, I am going to delete both columns
del df['division']
del df['tier']

# Delete the unnecessary index column which comes as a byproduct of creating
# a pandas dataframe
df.set_index('Season', inplace=True)

# Delete the "FT" column because it creates formatting issues when the
# output csv file is opened on Excel
# Also, the column is unnecessary because we have a column for home goals and
# away goals as well as a column for the final result
del df['FT']

# Create a csv file from the dataframe
df.to_csv('clean_data.csv')

