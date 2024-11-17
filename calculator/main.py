import bryly as br
import figury_plaskie as fp

print("Program rozpoczal dzialanie ;)")

def menu():
    print("""1-kwadrat               9-sześcian")
    2-prostokąt                      10-prosopadłościan")
    3-równoległobok                  11-graniastosłup")
    4-trapez                         12-ostrosłup")
    5-trójkąt                        13-walec")
    6-t. równoboczny                 14-stożek")
    7-koło                           15-kula")
    8-romb                           16-wys tr.równobocznego
    17-prz.kwadratu                  18-tw.pitagorasa""")

menu()
while True:
    inp = input()
    if inp == "stop":
        print("Progam zkonczyl dzialanie")
        break
    elif inp == "1":
        a = float(input("a - "))
        print("Pole kwadratu", fp.p_kwadratu(a), "Obwód kwadratu", fp.l_kwadratu(a))
    elif inp == "2":
        a = float(input("a - "))
        b = float(input("b - "))
        print("pole postokata", fp.p_prostokata(a,b), "obwod prostokata", fp.l_prostokata(a,b))
    elif inp == "3":
        a = float(input("a - "))
        b = float(input("b - "))
        print("pole rownolegloboku", fp.p_rownolegloboku(a,b), "obwod rownolegloboku", fp.l_rownolegloboka(a,b))
    elif inp == "4":
        a = float(input("a - "))
        b = float(input("b - "))
        h = float(input("h - "))
        d = float(input("d - "))
        c = float(input("c - "))
        print("pole trapezu", fp.p_trapezu(a,b,h), "obwod trapezu ", fp.l_trapezu(a,b,c,d))
    elif inp == "5":
        a = float(input("a - "))
        b = float(input("b - "))
        c = float(input("c - "))
        h = float(input("h - "))
        print("pole trojkata", fp.p_trojkata(a,h), "obwod trojkata", fp.l_torjkata(a,b,c))
    elif inp =="6":
        a=float(input("a = "))
        print("pole tr rownobocznego", fp.p_tr_rowbocznego(a), "obwod tr rownobocznego", fp.l_tr_rownobocznego(a))
    elif inp =="7":
        r=float(input("r -  "))
        print("pole kola",fp.p_kola(r), "obwod kola", fp.l_kola(r))
    elif inp =="8":
        a=float(input("a - "))
        h=float(input("h = "))
        print("pole rombu", fp.p_rombu(a,h), "obwod kola", fp.l_rombu(a))
    elif inp=="9":#brly szescian
        a=float(input(" a= "))
        print("P.całkowite", br.pc_szescianu(a), "Objętość", br.v_szescianu(a))
    elif inp =="10":
        a=float(input("  a= "))
        b=float(input("  b= "))
        c=float(input("  c= "))
        print("P.całkowite", br.pc_prostopadloscianu(a,b,c), "Objętość", br.v_porostobloscian)
    elif inp=="11":
        Pp=float(input("  Pp= "))
        Pb=float(input("  Pb= "))
        h=float(input("  h= "))
        print("P.całkowite", br.pc_graniastoslupa(Pp,Pb), "Objętość", br.v_graniastoslupa(Pp,h))
    elif inp=="12":
        Pp=float(input("  pp= "))
        Pb=float(input("  pb= "))
        h=float(input("  h= "))
        print("P.całkowite", br.pc_ostroslupa(Pp,Pb), "Objętość", br.v_osrtroslupa(Pp,h))
    elif inp=="13":
        r=float(input("  r= "))
        h=float(input("  h= "))
        print("P,calkowite", br.pc_walca(r,h), "Objętość", br.v_walca(h,r))
    elif inp=="14":
        r=float(input("  r= "))
        l=float(input("  l= "))
        h=float(input("  h= "))
        print("P.całkowite", br.pc_stozka(r,l,h), "Objętość", br.v_stozka(r,h))
    elif inp=="15":
        r=float(input("  r= "))
        print("P.całkowite", br.pc_kuli(r), "Objętość", br.v_koli(r) )
    else:
        print(f"Nie ma takiej komendy: {inp}")
    print("\n\nWybierz kolejną figurę lub bryłę z menu.")
    menu()
