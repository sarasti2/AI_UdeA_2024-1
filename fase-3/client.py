import requests
import pandas as pd

### Verify if the server is running
endpoint = 'http://127.0.0.1:5000/'
response = requests.post(endpoint)


### Hacer el pedido de predicción de un solo registro
endpoint = 'http://127.0.0.1:5000/predict'
csv_file = 'fase-3/modelo/test.csv'

# Read the CSV file and drop the specified columns
df = pd.read_csv(csv_file).drop(['outcome', 'Unnamed: 0'], axis=1)

# Take only the first row
df_single = df.head(1)

# Convert DataFrame to standard Python types
df_single = df_single.astype(object).where(pd.notnull(df_single), None)

# Convert DataFrame to dictionary format
data = df_single.to_dict(orient='records')

# Send POST request with JSON payload
response = requests.post(endpoint, json=data)
print(response.json())

### Hacer el pedido de predicción de varios registros y guardar el resultado en un archivo CSV
endpoint = 'http://127.0.0.1:5000/predict'
df = df.astype(object).where(pd.notnull(df), None)
data = df.to_dict(orient='records')
response = requests.post(endpoint, json=data)
df['prediction'] = response.json()
df.to_csv('fase-3/modelo/predictions.csv', index=False)
print('Predictions saved to fase-3/modelo/predictions.csv')

