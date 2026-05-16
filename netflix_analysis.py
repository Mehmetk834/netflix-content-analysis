import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df = df.drop(columns=['description', 'cast', 'director'], errors='ignore')

# Content Type Distribution

type_counts = df['type'].value_counts()
print(type_counts)
type_counts.plot(kind='bar')
plt.title("Netflix Content Types")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=20)
for i, v in enumerate(type_counts):
    plt.text(i, v + 50, str(v), ha='center')

plt.show()
type_counts.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Distribution of Content Types") 
plt.show()


print(df['country'].value_counts().head(10))
print(df['release_year'].value_counts().sort_index())

# us analysis
us_data = df[df['country'].str.contains('United States', na=False)]
print(us_data['type'].value_counts())


us_type_counts = us_data['type'].value_counts()

us_type_counts.plot(kind='bar')
plt.title("US Content Types")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=30)

for i, v in enumerate(us_type_counts):
    plt.text(i, v + 50, str(v), ha='center')

plt.show()

# movie categories

movies = df[df['type'] == 'Movie']
movie_categories = movies['listed_in'].str.split(',').explode().str.strip()
print(movie_categories.value_counts().head(10))

top_categories=movie_categories.value_counts().head(10)[::-1]
plt.figure(figsize=(8,5))
top_categories.plot(kind='bar')
plt.title("Top Movie Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.gca().invert_xaxis()
for i,v in enumerate(top_categories):
    plt.text(i, v + 50, str(v), ha='center')
plt.tight_layout()
plt.show()

# country & type
country_type = df.groupby(['country', 'type']).size().unstack().fillna(0)
print(country_type.head(10))
country_type['total'] = country_type.sum(axis=1)
top_countries = country_type.sort_values('total', ascending=False).head(10)


top_countries[['Movie', 'TV Show']].plot(kind='bar', stacked=True)

plt.title("Movie vs TV Show by Country")
plt.xlabel("Country")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()