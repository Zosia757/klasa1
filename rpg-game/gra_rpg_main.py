import osilek_z_osiedla as o
import mondrala as m
import potwor as p
from random import randint


def spotkanie_potwora(bohater: list, potwor: list)->int:
    print('bohater',bohater.cechy)
    print('przeciwnik', potwor) 
    nie_wybrales_jeszcze = 0

    while True:
        atak = input("(W)alczysz, (U)ciekasz czy (P)odstęp \n")
        atak = atak.upper()
        if atak in ['W','P','U']:
            if atak == 'W':
                l = randint(25, 40)
                potwor[0] -= l
                bohater.cechy[0] -= l/2
            elif atak == 'P':
                l = randint(3,7)
                potwor[1] -= l
                bohater.cechy[1] -= l/2
            elif atak == 'U':
                l = randint(10,30)
                potwor[2] -= l
                if potwor[2] < 0:
                    print("Ucieczka zakończona sukcesem")
                else:
                    bohater.cechy[2] -= l

        if nie_wybrales_jeszcze == 0:
            print("potka lecznicza wybierz 1 jesli bierzesz lub 2 jesli nie chcesz jej uzyc ")
            wybor = input("wybor = ")
            if wybor == "1":
                potka_lecznicza(cechy_bohatera = bohater.cechy)
                print("uzyles potki lecniczej ")
                nie_wybrales_jeszcze = 1
        
        if smierc_bohatera(bohater.cechy):
            return 0
        
        print('bohater', bohater.cechy)
        print('potwor', potwor)

        if potwor[0] <= 0 or potwor[1] <= 0 or potwor[2] <= 0:
            print("Potwor pokonany")
            return 1
            

def losuj_potwora() -> list:
    losowa_liczba = randint(0,100)
    if losowa_liczba >= 75:
        gen_potwora = p.wygeneruj_super_potwora()
        print("spotkales super potwora")
    else:
        gen_potwora = p.wygeneruj_potwora()
        print("spotkales potwora")
    return gen_potwora


def smierc_bohatera(cechy_bohatera)-> bool:
    if cechy_bohatera[0] <= 0 or cechy_bohatera[1] <= 0 or cechy_bohatera[2] <= 0:
        return True
    else:
        return False


def potka_lecznicza(cechy_bohatera):
    cechy_bohatera [0] += 15 
    cechy_bohatera [1] += 15
    cechy_bohatera [2] += 15


print("wybierz bohatera")
print("1.osiłek 2.madrala")
wybor = input("wybór = ")


if wybor == "1":
    bohater = o
elif wybor == "2":
    bohater = m

liczba_zabitych_potworow = 0
for a in range(20):
    print(f"potyczka {a+1}")
    liczba_zabitych_potworow += spotkanie_potwora(bohater, losuj_potwora())
    if smierc_bohatera(bohater.cechy):
        print("zgineles, koniec gry")
        print("liczba pokonanych potworow", liczba_zabitych_potworow)
        break


