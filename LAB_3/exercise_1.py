import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

"""
Zadanie 3:
Napisz program w Pythonie, który wykorzystuje regresję liniową z scikit-learn do przewidywania cen mieszkań na podstawie danych o ich cechach (np. liczba pokoi, powierzchnia,
piętro, lokalizacja). Dopasuj model do danych treningowych. Ocena modelu na zbiorze testowym za pomocą metryk takich jak średni błąd kwadratowy (MSE) lub współczynnik determinacji (R2
). Zwizualizuj wyniki regresji na wykresie, porównując przewidywane wartości z rzeczywistymi.
"""

# Wczytanie danych z pliku CSV
df = pd.read_csv('data/appartments.csv')

# Sprawdzenie wymiarów DataFrame
print(f" wymiary {df.head()}")

# Typy danych
print(f" typy danych: {df.dtypes}")

# Dane do modelu
X = df[['area', 'rooms', 'floor', 'year_of_construction']]
y = df['price']

# Tworzenie modelu
model = LinearRegression()

# stwórz x_test z wymiarami takimi jak X które są w zbiorze treningowym
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dopasowanie modelu do danych treningowych
model.fit(X_train, y_train)

# Aby zobaczyć dlaczego jest tak nietypowa zależność między powierzchnią a ceną możemy sprawdzić jego korelację z ceną która jest widocznie negatywna
print(model.coef_)

# Ocena modelu na zbiorze testowym
print(f"R2: {model.score(X_test, y_test)}")

# Przewidywanie cen mieszkań
y_pred = model.predict(X_test)

# Wizualizacja wyników po area, rooms i price
print(y_test.shape)


# wykresy
fig, ax = plt.subplots(2)
a_test = X_test['area'].values

# Znormalizuj a_test oraz y_pred i y_test
a_test = (a_test - a_test.mean()) / a_test.std()
y_pred = (y_pred - y_pred.mean()) / y_pred.std()
y_test = (y_test - y_test.mean()) / y_test.std()

ax[0].scatter(a_test, y_pred)
ax[0].set_title("Wykres zależności między Area a predykowaną Price")

ax[1].scatter(a_test, y_test)
ax[1].set_title("Wykres zależności między Area a rzeczywistymi Price")

plt.tight_layout()
plt.show()

