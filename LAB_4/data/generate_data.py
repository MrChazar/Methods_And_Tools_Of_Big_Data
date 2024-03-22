import random
import pandas as pd
from datetime import datetime, timedelta

def generate_data(N):
    # Definiowanie listy, która będzie przechowywać dane
    data = []
    # Generowanie N losowych wierszy danych
    for _ in range(N):
        # stwórz wektor dat w formacie rok-miesiąc-dzień żeby był datetime w pd
        time = datetime.now() + timedelta(days=_)
        temperature = random.randint(-30, 40)
        data.append([time, temperature])
    # Tworzenie obiektu DataFrame z listy danych
    df = pd.DataFrame(data, columns=['time', 'temperature'])
    # Zapisanie danych do pliku CSV
    df.to_csv('weather_data.csv', index=False)
generate_data(100**2)
