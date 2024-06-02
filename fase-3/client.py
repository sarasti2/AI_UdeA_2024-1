import requests
import pandas as pd

endpoint = 'http://127.0.0.1:5000/predict'
csv_file = 'fase-3/modelo/test.csv'

# Read the CSV file and drop the specified columns
df = pd.read_csv(csv_file).drop(['outcome', 'Unnamed: 0'], axis=1)

# Take only the first row
df = df

# Convert DataFrame to standard Python types
df = df.astype(object).where(pd.notnull(df), None)

# Convert DataFrame to dictionary format
data = df.to_dict(orient='records')

# Send POST request with JSON payload
response = requests.post(endpoint, json=data)
print(response.json())