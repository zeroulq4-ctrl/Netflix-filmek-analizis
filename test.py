
#TÉMA : NETFLIX MOVIES AND TV SHOWS
import matplotlib.pyplot as plt
import seaborn as sns # daigram konyvtar
import numpy as np
import scipy as sp #szamitasok, tudomanyomós clc
import os
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

 


df = pd.read_csv(r"C:\Users\hmate\Downloads\netflix_titles.csv.zip")

#ELSO KERDES : Hogyan változott a Netflix kinálata az évek során?

df['release_year'].value_counts().sort_index().plot(
    kind='line',
    figsize=(12,6)
)

plt.title("Netflix tartalmak megjelenési éve szerint")
plt.xlabel("Év")
plt.ylabel("Darabszám")
plt.grid(True)
plt.show() 


#MASODIK KERDES : Film vagy sorozat van tobb a Netflixen?

df['type'].value_counts().plot(kind='pie')


#harmadik kerdes : Melyik orszagban van a legtobb film vagy sorozat a Netflixen?

top_countries = df['country'].value_counts().head(10)

print(top_countries)

top_countries.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 ország a Netflix kínálatában")
plt.show() # ez a sor a country oszlopban található értékek előfordulásait számolja meg, majd azokat csökkenő sorrendbe rendezi, és az első 10 országot jeleníti meg.

#negyedik kerdes : Melyik a leggyakoribb műfaj a Netflixen?
genres = df['listed_in'].str.split(', ').explode()

genres.value_counts().head(10).plot(kind='bar')
plt.title("Leggyakoribb műfajok")
plt.show()
 
#OTODIK KERDES : Hogyan alakult a filmek átlagos hossza az évek során?

movies = df[df['type'] == 'Movie'].copy()

movies['duration_num'] = movies['duration'].str.extract('(\d+)').astype(float)
avg_duration = movies.groupby('release_year')['duration_num'].mean()

avg_duration.plot(figsize=(12,6))

plt.title("Filmek átlagos hosszának változása")
plt.xlabel("Év")
plt.ylabel("Átlagos hossz (perc)")
plt.grid(True)

plt.show()

movies = df[df['type'] == 'Movie'].copy()

movies['duration_num'] = (
    movies['duration']
    .str.extract('(\d+)')
    .astype(float)
)

sns.scatterplot(
    data=movies,
    x='release_year',
    y='duration_num'
)

plt.title("Filmhossz és megjelenési év kapcsolata")
plt.show()

