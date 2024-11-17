import math
print("kalkulator")
print("wyierz numer figury")
print("1-kwadrat                        9-sześcian")
print("2-prostokąt                      10-prosopadłościan")
print("3-równoległobok                  11-graniastosłup")
print("4-trapez                         12-ostrosłup")
print("5-trójkąt                        13-walec")
print("6-t. równoboczny                 14-stożek")
print("7-koło                           15-kula")
print("8-romb                           16-wys tr.równobocznego")
print("17-prz.kwadratu                  18-tw.pitagorasa")

wybor=input("wybór= ")
if wybor=="1":
    a=float(input("podaj dł.boku a= "))
    print("Obwód=",a*4, "Pole=",a*a)
elif wybor=="2":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    print("Obwód=",2*a+2*b, "Pole=",a*b)
elif wybor=="3":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    h=float(input("podaj dł.boku h= "))
    print("Obwód=",2*a+2*b, "Pole=",a*h)
elif wybor=="4":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    c=float(input("podaj dł.boku c= "))
    d=float(input("podaj dł.boku d= "))
    h=float(input("podaj dł.boku h= "))
    print("Obwód=",a+b+c+d, "Pole=",((a+b)*h)/2)
elif wybor=="5":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    c=float(input("podaj dł.boku c= "))
    h=float(input("podaj dł.boku h= "))
    print("Obwód=",a+b+c, "Pole=",0,5*c*h)
elif wybor=="6":
    a=float(input("podaj dł.boku a= "))
    print("Obwód=",3*a, "Pole=",(a*a*(math.sqrt(3)))/4)
elif wybor=="7":
    r=float(input("podaj dł.boku r= "))
    print("Obwód=",2*(math.pi)*r, "Pole=",(math.pi)*r*r)
elif wybor=="8":
    a=float(input("podaj dł.boku a= "))
    h=float(input("podaj dł.boku h= "))
    e=float(input("podaj dł.boku e= "))
    f=float(input("podaj dł.boku f= "))
    print("Obwód=",4*a, "Pole=",a*h,)
elif wybor=="9":#brly szescian
    a=float(input("podaj dł.boku a= "))
    print("P.całkowite=",6*a*a, "Objętość=",a*a*a)
elif wybor=="10":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    c=float(input("podaj dł.boku c= "))
    print("P.całkowite=",2*a*b+2*a*c+2*b*c, "Objętość=",a*b*c)
elif wybor=="11":
    pp=float(input("podaj dł.boku pp= "))
    pb=float(input("podaj dł.boku pb= "))
    h=float(input("podaj dł.boku h= "))
    print("P.całkowite=",2*pp+pb, "Objętość=",pp*h)
elif wybor=="12":
    pp=float(input("podaj dł.boku pp= "))
    pb=float(input("podaj dł.boku pb= "))
    h=float(input("podaj dł.boku h= "))
    print("P.całkowite=",pp+pb, "Objętość=",0,33*pp*h)
elif wybor=="13":
    r=float(input("podaj dł.boku r= "))
    h=float(input("podaj dł.boku h= "))
    print("P.całkowite=",2*(math.pi)*r*r+2*(math.pi)*r*h, "Objętość=",(math.pi)*r*r*h)
elif wybor=="14":
    r=float(input("podaj dł.boku r= "))
    l=float(input("podaj dł.boku l= "))
    h=float(input("podaj dł.boku h= "))
    print("P.całkowite=",(math.pi)*r*r+(math.pi)*r*l, "Objętość=",0,33*(math.pi)*r*r*h)
elif wybor=="15":
    r=float(input("podaj dł.boku r= "))
    print("P.całkowite=",4*(math.pi)*r*r, "Objętość=",1,33*(math.pi)*r*r*r)
elif wybor=="16":
    a=float(input("podaj dł.boku a= "))
    print("wysokość=",(a*(math.sqrt(3)))/2)
elif wybor=="17":
    a=float(input("podaj dł.boku a= "))
    print("przekątna=",(a*(math.sqrt(3))))
elif wybor=="18":
    a=float(input("podaj dł.boku a= "))
    b=float(input("podaj dł.boku b= "))
    print("c=",a*a+b*b)
else:
    print("nie ma takiej komendy")