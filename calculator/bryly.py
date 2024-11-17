import math
PI = math.pi

def pc_szescianu(a):
    return 6*a**2

def pc_prostopadloscianu(a,b,c):
    return 2*a*b + 2*a*c + 2*b*c

def pc_graniastoslupa(Pp,Pb):
    return 2*Pp + Pb

def pc_ostroslupa(Pp,Pb):
    return Pp + Pb

def pc_walca(r,h):
    return 2*(math.pi)*r*r+2*(math.pi)*r*h

def pc_stozka(r,l,h):
    return (math.pi)*r*r+(math.pi)*r*l 

def pc_kuli(r):
    return 4*(math.pi)*r*r

def v_szescianu(a):
    return a**3

def v_porostobloscian(a,b,c):
    return a*b*c

def v_graniastoslupa(Pp,h):
    return Pp*h

def v_osrtroslupa(Pp,h):
    return 0,33*Pp*h

def v_walca(r,h):
    return (math.pi)*r*r*h

def v_stozka(r,h):
    return 0,33*(math.pi)*r*r*h

def v_koli(r):
    return 4/3*PI* r**3

