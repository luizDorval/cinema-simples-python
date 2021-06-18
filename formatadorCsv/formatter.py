import os
import pandas
import csv
read_file = pandas.read_csv(os.path.abspath("./veiculos.txt"))
read_file.to_csv(os.path.abspath('./veiculos.csv'), index=None)


def vogal(v):
    if (v == "a" or v == "e" or v == "i" or v == "o" or v == "u"):
        return True
    else:
        return False


def questionA():
    with open('veiculos.csv') as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()

        print('A)')
        for row in reader:
            if (int(row[2]) >= 2015 and int(row[2]) <= 2018):
                print(row[0] + ', ' + row[1] + ', ' +
                      row[2] + ', ' + row[3] + ', ' + row[4])


def questionB():
    with open('veiculos.csv') as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()

        print('B)')
        for row in reader:
            if(vogal(row[0][0])):
                print(row[0] + ', ' + row[1] + ', ' +
                      row[2] + ', ' + row[3] + ', ' + row[4])
            elif (not (vogal(row[0][len(row[0])-1]))):
                print(row[0] + ', ' + row[1] + ', ' +
                      row[2] + ', ' + row[3] + ', ' + row[4])


def questionC():
    with open('veiculos.csv') as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()

        print('C)')
        arquivo = open('autonomia.txt', 'a')
        for row in reader:
            autonomia = float(row[4]) * float(row[3])

            if(autonomia < 650):
                texto = str(autonomia)
                print(texto)
                texto += "\n"
                arquivo.write(texto)

        arquivo.close()


questionA()

questionB()

questionC()
