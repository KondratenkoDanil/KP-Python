import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

def parse_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    data = pd.read_html(str(table))[0]
    return data

def analyze_data(data):
    cleaned_data = data.dropna()
    return cleaned_data

def transform_data(data):
    return data

def group_and_compute_statistics(data):
    grouped_data = data.groupby('group_column')
    statistics = grouped_data.agg({'numeric_column': ['mean', 'median', 'std']})
    return statistics

def visualize_data(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['numeric_column'], bins=20, kde=True)
    plt.title('Гістограма числового стовпця')
    plt.xlabel('Цінності')
    plt.ylabel('Частота')
    plt.show()

def main():
    url = "https://m.imdb.com/chart/top/"
    data = parse_data(url)
if data is not None:
    print("Перші 5 рядків даних:")
    print(data.head())
    cleaned_data = analyze_data(data)
    transformed_data = transform_data(cleaned_data)
    grouped_statistics = group_and_compute_statistics(transformed_data)
    print("\nСтатистичні показники після групування:")
    print(grouped_statistics)
    visualize_data(transformed_data)

if __name__ == "__main__":
    main()