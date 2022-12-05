class Biblioteka:

    def __init__(self):
        self.lista_egzemplarzy = []
        self.lista_wystapien = []

    def dodaj_egzemplarz(self, tytul, autor):
        ksiazka = Ksiazka(tytul, autor)
        self.lista_egzemplarzy.append(ksiazka)

    def zlicz_wystapienia(self):
        for element in self.lista_egzemplarzy:
            ile = str(self.lista_egzemplarzy).count(str(element))
            wystapienia = str(element,)
            self.lista_wystapien.append(f"{wystapienia}{ile})")
        final_list = sorted(list(set(self.lista_wystapien)))
        for element in final_list:
            print(element)

class Ksiazka:

    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    def __repr__(self):
        return f"('{self.tytul.strip()}', '{self.autor.strip()}', "

# logic
MojaBiblioteka = Biblioteka()
lista_input = []

n = int(input())
for i in range(n):
    x = eval(input())
    lista_input.append(x)
for element in lista_input:
    x = eval(str(element))
    tytul = element[0]
    autor = element[1]
    MojaBiblioteka.dodaj_egzemplarz(tytul, autor)
MojaBiblioteka.zlicz_wystapienia()



