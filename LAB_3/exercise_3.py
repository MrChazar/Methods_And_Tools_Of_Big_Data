import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

"""

Przy użyciu danych dotyczących temperatury i zużycia energii, zaimplementuj regresję
grzbietową w Pythonie. Stwórz modele regresji grzbietowej i Lasso przy użyciu biblioteki
scikit-learn. Dobierz odpowiednie wartości parametrów regularyzacji (alpha). Porównaj
wyniki regresji z różnymi parametrami regularyzacji. Porównaj wyniki regresji z regresją
liniową i zidentyfikuj, która metoda daje najlepsze wyniki.

"""


