import random

'''
Instructiunea FOR
-> Instructiunea for este utilizata pentru a itera (parcurge) o secventa - o lista, sir caractere, dictionar, multime, interval numere etc

Sintaxa de baza:

for element in secventa:
    bloc de cod

element -> variabila care ia pe rand fiecare valoare din secventa
secventa -> orice obiect iterabil(sir, lista etc)
blocul de cod este indentat
'''

#Iterare printr-un sir
#for litera in 'itschool':
    #print(litera)

#Iterare printr-o lista
'''for litera in ['itschool', 'programare', 'python e cool']:
    print(litera)'''

'''Explicatie
itschool este un sir de caractere
bucla for ia fiecare caracter din acest sir, unul cate unul, si il atribuie variabilei litera, in cazul nostru(poti declara cu orice nume, mai putin cele rezervate)

iteratia 1 -> litera i 
iteratia 2 -> litera t
.
.
.
'''

#Functia range ->
'''for i in range(5):
    print(i)'''

#Variante
#range(5) -> 0 pana la 4
#range(-10, 10) -> de la 1 pana la 5
#range(1, 10, 2) -> 1, 3, 5, 7, 9 (pas/salt de 2)

#FOR cu ELSE -> Blocul else se executa daca bucla nu a fost intrerupta cu BREAK
'''for i in range(3):
    print(i)
else:
    print("Bucla s-a terminat normal")'''

#BREAK & CONTINUE
#break -> intrerupe bucla

'''for i in range(10):
    if i == 5:
        break
    print(i)'''

#continue -> sare peste restul iteratiei curente

'''for i in range(10):
    if i == 5:
        continue
    print(i)'''

#nested loop -> bucla for inlantuita

'''for i in range(3):
    for j in range(2):
        print(f"i = {i} si j = {j}")'''
# Explicatie detaliata
'''
range(3) -> genereaza 0, 1, 2 pentru i
pentru fiecare valoare a lui i, bucla interioara va parcurge valorile 0 si 1
print() -> va afisa toate combinatiile posibile dintre valorile lui i si j

Explicatie detaliata:
1.
i = 0
    j = o
         i = 0, j = 0
    j = 1
        i = 0, j = 1
        
2. 
i = 1
    j = 0
        i = 1, j = 0
    j = 1
        i = 1, j = 1

3. 
i = 2
    j = 0
        i = 2, j = 0
    j = 1
        i = 2, j = 1
'''

#Exemple de exercitii
# Afiseaza numerele pare de la 1 la 10

'''for i in range(1, 11):
    if i % 2 == 0:
        print(i)'''

#Calculeaza suma numerelor de la 1 la 100
'''suma = 0
for i in range(1, 101):
    suma += i
    print(suma)'''

'''*** WHILE LOOP ***'''

# WHILE -> este o structura de control care executa un bloc de cod, atata timp cat o conditie este adevarata

'''
while conditie:
    # secventa de cod executata daca conditia este True
'''

#Exemple
'''x = 0
while x < 5:
    print(x)
    x += 1'''

#De retinut -> Conditia trebuie sa se schimbe
# Daca nu modificam variabilele din conditie, putem crea o bucla infinita

'''while True:
    print("Ruleaza la nesfarsit")'''

#BREAK -> opreste bucla imediat ce conditia este satisfacuta
'''x = 0

while True:
    if x == 3:
        break
    print(x)
    x += 1'''

#CONTINUE -> sare peste restul codului si revine la conditie


'''x = 0

while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)'''

'''def test(a, b):
    return a + b

rezultat = test(5, 3)
print(rezultat)'''

#ELSE in WHILE -> Se executa doar daca bucla se incheie natura (fara break)

'''x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("s-a oprit ok")'''

#Cazuri utilizare

#Numarare

'''n = 10
while n > 0:
    print(n)
    n -= 1'''

#Asteapta conditie

'''conditie = ''

while conditie != 'exit':
    conditie = input("Scrie 'exit' pentru a iesi: ").lower()'''
#lower() -> face caracterele dintr-un string dat cu CAPS in litere mici

#Validare input
'''valoare = int(input("Introdu un numar pozitiv:"))
while valoare <= 0:
    valoare = int(input("Numar invalid. Reincearca"))'''

#Citire caracter cu caracter pana la o conditie data

'''text = 'python'
i = 0
while i < len(text):
    if text[i] == 'h':
        i += 1
        continue
    print(text[i])
    i += 1'''

# try / except

'''try:
    x = 10 / 0
except ZeroDivisionError:
    print("Nu poti imparti la 0")'''

secret = random.randint(1, 5)
incercari_maxime = 3
incercari = 0
ghicire = None

print("Ghiceste nr. Ai 3 incercari")
while ghicire != secret and incercari < incercari_maxime:
    try:
        ghicire = int(input("Ghiceste numarul(1, 5): "))
        incercari += 1

        if ghicire < secret:
            print("Numarul este mai mare")
        elif ghicire > secret:
            print("Numarul este mai mic")
    except:
        print("Introdu un numar valid")
        continue

if ghicire == secret:
    print(f"Ai ghicit din {incercari} incercari")
else:
    print(f"Ai pierdut. Numarul era {secret}")









