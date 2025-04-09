class Silnik:
    def __init__(self, typ, pojemnosc):
        self.typ = typ
        self.pojemnosc = pojemnosc

    def uruchom(self):
        print(f"Silnik {self.typ} o pojemności {self.pojemnosc} uruchomiony!")


class Akumulator:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc

    def laduj(self):
        print(f"Ładowanie akumulatora o pojemności {self.pojemnosc} kWh.")


class Pojazd:
    def __init__(self, marka, model, rok_produkcji, kolor):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor

    def przedstaw_sie(self):
        print(f"To jest {self.marka} {self.model}, {self.rok_produkcji} r., kolor: {self.kolor}.")


class SamochodOsobowy:
    def __init__(self, marka, model, rok_produkcji, kolor, liczba_drzwi, typ_napędu, typ_silnika, pojemnosc_silnika):
        self.pojazd = Pojazd(marka, model, rok_produkcji, kolor)
        self.silnik = Silnik(typ_silnika, pojemnosc_silnika)
        self.liczba_drzwi = liczba_drzwi
        self.typ_napędu = typ_napędu

    def przedstaw_sie(self):
        self.pojazd.przedstaw_sie()
        print(f"Jest to samochód osobowy z {self.liczba_drzwi} drzwiami, napęd: {self.typ_napędu}.")
    
    def uruchom_silnik(self):
        self.silnik.uruchom()
        print("Pojazd jest gotowy do jazdy!")


class Motocykl:
    def __init__(self, marka, model, rok_produkcji, kolor, typ, typ_silnika, pojemnosc_silnika):
        self.pojazd = Pojazd(marka, model, rok_produkcji, kolor)
        self.silnik = Silnik(typ_silnika, pojemnosc_silnika)
        self.typ = typ

    def przedstaw_sie(self):
        self.pojazd.przedstaw_sie()
        print(f"To motocykl typu {self.typ}.")

    def uruchom_silnik(self):
        self.silnik.uruchom()
        print("Motocykl jest gotowy do jazdy!")


class PojazdElektryczny:
    def __init__(self, marka, model, rok_produkcji, kolor, zasięg_na_baterii, pojemnosc_akumulatora):
        self.pojazd = Pojazd(marka, model, rok_produkcji, kolor)
        self.akumulator = Akumulator(pojemnosc_akumulatora)
        self.zasięg_na_baterii = zasięg_na_baterii

    def przedstaw_sie(self):
        self.pojazd.przedstaw_sie()
        print(f"Jest to pojazd elektryczny z zasięgiem na baterii: {self.zasięg_na_baterii} km.")

    def uruchom_silnik(self):
        self.akumulator.laduj()
        print("Pojazd elektryczny jest gotowy do jazdy!")


class PojazdHybrydowy:
    def __init__(self, marka, model, rok_produkcji, kolor, zasięg_na_baterii, pojemnosc_akumulatora, typ_silnika, pojemnosc_silnika):
        self.pojazd = Pojazd(marka, model, rok_produkcji, kolor)
        self.pojazd_elektryczny = PojazdElektryczny(marka, model, rok_produkcji, kolor, zasięg_na_baterii, pojemnosc_akumulatora)
        self.silnik = Silnik(typ_silnika, pojemnosc_silnika)

    def przedstaw_sie(self):
        self.pojazd.przedstaw_sie()
        self.pojazd_elektryczny.przedstaw_sie()
        print(f"Jest to pojazd hybrydowy z napędem {self.silnik.typ} o pojemności {self.silnik.pojemnosc} litrów.")

    def uruchom_silnik(self):
        self.silnik.uruchom()
        print("Pojazd hybrydowy jest gotowy do jazdy!")


class TestPojazdów:
    def __init__(self):
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def uruchom_wszystkie_silniki(self):
        for pojazd in self.pojazdy:
            pojazd.uruchom_silnik()

    def przedstaw_wszystkie_pojazdy(self):
        for pojazd in self.pojazdy:
            pojazd.przedstaw_sie()


def main():
    samochod = SamochodOsobowy("Toyota", "Corolla", 2020, "czerwony", 4, "spalinowy", "benzynowy", 2.0)
    motocykl = Motocykl("Harley-Davidson", "Sportster", 2019, "czarny", "cruiser", "benzynowy", 1.2)
    elektryk = PojazdElektryczny("Tesla", "Model 3", 2023, "biały", 500, 75)
    hybryda = PojazdHybrydowy("Toyota", "Prius", 2022, "zielony", 400, 60, "hybrydowy", 1.8)

    tester = TestPojazdów()

    tester.dodaj_pojazd(samochod)
    tester.dodaj_pojazd(motocykl)
    tester.dodaj_pojazd(elektryk)
    tester.dodaj_pojazd(hybryda)

    tester.przedstaw_wszystkie_pojazdy()


    tester.uruchom_wszystkie_silniki()

if __name__ == "__main__":
    main()
