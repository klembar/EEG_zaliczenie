from data import DataSet

d1 = DataSet('data.csv')

train, valid, test = d1.get_divided_sets(0.5, 0.4, 0.1) # podział danych na trzy grupy wg ustalonych procentów tu(50%, 40%, 10%)

print(len(train)) # wypisuje liczbę rekordów treningowych
print(len(valid)) # wypisuje liczbę rekordów walidacyjnych
print(len(test)) # wypisuje liczbę rekordów testujących

print("Suma " + str(len(train) + len(valid) + len(test))) # wypisuje liczbę wszystkich rekordów

d1.print_data_range(0, 5) #wypisanie rekordów od start do end

print(d1.count_classifiers()) #wypisanie liczby klasyfikatorów

print(d1.get_classifiers()) # wypisanie klasyfikatorów

print(f"Operacje na zestawie: {d1}")  # wykorzystana zostanie metoda __str__

a = 1
d1.print_header() #wypisanie etykiet
print("Kot")
etykiety1 = d1.get_header()#inny sposób na wypisanie etykiet
print(etykiety1)
print("Mysz")
print(d1[0]) #wypisuje pierwszy rrekord z danych
print("Pies")
print(train[0]) #wypisuje wybrany rekord (tu pierwszy) z danych treningowych
print(valid[1]) #wypisuje wybrany rekord (tu drugi) z danych walidacyjnych
print(test[1]) #wypisuje wybrany rekord (tu trzeci) z danych testujących


