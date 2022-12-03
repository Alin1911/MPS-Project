import csv
import os
import numpy as np
from sklearn.model_selection import train_test_split
import random
import math
import time
import copy

# extragerea setului de date
def parse_csv(search_path):
    thresholds = np.empty((0,15))
    fmeasure = np.empty((0,256))
    file_nr = 0
    for root, dir, files in os.walk(search_path):
        for filename in files:
            csv_file = os.path.join(root, filename)
            f = open(csv_file, 'r')
            csv_reader = csv.reader(f, delimiter=',')
            counter = 0
            for row in csv_reader:
                counter += 1
                if counter == 1:
                    thresholds = np.vstack([thresholds, row[1:]])
                if counter == 2:
                    fmeasure = np.vstack([fmeasure, row[0:256]])
            file_nr += 1
            if file_nr > 2500:
                return thresholds, fmeasure
    return thresholds, fmeasure

# functiile utilizabile
def f1(x1, n):
    return min(float(x1) + 0.1, 1)

def f2(x1, x2, n):
    return max(float(x1), float(x2))

def f3(x1, x2, x3, n):
    if float(x1) > float(x3):
        return max(float(x2) - n * 0.02, 0)
    else:
        return min((float(x2) + float(x3)) / 2 + n * 0.012, 1)

def f4(x1, x2, x3, x4, n):
    if float(x1) > float(x2):
        return min(abs(float(x3) - float(x4)) + n * 0.016, 1)
    else:
        return max((float(x2) + float(x3)) / 2 - n * 0.01, 0)

def f5(x1, x2, x3, x4, x5, n):
    if float(x2) > float(x4):
        return min(abs(float(x1) - float(x4)) + n * 0.012, 1)
    else:
        return max((float(x2) + float(x3) + float(x5)) / 3 - n * 0.008, 0)

# alegerea listei de threshold-uri initiale cu care porneste un arbore
def choose_random_starting_thresholds():
    number_of_thresholds_choice = list(range(5, 16))
    thresholds_choice = list(range(0, 15))
    number_of_thresholds = random.choice(number_of_thresholds_choice)
    thresholds = random.sample(thresholds_choice, number_of_thresholds)
    return thresholds

# crearea unui arbore initial
def generate_starting_tree_structure():
    tree_data_structure = []

    thresholds_used = choose_random_starting_thresholds()
    for threshold in thresholds_used:
        tree_data_structure.append((threshold, None, None))

    i = 0
    while len(tree_data_structure) - i > 5:
        f = random.choice(list(range(30)))
        n = f // 10 + 3
        arguments = []
        while n: 
            arguments.append(i)
            i = i + 1
            n = n - 1
        tree_data_structure.append((None, f, arguments))

    arguments = []
    dif = len(tree_data_structure) - i
    if dif > 0:
        for j in range(dif):
            arguments.append(i)
            i += 1
        if(dif == 1):
            f = 31
        elif(dif == 2):
            f = 32
        elif(dif == 3):
            f = 1
        elif(dif == 4):
            f = 11
        elif(dif == 5):
            f = 21
        tree_data_structure.append((None, f, arguments)) 
    return tree_data_structure

# introducerea unui nou nod intr-un arbore existent, alegand cea mai buna optiune din pdv al metricii
def generate_new_node_in_tree(tree, threshold_dataset, fmeasure_dataset, number_of_options):
    best_tree = tree
    best_value = solve_over_dataset(tree, threshold_dataset, fmeasure_dataset)
    for i in range(number_of_options):
        new_tree = copy.deepcopy(tree)
        f = random.randrange(30)
        nodes_used = random.sample(list(range(len(tree) - 1)), f // 10 + 2)
        nodes_used.append(int(len(tree) - 1))
        new_tree.append((None, f, nodes_used))
        result = solve_over_dataset(new_tree, threshold_dataset, fmeasure_dataset)
        if result > best_value:
            best_value = result
            best_tree = new_tree
    return (best_tree, best_value)

# calcularea f-measure-ului unui arbore fiind dat un vector de threshold-uri initiale si un vector de f-measure
def solve(tree, threshold_list, fmeasure):
    value_list = []
    for node in tree:
        if node[1] is None:
            value_list.append(threshold_list[node[0]])
        if node[1] is not None:
            args = []
            for argument in node[2]:
                args.append(value_list[argument])
            args.append(int(node[1] // 10))
            if node[1] == 31:
                value_list.append(f1(*args))
            elif node[1] == 32:
                value_list.append(f2(*args))
            elif node[1] // 10 == 0:
                value_list.append(f3(*args))
            elif node[1] // 10 == 1:
                value_list.append(f4(*args))
            elif node[1] // 10 == 2:
                value_list.append(f5(*args))
    index = math.floor(value_list[-1] * 255)
    return fmeasure[index]

# maparea functiei solve pe un intreg set de date si obtinerea metricii principale de comparatie
def solve_over_dataset(tree, threshold_dataset, fmeasure_dataset):
    sum = 0
    t1 = time.time()
    for i in range(len(threshold_dataset)):
        sum += float(solve(tree, threshold_dataset[i], fmeasure_dataset[i]))
    t2 = time.time()
    return sum / len(threshold_dataset) - 10 * (t2 - t1)

# obtinerea metricii f-measure finale in cadrul etapei de test
def get_final_metrics(tree, threshold_dataset, fmeasure_dataset):
    sum = 0
    t1 = time.time()
    for i in range(len(threshold_dataset)):
        sum += float(solve(tree, threshold_dataset[i], fmeasure_dataset[i]))
    t2 = time.time()
    return (sum / len(threshold_dataset), t2 - t1)

# obtinerea unui arbore din etapa de antrenare
def train(t_train, f_train, number_of_trees, number_of_options):
    tree_dictionary = {}
    value_dictionary = {}
    print("In etapa de antrenare, vom crea " + str(number_of_options) + " arbori aleatori pe care sa ii comparam")
    for i in range(number_of_trees):
        tree_data_structure = generate_starting_tree_structure()
        tree_dictionary[i] = tree_data_structure
        value_dictionary[i] = solve_over_dataset(tree_data_structure, t_train, f_train)

    while len(tree_dictionary) > 1:
        for elem in list(tree_dictionary.keys()):
            (tree, value) = generate_new_node_in_tree(tree_dictionary[elem], t_train, f_train, number_of_options)
            print(str(elem) + ": " + str(value))
            tree_dictionary[elem] = tree
            value_dictionary[elem] = value
        print("A fost eliminat arborele cu indicele " + str(min(value_dictionary, key=value_dictionary.get)))
        tree_dictionary.pop(min(value_dictionary, key=value_dictionary.get))
        value_dictionary.pop(min(value_dictionary, key=value_dictionary.get))
    return list(tree_dictionary.values())[0]

# obtinerea unui arbore din etapa de validare
def validate(best_tree, t_validation, f_validation, number_of_trees, number_of_options):
    tree_dictionary = {}
    value_dictionary = {}
    print("In etapa de validare, comparam arborele obtinut in etapa de antrenare cu alti " + str(number_of_options - 1) + " arbori aleatori, arborele initial avand indicele 0")
    tree_dictionary[0] = best_tree
    value_dictionary[0] = solve_over_dataset(best_tree, t_validation, f_validation)
    for i in range(1, number_of_trees):
        tree_data_structure = generate_starting_tree_structure()
        tree_dictionary[i] = tree_data_structure
        value_dictionary[i] = solve_over_dataset(tree_data_structure, t_validation, f_validation)

    while len(tree_dictionary) > 1:
        for elem in list(tree_dictionary.keys()):
            if elem != 0:
                (tree, value) = generate_new_node_in_tree(tree_dictionary[elem], t_validation, f_validation, number_of_options)
                print(str(elem) + ": " + str(value))
                tree_dictionary[elem] = tree
                value_dictionary[elem] = value
        print("A fost eliminat arborele cu indicele " + str(min(value_dictionary, key=value_dictionary.get)))
        tree_dictionary.pop(min(value_dictionary, key=value_dictionary.get))
        value_dictionary.pop(min(value_dictionary, key=value_dictionary.get))
    return list(tree_dictionary.values())[0]

# functie auxiliara pentru functia de scriere
def aux_str(n, l):
    if n + 1 > l:
        return "N" + str(n - l)
    else:
        return "T" + str(n + 1)

# interpretarea si scrierea rezultatului in fisier
def write_results_to_file(tree, file):
    f = open(file, "w")
    i = 0
    j = 0
    threshold_name_list = ['Otsu', 'Kittler', 'Lloyd', 'Sung', 'Ridler', 'Huang', 'Ramesh', 'Li1', 'Li2', 'Brink', 'Kapur', 'Sahoo', 'Shanbhag', 'Yen', 'Tsai']
    for elem in tree:
        if elem[0] is not None:
            i += 1
            f.write("T" + str(i) + ": " + threshold_name_list[elem[0]] + " threshold")
        else:
            if elem[1] == 31:
                f.write("N" + str(j) + " = min(" + aux_str(elem[2][0], i) + " + 0.1, 1)")
            elif elem[1] == 32:
                f.write("N" + str(j) + " = max(" + aux_str(elem[2][0], i) + ", " + aux_str(elem[2][1], i) + ")")
            elif elem[1] // 10 == 0:
                f.write("N" + str(j) + " = " + aux_str(elem[2][0], i) + " > " + aux_str(elem[2][2], i) + " ? max(" + aux_str(elem[2][1], i) + " - " + str(0.02 * (elem[1] % 10)) + ", 0) : min((" + aux_str(elem[2][1], i) + " + " + aux_str(elem[2][2], i) + ") / 2 + " + str(0.012 * (elem[1] % 10)) + ", 1)")   
            elif elem[1] // 10 == 1:
                f.write("N" + str(j) + " = " + aux_str(elem[2][0], i) + " > " + aux_str(elem[2][1], i) + " ? min(abs(" + aux_str(elem[2][2], i) + " - " + aux_str(elem[2][3], i) + ") + " + str((elem[1] % 10) * 0.016) + ", 1) : max((" + aux_str(elem[2][1], i) + " + " + aux_str(elem[2][2], i) + ") / 2 - " + str((elem[1] % 10) * 0.01) + ", 0)")
            elif elem[1] // 10 == 2:
                f.write("N" + str(j) + " = " + aux_str(elem[2][1], i) + " > " + aux_str(elem[2][3], i) + " ? min(abs(" + aux_str(elem[2][0], i) + " - " + aux_str(elem[2][3], i) + ") + " + str((elem[1] % 10) * 0.012) + ", 1) : max((" + aux_str(elem[2][1], i) + " + " + aux_str(elem[2][2], i) + " + " + aux_str(elem[2][4], i) + ") / 3 - " + str((elem[1] % 10) * 0.008) + ", 0)")
            j += 1 
        f.write("\n")
    f.write("^")
    f.write("\n")
    f.write("|")
    f.write("\n")
    f.write("root")
    f.close()
        

# parsarea input-ului si crearea setului de date
print("Se incarca setul de date...")
t, f = parse_csv('MPS-Global')
t_train, x, f_train, y = train_test_split(t, f, test_size=0.3, random_state=42)
t_validation, t_test, f_validation, f_test = train_test_split(x, y, test_size = 0.16666, random_state=69)
print("Set de date incarcat!")
print(" ")

# etapa de antrenare
training_final_tree = train(t_train, f_train, 10, 10)
print(" ")
print("Arborele obtinut dupa etapa de antrenare a fost salvat in fisierul test_result.txt")
write_results_to_file(training_final_tree, "test_result.txt")
print(" ")

# etapa de validare
validation_final_tree = validate(training_final_tree, t_validation, f_validation, 10, 10)

# etapa de testare
(best_tree_metric, timpul) = get_final_metrics(validation_final_tree, t_test, f_test)
print(" ")
print("Arborele obtinut dupa etapa de validare a fost salvat in fisierul final_result.txt")
write_results_to_file(validation_final_tree, "final_result.txt")
print(" ")
print("Arborele final a obtinut in etapa de test un scor f-measure final de " + str(best_tree_metric) + " intr-un timp de " + str(timpul) + "s.")