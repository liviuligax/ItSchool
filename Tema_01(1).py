'''Problema 1. Operatii aritmetice
Scrie un program care:
    - Cere doua numere si calculeaza:
        - Suma
        - Diferenta
        - Produsul
        - Impartirea
        - Imaprtirea intreaga
        - Restul impartirii (modulo)
        - Puterea
    - La final, afiseaza fiecare rezultat
'''

#Incepe de aici problema 1

z = float(input("Primul număr: "))
x = float(input("Al doilea număr: "))

suma = z + x
diferenta = z - x
produsul = z * x
impartirea = z / x
impartirea_intreaga = z // x
restul_impartirii = z % x
puterea = z ** x

print("Rezultatele operațiilor:")
print(f"Suma: {suma}")
print(f"Diferența: {diferenta}")
print(f"Produsul: {produsul}")
print(f"Împărțirea: {impartirea}")
print(f"Împărțirea întreagă: {impartirea_intreaga}")
print(f"Restul împărțirii: {restul_impartirii}")
print(f"Puterea: {puterea}")

#Sfarsit problema 1


'''Problema 2. Tipuri de date
Declara cate o variabila pentru fiecare tip de date studiat si afiseaza tipul acesteia
'''

#Incepe de aici problema 2

nume = "Liviu"
an_nastere = 1995
varsta = 29
inaltime = 1.79
numar_complex = 11 + 8j

print("nume (str):", nume)
print("an_nastere (int):", an_nastere)
print("varsta (int):", varsta)
print("inaltime (float):", inaltime)
print("numar_complex (complex):", numar_complex)

major = True
minor = False

print("major (bool):", major)
print("minor (bool):", minor)

hobbyuri = ["filme", "seriale", "programare", "drumeții", "sport"]
zile_libere = ("sambata", "duminica")
limbi = {"romana", "engleza"}

print("hobbyuri (list):", hobbyuri)
print("zile_libere (tuple):", zile_libere)
print("limbi (set):", limbi)



ani_de_viata = range(1995, 2095)
print("ani_de_viata (range):", list(ani_de_viata))

membre_rupte = None
nume_bytes = b"Liviu"

print("membre_rupte (NoneType):", membre_rupte)
print("nume_bytes (bytes):", nume_bytes)

#Sfarsit problema 2


''' Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar
'''

#Incepe de aici problema 3

minute = int(input("Introdu numărul de minute: "))
ore = minute // 60
minute = minute % 60

print(f"{ore} ore și {minute} minute")

#Sfarsit problema 3


''' Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA
'''

#Incepe de aici problema 4

produs_bere = float(input("Introdu prețul la bere: "))
produs_pizza = float(input("Introdu prețul la pizza: "))
produs_desert = float(input("Introdu prețul la desert: "))

total_fara_tva = produs_bere + produs_pizza + produs_desert
tva = total_fara_tva * 0.19
total_cu_tva = total_fara_tva + tva

print(f"Totalul fără TVA: {total_fara_tva} RON")
print(f"TVA (19%): {tva} RON")
print(f"Totalul cu TVA: {total_cu_tva} RON")

#Sfarsit problema 4

'''Problema 5. Bugetul pentru un concediu
Cerinta: Un grup de prieteni planuieste o vacanta. Trebuie sa calculezi: 
    - Contributia totala
    - Costul cheltuielilor (transport, cazare, mancare pe zile)
    - Ce suma ramane pentru distractii

Date de intrare: 
    - Numarul de prieteni
    - Suma de bani per persoana
    - Costul transportului
    - Costul pe zi pentru cazare
    - Costul pe zi pentru mancare
    - Numarul de zile
'''

#Incepe de aici problema 5

nr_prieteni = int(input("numarul de prieteni:"))
suma_per_persoana = float(input("suma de bani per persoana:"))
cost_transport = float(input("costul transportului:"))
cost_cazare_zi = float(input("costul pe zi pentru cazare:"))
cost_mancare_zi = float(input("costul pe zi pentru mancare:"))
nr_zile = int(input("numarul de zile:"))

contributie_totala = nr_prieteni * suma_per_persoana
cost_cazare_total = cost_cazare_zi * nr_zile
cost_mancare_total = cost_mancare_zi * nr_zile
cheltuieli_totale = cost_transport + cost_cazare_total + cost_mancare_total

suma_distractii = contributie_totala - cheltuieli_totale

print("Rezumat buget")
print(f"Contributia totala: {contributie_totala:}RON")
print(f"Cheltuieli totale (transport, cazare, mancare): {cheltuieli_totale:}RON")
print(f"Suma ramasa pentru distractii: {suma_distractii:}RON")

#La problema 5 m-am ajutat de pe internet,putin.. nu am stiut cum se calculeaza "suma_distractii" si "cheltuieli_totale" ...
#Dupa ce am gasit am inteles si am incercat sa duc la capat problema.

#Sfarsit problema 5