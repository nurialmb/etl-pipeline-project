import pandas as pd
import random
from faker import Faker

fake = Faker()

watch_history = []

# Load existing users and content
users = pd.read_csv('data/users.csv')
content = pd.read_csv('data/content.csv')

user_ids = users['user_id'].tolist()
content_ids = content['content_id'].tolist()

# Generate 500 watch events
for watch_id in range(1001, 1501):
    user_id = random.choice(user_ids)
    content_id = random.choice(content_ids)
    watch_date = fake.date_between(start_date='-1y', end_date='today')
    duration_minutes = random.randint(5, 120)

    watch_history.append({
        'watch_id': watch_id,
        'user_id': user_id,
        'content_id': content_id,
        'watch_date': watch_date,
        'duration_minutes': duration_minutes
    })

df = pd.DataFrame(watch_history)
df.to_csv('data/watch_history.csv', index=False)

print("✅ watch_history.csv generated with 500 events")
