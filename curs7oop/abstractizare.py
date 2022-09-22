import math
from abc import ABC

"""
Clasele Abstracte trebuie sa mosteneasca o clasa speciala numita ABC
iar metodele lor trebuie sa aiba o singura linie, care ridica o exceptie numita NotImplementedError
"""
class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return self.raza ** 2 * 3.14

    def perimetru(self):
        return self.raza * 3.14


class Dreptunghi(FormaGeometrica):

    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def diagonala(self):
        return math.sqrt(self.lungime**2 + self.latime**2)


class Triunghi(FormaGeometrica):

    def __init__(self, lat1, lat2, lat3):
        self.l1 = lat1
        self.l2 = lat2
        self.l3 = lat3

    def aria(self):
        return self.l1 * self.l2 * self.l3

    def perimetru(self):
        return self.l1 + self.l2 + self.l3

    def inaltimea(self):
        return self.l1 * self.l2 / self.l3

# Pot crea FormaGeometrica, dar nu are sens (si nu ar trebui sa fac asta oricum)
forma = FormaGeometrica()
# print(forma.aria())  # va da eroare
# print(forma.perimetru())  # va da eroare

lista_forme_geometrice = [
    Cerc(12),
    Triunghi(3, 4, 5),
    Dreptunghi(12, 14),
    Cerc(7),
    Dreptunghi(5, 9),
    Dreptunghi(6, 6)
]

for fg in lista_forme_geometrice:
    print(f"Aria {fg.aria()} si perimetrul {fg.perimetru()}")

"""
Folosim mostenire atunci cand avem atribute si metode comune pe care vrem sa le tinem in clasa parinte.
Folosim abstractizare atunci cand vrem ca mai multe clase copil sa implementeze aceleasi metode,
dar fiecare are o implementare diferita.

La mostenire nu avem nici un fel de "obligatii" fata de clasa parinte.
La abstractizare, suntem obligati sa implementam metodele respective in toate clasele copil.
"""

"""
Zicem ca metodele aria si perimetru sunt POLIMORFICE
Adica ele fac chestii diferite, desi arata la fel (adica se apeleaza cu acelasi nume)
"""