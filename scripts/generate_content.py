import pandas as pd
import random

# Predefined list of genres and titles
genres = ['Action', 'Comedy', 'Drama', 'Romance', 'Sci-Fi', 'Thriller', 'Fantasy', 'Horror']
titles = [
    'Lost in Time', 'The Final Code', 'Heartlines', 'Beyond Reality', 'Laugh Riot',
    'Ghost Circuit', 'Parallel Minds', 'Broken Signals', 'Neon Dreams', 'Crimson Sky'
]

content = []

for content_id in range(101, 151):  # 50 items
    title = random.choice(titles) + f" {random.randint(1, 10)}"
    genre = random.choice(genres)
    release_year = random.randint(2010, 2023)

    content.append({
        'content_id': content_id,
        'title': title,
        'genre': genre,
        'release_year': release_year
    })

df = pd.DataFrame(content)
df.to_csv('data/content.csv', index=False)

print("✅ content.csv generated with 50 fake shows/movies")
