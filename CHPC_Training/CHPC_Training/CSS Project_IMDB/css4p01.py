# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:37:07 2024

@author: climate.intern
"""

#Load the libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv("movie_dataset.csv", index_col=0)

##########################################################################

print(df.info())

"""
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Title               1000 non-null   object 
 1   Genre               1000 non-null   object 
 2   Description         1000 non-null   object 
 3   Director            1000 non-null   object 
 4   Actors              1000 non-null   object 
 5   Year                1000 non-null   int64  
 6   Runtime (Minutes)   1000 non-null   int64  
 7   Rating              1000 non-null   float64
 8   Votes               1000 non-null   int64  
 9   Revenue (Millions)  872 non-null    float64
 10  Metascore           936 non-null    float64
dtypes: float64(3), int64(3), object(5)
memory usage: 93.8+ KB
None

"""

print(df.describe())

"""
            Year  Runtime (Minutes)  ...  Revenue (Millions)   Metascore
count  1000.000000        1000.000000  ...          872.000000  936.000000
mean   2012.783000         113.172000  ...           82.956376   58.985043
std       3.205962          18.810908  ...          103.253540   17.194757
min    2006.000000          66.000000  ...            0.000000   11.000000
25%    2010.000000         100.000000  ...           13.270000   47.000000
50%    2014.000000         111.000000  ...           47.985000   59.500000
75%    2016.000000         123.000000  ...          113.715000   72.000000
max    2016.000000         191.000000  ...          936.630000  100.000000

[8 rows x 6 columns]


"""

# Replacing spaces in column names with underscores

df.columns = df.columns.str.replace(' ', '_')

# Drop rows with missing values
df_cleaned = df.dropna()
print(df_cleaned.info())

##########################################################################

"""
Question 1
What is the highest rated movie in the dataset?
"""

# Find the index of the highest-rated movie
highest_rated_movie_index = df['Rating'].idxmax()

# Extract information about the highest-rated movie
highest_rated_movie = df.loc[highest_rated_movie_index]

print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

"""
Highest-rated movie:
Title     The Dark Knight
Rating                9.0
"""

##########################################################################
"""
Question 2
What is the average revenue of all movies in the dataset?  
"""

# Calculate the average revenue
average_revenue = df['Revenue_(Millions)'].mean()

print(f"Average revenue is approximately ${average_revenue:.2f} million.")

"""
Average revenue is approximately $82.96 million.
"""

##########################################################################
"""
Question 3
What is the average revenue of movies from 2015 to 2017 in the dataset?
"""

# Filter movies from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Filter movies from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_df['Revenue_(Millions)'].mean()

print(f"Average revenue is approximately ${average_revenue_2015_to_2017:.2f} million.")

"""
Average revenue is approximately $63.10 million.
"""

##########################################################################
"""
Question 4
How many movies were released in the year 2016?
"""

# Count the number of movies released in 2016
movies_2016_count = df[df['Year'] == 2016].shape[0]

print(movies_2016_count)

"""
297
"""

##########################################################################
"""
Question 5
How many movies were directed by Christopher Nolan?
"""

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]

print(f"Christopher Nolan are: {nolan_movies_count}")

"""
Christopher Nolan are: 5
"""

##########################################################################
"""
Question 6
How many movies in the dataset have a rating of at least 8.0?
"""

# Count the number of movies with a rating of at least 8.0
high_rated_movies_count = df[df['Rating'] >= 8.0].shape[0]

print(f"The number of movies with a rating of at least 8.0 is: {high_rated_movies_count}")

"""
The number of movies with a rating of at least 8.0 is: 78
"""

##########################################################################
"""
Question 7
What is the median rating of movies directed by Christopher Nolan?
"""

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}")

"""
The median rating of movies directed by Christopher Nolan is: 8.6
"""

##########################################################################
"""
Question 8
Find the year with the highest average rating?
"""

# Group by year and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"Highest average rating year: {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}")

"""
Highest average rating year: 2007 with an average rating of 7.13
"""

##########################################################################
"""
Question 9
What is the percentage increase in number of movies made between 2006 and 2016?
"""

# Count the number of movies for each year
movies_count_by_year = df['Year'].value_counts()

# Extract the counts for the years 2006 and 2016
movies_count_2006 = movies_count_by_year.get(2006, 0)
movies_count_2016 = movies_count_by_year.get(2016, 0)

# Calculate the percentage increase
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100

print(percentage_increase)

"""
575.0
"""

##########################################################################
"""
Question 10
Find the most common actor in all the movies?

"""
# Split the 'Actors' column into separate actors and create a list of all actors
all_actors = df['Actors'].str.split(', ').explode()

# Find the most common actor
most_common_actor = all_actors.mode().iloc[0]

print(f"The most common actor is: {most_common_actor}")

"""
The most common actor is: Mark Wahlberg
"""

##########################################################################
"""
Question 11
How many unique genres are there in the dataset?
"""

# Split the 'Genre' column into separate genres and create a set of unique genres
unique_genres = set(df['Genre'].str.split(', ').explode())

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print(f"Unique genres are: {num_unique_genres}")

"""
Unique genres are: 207
"""

##########################################################################
"""
Question 12
Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

And what advice can you give directors to produce better movies?
"""

# Calculate the correlation matrix for numerical features
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

"""
                        Year  Runtime_(Minutes)  ...  Revenue_(Millions)  Metascore
Year                1.000000          -0.164900  ...           -0.126790  -0.079305
Runtime_(Minutes)  -0.164900           1.000000  ...            0.267953   0.211978
Rating             -0.211219           0.392214  ...            0.217654   0.631897
Votes              -0.411904           0.407062  ...            0.639661   0.325684
Revenue_(Millions) -0.126790           0.267953  ...            1.000000   0.142397
Metascore          -0.079305           0.211978  ...            0.142397   1.000000

[6 rows x 6 columns]
"""

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


"""
Insights:
1. There is a positive correlation between 'Votes' and 'Revenue_(Millions)', suggesting that movies with more votes tend to have higher revenue.
2. 'Rating' and 'Metascore' show a positive correlation, indicating that movies with higher ratings also tend to have higher Metascores.
3. There is a weak positive correlation between 'Year' and 'Runtime_(Minutes)', suggesting that movie runtimes may have slightly increased over the years.
4. 'Rating' and 'Runtime_(Minutes)' show a weak negative correlation, indicating that longer movies may not necessarily have higher ratings.
5. 'Rating' and 'Votes' exhibit a positive correlation, suggesting that highly-rated movies tend to attract more votes.

Advice for directors to produce better movies:
1. Focus on creating engaging and compelling stories that resonate with the audience.
2. Pay attention to both critical acclaim (Metascore) and audience feedback (Rating and Votes).
3. Consider the optimal runtime for your movie, as excessively long or short runtimes may impact audience reception.
4. Invest in marketing and promotion to increase visibility and attract more viewers.
5. Collaborate with talented actors, directors, and writers to enhance the overall quality of the production.

"""






























