import pandas as pd
from faker import Faker

fake = Faker()
users = []

for user_id in range(1, 101):  # 100 users
    name = fake.name()
    email = fake.email()
    signup_date = fake.date_between(start_date='-2y', end_date='today')
    users.append({
        'user_id': user_id,
        'name': name,
        'email': email,
        'signup_date': signup_date
    })

df = pd.DataFrame(users)
df.to_csv('data/users.csv', index=False)

print("✅ users.csv generated with 100 fake users")
