import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://www.numbeo.com/quality-of-life/rankings_by_country.jsp'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

def get_country_data(country_name):
    table = soup.find('table', id='t2')
    rows = table.tbody.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        country = cols[1].text.strip()
        if country.lower() == country_name.lower():
            data = {
                'Country': country,
                'Quality of Life Index': cols[2].text.strip().replace(',', ''),
                'Purchasing Power Index': cols[3].text.strip().replace(',', '').replace('+', ''),
                'Safety Index': cols[4].text.strip().replace(',', ''),
                'Health Care Index': cols[5].text.strip().replace(',', '').replace('+', ''),
                'Cost of Living Index': cols[6].text.strip().replace(',', ''),
                'Property Price to Income Ratio': cols[8].text.strip().replace(',', ''),
                'Traffic Commute Time Index': cols[9].text.strip().replace(',', ''),
                'Pollution Index': cols[10].text.strip().replace(',', '')
            }
            return data
    return None

countries = ['Luxembourg', 'Netherlands']
data = []

for country in countries:
    country_data = get_country_data(country)
    if country_data:
        data.append(country_data)

df = pd.DataFrame(data)
print("Parsed Data:")
print(df)

df['Quality of Life Index'] = pd.to_numeric(df['Quality of Life Index'], errors='coerce')
df['Purchasing Power Index'] = pd.to_numeric(df['Purchasing Power Index'], errors='coerce')
df['Safety Index'] = pd.to_numeric(df['Safety Index'], errors='coerce')
df['Health Care Index'] = pd.to_numeric(df['Health Care Index'], errors='coerce')
df['Cost of Living Index'] = pd.to_numeric(df['Cost of Living Index'], errors='coerce')
df['Property Price to Income Ratio'] = pd.to_numeric(df['Property Price to Income Ratio'], errors='coerce')
df['Traffic Commute Time Index'] = pd.to_numeric(df['Traffic Commute Time Index'], errors='coerce')
df['Pollution Index'] = pd.to_numeric(df['Pollution Index'], errors='coerce')

print("\nQuantitative Characteristics:")
print(df.describe())

print("\nTable Headers:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

df = df.fillna(0)

print("\nCleaned Data:")
print(df)

df_sorted = df.sort_values(by='Quality of Life Index', ascending=False)

print("\nCalculated Data:")
print(df_sorted)

#1 Quality of Life Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Quality of Life Index', data=df_sorted)
plt.title('Quality of Life Index')
plt.show()

#2 Purchasing Power Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Purchasing Power Index', data=df_sorted)
plt.title('Purchasing Power Index')
plt.show()

#3 Safety Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Safety Index', data=df_sorted)
plt.title('Safety Index')
plt.show()

#4 Health Care Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Health Care Index', data=df_sorted)
plt.title('Health Care Index')
plt.show()

#5 Cost of Living Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Cost of Living Index', data=df_sorted)
plt.title('Cost of Living Index')
plt.show()

#6 Property Price to Income Ratio
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Property Price to Income Ratio', data=df_sorted)
plt.title('Property Price to Income Ratio')
plt.show()

#7 Traffic Commute Time Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Traffic Commute Time Index', data=df_sorted)
plt.title('Traffic Commute Time Index')
plt.show()

#8 Pollution Index
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Pollution Index', data=df_sorted)
plt.title('Pollution Index')
plt.show()