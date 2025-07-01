import pandas as pd
from sqlalchemy import create_engine

# Read CSVs
users = pd.read_csv('data/users.csv')
content = pd.read_csv('data/content.csv')
history = pd.read_csv('data/watch_history.csv')

users['signup_date'] = pd.to_datetime(users['signup_date'])
history['watch_date'] = pd.to_datetime(history['watch_date'])

merged = history.merge(users, on='user_id', how='left') \
                .merge(content, on='content_id', how='left')


engine = create_engine('sqlite:///data/streaming.db', echo=False)


users.to_sql(name='users', con=engine, if_exists='replace', index=False)
content.to_sql(name='content', con=engine, if_exists='replace', index=False)
history.to_sql(name='watch_history', con=engine, if_exists='replace', index=False)
merged.to_sql(name='watch_events', con=engine, if_exists='replace', index=False)

print("✅ All tables loaded into streaming.db successfully!")
