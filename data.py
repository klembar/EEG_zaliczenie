import csv
import math


class DataSet:

    def __init__(self, file_path, has_header=True):
        self.has_header = has_header
        self.file_path = file_path
        self.data = self.get_data()  # pod nazwa data mamy dane w postaci listy
        self.header = self.get_header()

    def __str__(self):  # reprezentacja tekstowa obiektow naszej klasy - do uzycia np w print()
        return f"DataSet: {self.file_path} Size: {len(self.data)}"

    def __getitem__(self, item):  # pozwala na wybranie danych jak z listy (np. d[0] - pierwszy element z listy danych)
        return self.data[item]

    def print_header(self):  # wypisuje na ekran, ale nic nie zwraca (nie ma slowa return wewnatrz funckji)
        print(self.header)

    def get_header(self):  # nie wypisuje, ale zwraca (slowo return)
        if self.has_header:
            with open(self.file_path, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                return next(csv_reader)
        else:
            return []

    def get_data(self):  # zaladowanie danych z pliku csv i zwrocenie jako lista
        with open(self.file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            if self.has_header:
                next(csv_reader)  # przeskakuje jeden element readera (pierwszy, czyli header)
            return list(csv_reader)

    def get_divided_sets(self, training_perc, validation_perc, test_perc):
        """ dzieli zbior danych na trzy grupy i je zwraca"""
        if (training_perc + validation_perc + test_perc) > 1:
            return ValueError("Procenty sie nie zgadzaja")

        size = len(self.data)
        training_size = math.floor(size * training_perc)  # math.floor - zaokraglenie w dol
        valid_size = math.floor(size * validation_perc)  # modul math musi byc zaimportowany
        test_size = math.floor(size * test_perc)

        training_set = self.data[0:training_size]
        valid_set = self.data[training_size:training_size + valid_size]
        test_set = self.data[training_size + valid_size:training_size + valid_size + test_size]

        return training_set, valid_set, test_set  # jesli po return jest kilka wartosci po przecinku,
        # to jest to zwracane jako krotka (tuple)
        # wynik takiej metody mozna "rozpakowac" (unpack)
        # train, valid, test = dataset.get_divided_sets(0.5, 0.1, 0.2)
        # wtedy train bedzie lista wynikow training_set itd.
    def print_data_range(self, start=None, end=None):  # wypisywanie danych wg życzenia od do
        for row in self.data[start:end]:
            print(row)

    def get_classifiers(self):  # zwrócenie klas decyzyjnych jako zbiór
        classifiers = set()
        for row in self.data:
            classifiers.add(row[-1])
        return classifiers

    def count_classifiers(self):  # zwrócenie liczby klas decyzyjnych
        return len(self.get_classifiers())
