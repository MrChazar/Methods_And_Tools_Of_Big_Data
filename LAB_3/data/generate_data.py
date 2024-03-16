import pandas as pd
import random
import numpy as np

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
#generate_data(100**2)

def calculate_energy_consumption(temperature):
    if temperature <= 0:
        return 1000 * (abs(temperature) + 1)  # Dla temperatur <= 0, większe wartości temperatury powodują większe zużycie energii
    else:
        return 1000 / (temperature + 1)  # Dla temperatur > 0, mniejsze wartości temperatury powodują większe zużycie energii


def generate_energy_consumption():
    # otwarcie pliku do dodania
    df = pd.read_csv('temperatures.csv')

    # dodanie nowej kolumny na podstawie kolumny temperature która będzie tworzona w taki sposób że im mniejsza temperatura tym większe zużycie energii
    df['energy_consumption'] = df['temperature'].apply(calculate_energy_consumption)

    # Dane do modelu
    # stwórz df['time_n'] który będzie zawierał tylko rok miesiąc i dzień  z df['time'] pozbądź się godzin i minut
    df['time_n'] = pd.to_datetime(df['time']).dt.date

    # usuń powtarzające się dane
    df = df.drop_duplicates(subset='time_n', keep='first')

    # zapisz tylko time_n, energy_consumption i temperature do pliku
    df[['time_n', 'temperature', 'energy_consumption']].to_csv('temperature_and_energy_consumption.csv', index=False)




generate_energy_consumption()
