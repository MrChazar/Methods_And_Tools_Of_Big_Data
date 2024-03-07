import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Zadanie 2: tworzenie macierzy i podstawowe operacje
 - Utwórz tablicę NumPy z wartościami od 1 do 10.
 - Znajdź maksymalne i minimalne wartości w tablicy.
 - Oblicz średnią i odchylenie standardowe tablicy.
"""

def zad_2():
    arr = np.arange(1, 11)
    print(f'Max: {arr.max()} i Min {arr.min()}')
    print(f'Średnia: {arr.mean()} i Odchylenie standardowe: {arr.std()}')

"""
Zadanie 3: Indeksowanie i krojenie tablicy
 - Utwórz tablicę 2D NumPy o kształcie (3, 4).
 - Uzyskaj dostęp do elementu o indeksie wiersza 1 i indeksie kolumny 2.
 - Pokrój tablicę, aby wyodrębnić podtablicę składającą się z pierwszych 2 wierszy i 2
ostatnich kolumn
"""
def zad_3():
    arr = np.arange(12).reshape(3, 4)
    print(arr)
    print(arr[1, 2])
    print(arr[:2, -2:])

"""
Zadanie4: Przekształcanie i transponowanie tablic
 - Utwórz tablicę 1D NumPy z 10 elementami.
 - Zmień kształt tablicy na tablicę 2D z kształtem (2, 5).
 - Transponuj tablicę i wydrukuj wynikowy kształt
"""
def zad_4():
    arr = np.arange(10)
    arr = arr.reshape(2, 5)
    print(arr)
    print(arr.T)

"""
Zadanie: Operacje arytmetyczne na tablicach
 - Utwórz dwie tablice NumPy o tym samym kształcie.
 - Dodaj dwie tablice po elementach.
 - Pomnóż jedną z tablic przez wartość skalarną.
"""
def zad_5():
    arr1 = np.arange(10).reshape(2, 5)
    arr2 = np.arange(10).reshape(2, 5)
    print(f"wynik dodawania {arr1} i {arr2} to {arr1 + arr2})")
    print(f"Wynik mnożenia {arr1 * 2}")

"""
Zadanie6: Rozgłaszanie z tablicy
 - Utwórz tablicę NumPy kształtu (3, 3) reprezentującą siatkę współrzędnych.
 - Dodaj tablicę wartości 1D do każdego wiersza siatki.
 - Pomnóż każdą kolumnę siatki przez inną wartość skalarną.
"""
def zad_6():
    arr = np.arange(0, 9).reshape(3,3)
    arr_2 = np.arange(0, 3)
    print(f"arr {arr}")
    print(f"arr_2 {arr_2}")
    print(f"dodawanie {arr + arr_2}")

"""
Zadanie7: Agregacja tablic i statystyki
 - Wygeneruj losową tablicę NumPy kształtu (100,).
 - Znajdź sumę, średnią i odchylenie standardowe tablicy.
 - Oblicz skumulowaną sumę i skumulowany iloczyn tablicy.
"""
def zad_7():
    arr = np.random.rand(100)
    print(f"Suma: {arr.sum()}, Średnia: {arr.mean()}, Odchylenie standardowe: {arr.std()}")
    print(f"Skumulowana suma: {arr.cumsum()}")

"""
Zadanie: Sortowanie i wyszukiwanie tablic
 - Utwórz tablicę NumPy losowych liczb całkowitych.
 - Posortuj tablicę w porządku rosnącym.
 - Wyszukaj określoną wartość w tablicy za pomocą wyszukiwania binarnego.
"""
def zad_8():
    arr = np.random.rand(100)
    print(f"wygenerowana tablica: {arr}")
    arr = np.sort(arr)
    print(f"posortowana tablica: {arr}")
    print(f"wyszukana: {np.searchsorted(arr, 0.5)}")

"""
Załaduj i sprawdź dane
- Załaduj plik CSV do Pandas DataFrame.
- Sprawdź wymiary (wiersze i kolumny) DataFrame.
- Wypisz kilka pierwszych wierszy, aby sprawdzić dane
"""
def zad_9():
    frame = pd.read_csv('files/countries.csv')
    print(f"ramka: {frame}")
    print(f" kształt: {frame.shape}")

"""
Wybór i filtrowanie danych
- Wybierz określone kolumny z DataFrame.
- Filtruj DataFrame na podstawie określonego warunku.
- Wybierz wiersze na podstawie określonego kryterium.
"""

def zad_10():
    frame = pd.read_csv('files/countries.csv')
    print(frame[['Kraj', 'Rok']])
    print(frame[frame['Populacja'] > 1000000])
    print(frame[frame['Kraj'] == 'Nigeria'])

"""
Oczyszczanie i wstępne przetwarzanie danych
- Obsługa brakujących wartości w DataFrame.
- Usuń duplikaty z DataFrame.
- W razie potrzeby konwertuj typy danych kolumn.
"""

def zad_11():
    frame = pd.read_csv('files/countries.csv')
    print(frame.dropna())
    print(frame.drop_duplicates())
    print(frame.dtypes)

"""
Agregacja i grupowanie danych
- Grupuj dane według określonej kolumny i wykonuj agregacje (np. suma, średnia, liczba).
- Oblicz statystyki podsumowujące dla kolumn liczbowych.
- Jednoczesne stosowanie wielu agregacji w różnych kolumnach
"""

def zad_12():
    frame = pd.read_csv('files/countries.csv')
    print(f"group by {frame.groupby('Kraj').sum()}")
    print(f"statystyki {frame.describe()}")
    print(f"agregacje {frame.groupby('Kraj').agg({'Rok': 'sum', 'Populacja': 'mean'})}")

"""
Transformacja danych
- Utwórz nową kolumnę na podstawie istniejących kolumn (np. obliczonych przy użyciu formuły).
- Zastosuj funkcję do każdego elementu kolumny.
- Zastosuj manipulacje łańcuchami do kolumny (np. wyodrębnianie podłańcuchów, zmiana
wielkości liter).
"""

def zad_13():
    frame = pd.read_csv('files/countries.csv')
    frame['populacja_2'] = frame['Mężczyźni'] + frame['Kobiety']
    print(frame)
    print(frame['Kraj'].apply(lambda x: x.lower()))
    print(frame['Kraj'].str.upper())

"""
Wizualizacja danych za pomocą Pandas
- Utwórz podstawowe wykresy (np. wykres liniowy, wykres słupkowy) za pomocą wbudowanych funkcji wizualizacji Pandas.
- Dostosuj wygląd wykresów, dodając etykiety, tytuły i legendy.
- Eksploruj relacje między zmiennymi za pomocą wizualizacji.
"""

def zad_14():
    frame = pd.read_csv('files/countries.csv')
    frame['Populacja'].plot()
    plt.title('Populacja liniowy')
    plt.show()
    frame['Populacja'].plot(kind='bar')
    plt.title('Populacja słupkowy')
    plt.show()

"""
Zaawansowana manipulacja danymi za pomocą Pandas
- Wykonuj zaawansowane scalanie i łączenie wielu ramek DataFrame.
- Przestawiaj i przekształcaj dane za pomocą funkcji stapiania i obracania.
- Obsługuj dane szeregów czasowych za pomocą funkcji DateTime Pandas.
"""

def zad_15():
    frame = pd.read_csv('files/countries.csv')
    frame2 = pd.read_csv('files/health.csv')
    print(pd.merge(frame, frame2, on='Kraj'))
    print(frame.pivot(index='Kraj', columns='Rok', values='Populacja'))
    print(pd.to_datetime(frame['Rok']))

"""
Utwórz wykres liniowy
- Wygeneruj dwie tablice danych (np. x i y) za pomocą NumPy.
- Wykreśl wykres liniowy za pomocą Matplotlib do wizualizacji danych.
- Dostosuj wykres, dodając etykiety do osi x i y, tytuł i legendę.
"""

def zad_16():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Wykres sin(x)')
    plt.show()

"""
Utwórz wykres punktowy
- Wygeneruj dwie tablice losowych danych (np. x i y) za pomocą NumPy.
- Utwórz wykres punktowy za pomocą Matplotlib do wizualizacji punktów danych.
- Dostosuj wykres, dodając etykiety do osi x i y, tytuł i zmieniając kolory znaczników.
"""

def zad_17():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres punktowy')
    plt.show()

"""
Utwórz wykres słupkowy
- Utwórz listę kategorii i odpowiadających im wartości.
- Narysuj wykres słupkowy za pomocą Matplotlib, aby przedstawić wartości dla każdej kategorii.
- Dostosuj wykres, dodając etykiety do osi x i y, tytuł i zmieniając kolory pasków.
"""

def zad_18():
    kat = {'A': 1, 'B': 2, 'C': 3}
    plt.bar(kat.keys(), kat.values())
    plt.xlabel('Kategoria')
    plt.ylabel('Wartość')
    plt.title('Wykres')
    plt.show()

"""
Narysuj Histogram
- Wygeneruj losowy zestaw danych za pomocą NumPy.
- Utwórz histogram za pomocą Matplotlib, aby zwizualizować rozkład danych.
- Dostosuj wykres, dodając etykiety do osi x i y, tytuł i zmieniając liczbę pojemników.
"""

def zad_19():
    x = np.random.rand(100)
    plt.hist(x, bins=10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Histogram')
    plt.show()

"""
Utwórz wykres kołowy
- Utwórz listę etykiet i odpowiadających im wartości reprezentujących kategoryczny zestaw danych.
- Wykreśl wykres kołowy za pomocą Matplotlib, aby zwizualizować proporcje każdej kategorii.
- Dostosuj fabułę, dodając tytuł i zmieniając kolory kawałków ciasta.
"""

def zad_20():
    labels = ['A', 'B', 'C']
    sizes = [1, 2, 3]
    plt.pie(sizes, labels=labels)
    plt.title('Wykres kołowy')
    plt.show()

"""
Wykres wątków pobocznych (funkcja subplots)
- Generuj wiele zestawów danych za pomocą NumPy.
- Twórz wykres wątków pobocznych za pomocą Matplotlib, aby wyświetlać wiele działek
w siatce.
- Wykreśl różne typy wykresów (np. wykresy liniowe, wykresy punktowe) na każdym polu.
"""

def zad_21():
    fig, ax = plt.subplots(2, 2)
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    ax[0, 0].plot(x, y)
    ax[0, 1].scatter(x, y)
    ax[1, 0].bar([1, 2, 3], [4, 5, 6])
    ax[1, 1].pie([1, 2, 3])
    plt.show()

"""
Zaawansowana personalizacja
- Załaduj zestaw danych (np. plik CSV) za pomocą biblioteki takiej jak Pandas.
- Analizuj dane i wybierz odpowiednie kolumny do wykreślenia.
- Utwórz zaawansowaną wizualizację za pomocą Matplotlib, taką jak skumulowany wykres
słupkowy, wykres 3D lub wykres pudełkowy.
- Szeroko dostosuj fabułę, dostosowując kolory, dodając adnotacje i dopracowując estetykę.
"""

def zad_22():
    frame = pd.read_csv('files/countries.csv')
    frame_wie = frame[['Kraj', 'Wiek średni']]
    frame_okr = frame[['Kraj', 'Populacja']]

    fig, ax = plt.subplots(2)
    ax[0].plot(frame_okr['Kraj'], frame_okr['Populacja'])
    ax[0].set_xlabel('Kraj')
    ax[0].set_ylabel('Populacja')
    ax[0].set_title('Populacja w krajach')

    ax[1].bar(frame_wie['Kraj'], frame_wie['Wiek średni'])
    ax[1].set_xlabel('Kraj')
    ax[1].set_ylabel('Wiek')
    ax[1].set_title('Wiek w krajach')

    # stwórz odstęp między wykresami
    plt.tight_layout()
    plt.show()

