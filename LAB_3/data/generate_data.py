import pandas as pd
import random

def generate_data(N):
    # Definiowanie listy, która będzie przechowywać dane
    data = []
    # Generowanie N losowych wierszy danych
    for _ in range(N):
        area = random.randint(50, 120)
        rooms =  random.randint(1, 5)
        floor = random.randint(1, 10)
        year_of_construction = random.randint(1950, 2022)
        price = random.randint(150000, 1000000)
        data.append([area, rooms, floor, year_of_construction, price])
    # Tworzenie obiektu DataFrame z listy danych
    df = pd.DataFrame(data, columns=['area', 'rooms', 'floor',
    'year_of_construction', 'price'])
    # Zapisanie danych do pliku CSV
    df.to_csv('appartments.csv', index=False)
generate_data(100**2)