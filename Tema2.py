'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals
    ---Inceputul problemei --------

    parola = input("Introduc parola:")

    este_valida = True

    if len(parola) < 10
        print("Parola sa aiba cel putin 10 caractere.")
        este_valida = False

    if " " in parola:
        print("Parola nu trebuie sa conțina spati.")
        este_valida = False

    if este_valida:
        print("OK")

--- Sfarsitul problemei -----

    '''

'''Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.
---- Inceputul problemei ---- 
cuvant = input("Introduc un cuvant:")
litera = input("Introduc litera de cautat:")

count = 0
for caracter in cuvant:
    if caracter == litera:
        count += 1

print(f"litera '{litera}' apare de {count} ori in cuvantul '{cuvant}'")

----Sfarsitul problemei------ 
'''

'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.
---Inceputul problemei -----
putere = 1
while True:
    valoare = 3 ** putere
    if valoare > 300:
        
    if 200 <= valoare <= 300:
        print(valoare)
        putere += 1
----Sfarsitul problemei------ 
'''

'''Problema 4. Se citeste un numar de la tastatura. 
    Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)
----Inceputul problemei
    Este aceas ca la 6.
    '''

'''Problema 5. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
   Se citeste un numar n de la tastatura. Sa se scrie un program care
    face o numaratoare inversa de la numarul respectiv pana la 0.
    
    #Varianta 1 -> FOR
    n = int(input("Introduc un numar:"))

for i in range(n, -1, -1):
    print(i)
    
    #Varianta 2 -> WHILE
    n = int(input("Introduc un numar:"))
    while n >= 0:
        print(n)
        n -= 1
    
    '''

'''Problema 6. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
    Se citeste un numar de la tastatura. Sa se calculeze 
        suma numerelor de la 1 pana la numarul citit. (folositi for si while)
   
   #Varianta 1 -> FOR
   n = int(input("Introduceti un numar: "))
   suma = 0

   for i in range(1, n + 1):
    suma += i

    print(f"Suma de la 1 la {n} este: {suma}")

    #Varianta 2 -> WHILE
    n = int(input("Introduceti un numar:"))
    suma = 0
    i = 1

    while i <= n:
        suma += i
        i += 1

    print(f"Suma de la 1 la {n} este: {suma}")
        
        '''