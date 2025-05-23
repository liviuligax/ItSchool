''' O functie este un bloc de cod reutilizabil. Executa o sarcina specifica. Functiile ne ajuta sa scriem cod mai clar, mai scurt'''

'''
def nume_functie(parametru1, parametru2, ....)
    #bloc de cod
    return valoare
'''

'''def salut(nume):
    print(f"Salut, {nume}")

salut("Colegi")'''

#Functii cu return
'''def adunare(a, b):
    return a + b
rezultat = adunare(3,5)
print(rezultat)'''

#Functii fara parametri sau fara return
'''def afiseaza_mesaj():
    print("Functie fara parametri")
afiseaza_mesaj()

def calcul_pi():
    return 3.14
print(calcul_pi())'''

#Parametri impliciti
'''def salut(nume = "user"):
    print(f"Salut, {nume}")
salut()
salut("guys")'''

#Domenii de vizibilitate (scope)
'''Tipuri de scope:
    - Global - in afara functiilor
    - Local - in interiorul functiilor
    - Enclosing - functii nested/inlantuite
    - Built-in - functii/variabile predefinite'''

'''x = 10 #varibila globala

def test():
    x = 5 # variabila locala
    print(f"Local x {x}")
test()
print(f"Global, {x}")'''

#Modificarea unei variabile globale dintr-o functie

'''x = 10

def modifica():
    global x
    x = 20
modifica()
print(x)'''

#Regula LEGB - Python cauta variabilele in urmatoarea ordine:
'''
1. Local
2. Enclosing
3. Global
4. Built-in
'''

'''def functie_blank():
    pass'''

#Scope enclosing(nested)
'''def functie_exterioara():
    mesaj = 'Functie exterioara'

    def functie_interioara():
        print(mesaj)
    functie_interioara()
functie_exterioara()'''

#Functii lambda
'''
suma = lambda a, b: a + b
print(suma(3, 5))'''

#lambda poate avea doar o expresie, nu mai multe linii
# nu poate contine comenzi complicate precum if-else, for, while etc
# functie anonima(fara nume), folosita pentru a scrie rapid functii mici

#Enclosing scope(nonlocal)
'''def exterior():
    x = 10
    def interior():
        nonlocal x
        x += 1
        print(x)
    interior()
exterior()'''

#Exemplu care foloseste toate cele patru tipuri de scope

x = 'global'

def functie_exterioara():
    x = 'enclosing scope' # enclosing scope

    def functie_interioara():
        x = 'local' # local scope
        print(f"In functia interioara: {x}") # afiseaza variabila locala
    functie_interioara()
    print(f"In functia exterioara: {x}") # afiseaza variabila din enclosing scope
functie_exterioara()
print(f"In afara functiilor: {x}")



