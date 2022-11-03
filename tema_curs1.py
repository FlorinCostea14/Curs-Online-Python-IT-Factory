1. # variabila - este o zona din memorie in care punem date

2.
marca_masina = 'VW Golf'
an_fabricatie = 2004
pret = 3599.5500
inmatriculata = False

3.
print(type(marca_masina))
print(type(an_fabricatie))
print(type(pret))
print(type(inmatriculata))

4.
pret = 3599.5500
print(round(pret, 2))
pret = 3599.55
print(type(pret))

5.
print(f'Mi-am cumparat o masina {marca_masina}.')
print(f'Este fabricata in anul {an_fabricatie}.')
print(f'A costat {pret}.')
inmatriculata = False
if (inmatriculata == True):
    print ('Masina este inmatriculata')
elif (inmatriculata == False):
    print ('Masina nu este inmatriculata')

6.
prenume = input('Prenume: ')
nume = input('Nume: ')
nume_complet = prenume + ' ' + nume
print(nume_complet)
print(f'Numele complet are', len(nume_complet), 'caractere.')

7.

8.
string = 'Coral is either the stupidest animal or the smartest rock'
print(string.count('the'))

9.
string = 'Coral is either the stupidest animal or the smartest rock'
string_new = string.replace('the', 'THE')
print(string_new)

# optional
14.
pi = 3.146712
print(round(pi, 2))
