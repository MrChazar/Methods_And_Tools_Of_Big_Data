
"""
Przygotuj program wyświetlający liczby parzyste w zakresie od 1 do 30. Wykorzystaj pętlę for i instrukcję continue.
"""

def zad_1():
    for i in range(1, 31):
        if i % 2 != 0:
            continue
        print(i)

"""
Napisz program, który za pomocą instrukcji while zsumuje liczby całkowite w zakresie od 1 do x.
"""

def zad_2(x):
    suma = 0
    i = 1
    while i <= x:
        suma += i
        i += 1
    return suma

"""
Przygotuj funkcje parzyste, która za pomocą instrukcji for zsumuje liczby parzyste w zakresie od 0
do x. Należy skorzystać z operatora modulo %.
"""
def zad_3(x):
    suma = 0
    for i in range(x+1):
        if i % 2 == 0:
            suma += i
    return suma

"""
Przygotuj program, wyświetlający w liczby z zakresu -100 do 100 w porządku malejącym. Liczby
powinny być podzielne przez 2, ale niepodzielne przez 3 i 8. Zadanie wykonaj przy wykorzystaniu
instrukcji continue.
"""

def zad_4():
    for i in range(100, -101, -1):
        if i % 2 != 0 and i % 3 != 0 and i % 8 != 0:
            continue
        print(i)

"""
Proszę napisać algorytm, który wypełni tzw. „jodełką” tablicę kwadratową oraz wyświetli n wierszy i kolumn. Przykład: dla n równego 5, tablica ta jest postaci:
1 1 1 1 1
1 2 2 2 2
1 2 3 3 3
1 2 3 4 4
1 2 3 4 5
"""

def zad_5(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(j+1, end=" ")
            else:
                print(i+1, end=" ")
        print()

"""
Napisz funkcję w języku Python, która będzie dokonywać dodania elementów do listy zagnieżdżonej co n elementów. Przykładowo dla n=4
dane na wejściu: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P']
rezultat na wyjściu: [['A', 'E', 'I', 'M'], ['B', 'F', 'J', 'N'], ['C', 'G', 'K', 'O'], ['D', 'H', 'L', 'P']]
"""

def zad_6(lista, n):
    result = []
    for i in range(n):
        result.append(lista[i::n])
    print(result)
    return result

"""
Utworzyć program, który będzie zastępował ostatni element listy elementami z innej podanej listy.
Przykładowo.
dane na wejściu: [100, 90, 80, 70, 60, 50], [49, 39, 29, 19]
rezultat na wyjściu: [100, 90, 80, 70, 60, 49, 39, 29, 19]
"""

def zad_7(lista1, lista2):
    lista1[-1:] = lista2
    print(lista1)
    return lista1

"""
Stwórz funkcję, która do każdego z listy elementów będzie dodawać łańcuch znakowy podany
przez użytkownika. Przykładowo.
dane na wejściu: ['A', 'B', 'C', 'D'] , string: 'Exit'
rezultat na wyjściu: [Exit A, Exit B, Exit C, Exit D]
"""

def zad_8(lista, string):
    result = [string + " " + i for i in lista]
    print(result)
    return result

"""
Stwórz program do zamiany ostatniej wartości z listy krotek na 0.
Przykładowe dane na wejściu: list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
Wyniki na wyjściu: [(1, 2, 0), (4, 5, 0), (7, 8, 0)]
"""

def zad_9(lista):
    result = [i[:-1] + (0,) for i in lista]
    print(result)
    return result

"""
 Usuń puste krotki z listy krotek.
Przykładowe dane na wejściu: [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]
Wyniki na wyjściu: [('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), 'i4']
"""

def zad_10(lista):
    result = [i for i in lista if i]
    print(result)
    return result

"""
Napisz i uruchom funkcję do wykonania iloczynu na wartościach słownika typu liczb rzeczywistych.
dane na wejściu: { 'f1': 4.8, 'f2': 2.4, 'f3': 1.2, 'f4': 0.6}
wynik na wyjściu: 8.2944
"""

def zad_11(slownik):
    result = 1
    for i in slownik.values():
        result *= i
    print(result)
    return result

"""
Stwórz słownik, w którym klucz jest wartością od 1 do n. Natomiast wartości są wynikiem podniesienia do czwartej potęgi liczby z klucza. Przykładowo dla n=6:
wynik na wyjściu: {1: 1, 2: 16, 3: 81, 4: 256, 5: 625, 6: 1296}
"""

def zad_12(n):
    result = {i: i**4 for i in range(1, n+1)}
    print(result)
    return result

"""
Napisz funkcję w języku Python do wypisania wszystkich unikalnych wartości ze słownika.
dane na wejściu: [1: 'A201', 2: 'B218', 3:'H018', 4:'B218', 5:'H018', 6: 'G123', 7: 'A007', 8: 'G230']
rezultat na wyjściu: {'A201', 'A007', 'B218', 'G123', ' G230', 'H018'}
"""

def zad_13(slownik):
    result = set(slownik.values())
    print(result)
    return result

