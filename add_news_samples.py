import pandas as pd

# Load existing CSVs
fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

# New fake news sample
new_fake = pd.DataFrame([{
    'title': 'Alien Attack in Delhi',
    'text': 'Aliens attacked Delhi last night and took away cows.',
    'subject': 'news',
    'date': '2025-07-07'
}])

# New real news sample
new_real = pd.DataFrame([{
    'title': 'Chandrayaan-4 Launch Success',
    'text': 'India has successfully launched Chandrayaan-4 to the moon orbit.',
    'subject': 'news',
    'date': '2025-07-07'
}])

# Append new data to the existing ones
fake = pd.concat([fake, new_fake], ignore_index=True)
real = pd.concat([real, new_real], ignore_index=True)

# Save the updated CSVs
fake.to_csv("Fake.csv", index=False)
real.to_csv("True.csv", index=False)

print("✅ News samples added successfully.")
