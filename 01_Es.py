# 1) Da lista1 = [1, 2, 3, 4, 5], creo lista2 che ha tutti i valori raddoppiati

lista1 = [1, 2, 3, 4, 5]
lista2 = []

for item in lista1:
    lista2.append(item * 2)

print(lista2)

#oppure

lista2 = [item * 2 for item in lista1]      #list comprehension
print(lista2)



# 2) Trovo il fattoriale di un numero inserito in input

valore = int(input("Inserisci un numero usato per il fattoriale: "))
fattoriale = 1

for i in range(1, int(valore) + 1):     #deve partire da 1 a valore incluso perchè il range se parte da 0 non permette di calcolare il fattoriale
    fattoriale = fattoriale * i

print(fattoriale)

# 3) Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore

dizionario = {"a": 1, "b": 2, "c": 3}
invertito = {}
for chiave, valore in dizionario.items():
    invertito[valore] = chiave

print(invertito)