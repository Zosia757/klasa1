import random

class Jaa:
    def __init__(self, imie):
        self.imie = imie
        self.hp = 100
        self.atak = 10
        self.mana = 100
        self.zyje = True
        self.ile = 0
        self.ile_wykorzystano_potek_l = 0
        self.ile_wykorzystano_potek_m = 0

    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
        return self.zyje
    
    def damage(self, n):
        self.hp -= n
        self.czy_zyje()
        print(f"obrarzenia {n},pozostale hp {self.hp}, pozostala mana {self.mana}")

    def wypasiony_atak(self):
        return random.randint(10, 20) 
    
    def fireball_atak(self):
        if self.mana <= 10:
            print("wykorzystano cala mane nie da sie juz uzyc tego ataku")
            return False
        
        self.mana -= 10
        return random.randint(15,30)
    
    def potka_lecznicza(self):
        if self.ile_wykorzystano_potek_l == 4:
            return False
        
        if self.hp +15 >= 100:
            print("masz za duzo hp nie mozemy dolozyc wiecej")
            return False
        
        self.hp += 15
        self.ile_wykorzystano_potek_l += 1
        return True
    
    def potka_na_przyrost_many(self):
        if self.ile_wykorzystano_potek_m == 4:
            return False
        
        if self.mana +15 >= 100:
            print("masz za duzo many nie mozemy dolozyc wiecej")
            return False
        
        self.mana += 15
        self.ile_wykorzystano_potek_m += 1
        return True

    def atakuje(self):
        print(" basic atak - a | wypasiony atak - b | fireball atak - c ")
        inp = input("Jaki atak: ")

        if "a" == inp:
            return self.atak
        
        elif "b" == inp:
            return self.wypasiony_atak()
        
        elif "c" == inp:
            return self.fireball_atak()
        
        else:
            print('Bledny wybor ataku, uzyto podstawowy atak')
            return self.atak
    
    def uzupelnianie(self):
        print("potka lecznicza (l) lub na przyrost many (m)")
        inp = input("co uzupelnic:")
        if "l" == inp:
            return self.potka_lecznicza()
        elif "m" == inp:
            return self.potka_na_przyrost_many()
        

    def ile_zabito(self):
        return self.ile
    def podlicz_zabitych(self):
        self.ile += 1

class Goblin:
    def __init__(self):
        self.hp = 22
        self.atak = 5
        self.zyje = True
    
    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
        return self.zyje
    
    def damage(self, n):
        self.hp -= n
        self.czy_zyje()
        print(f"obrazenia {n},pozostale hp {self.hp}")

    def atakuje(self):
        return self.atak

class Mroczny_Elf:
    def __init__(self):
        self.hp = 63
        self.atak = 20
        self.zyje = True
        self.mana = 40

    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
        return self.zyje
    
    def damage(self,n):
        self.hp -= n 
        self.czy_zyje()
        print(f"obrazenia {n}, pozostale hp {self.hp}, pozostala mana {self.mana}")

    def atakuje(self):
        return self.atak


print("Start gry!!!")
imie = input("Podaj imie: ")

ja = Jaa(imie)

while ja.czy_zyje(): 
    if ja.ile_zabito() <= 10:
        przeciwnik = Goblin()
    else:
        przeciwnik = Mroczny_Elf()
        print("trafiles na wyzszy poziom teraz walczysz z trudniejszym przeciwnikiem")

    while ja.czy_zyje() and przeciwnik.czy_zyje():
        przeciwnik.damage(ja.atakuje())

        if przeciwnik.czy_zyje():
            ja.damage(przeciwnik.atakuje())

        if przeciwnik.czy_zyje() == False:
            ja.podlicz_zabitych()
            print("Zabilem przeciwnika!!!!")
            ja.uzupelnianie()


print("aAAAAAAaaaa.....")
print("Koniec gry")
print(f"zabiles {ja.ile_zabito()} przeciwnikow")

