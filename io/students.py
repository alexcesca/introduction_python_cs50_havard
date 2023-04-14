import sys
import csv
students = []

'''
#utilizando reader de arquivo.
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
'''
'''
#Utilizando reader do csv
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name":name,"house":house})
'''
#Utilizando reader do csv onde retorna um dicionario.
with open("students_cabec.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #adicionando manualmente
        #students.append({"name":row["name"],"house":row["house"]}) 
        
        #como o dictReader retorna um dicionario, pode ser incluido diretamente.
        students.append(row)

'''
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"hello, {student['name']} is in {student['house']}")
'''

'''
#utilizando Lambda na função de ordenação
for student in sorted(students, key=lambda student:student["name"]):
    print(f"hello, {student['name']} is in {student['house']}")
''' 
   
#utilizando Lambda na função de ordenação co mpassagem de parametro na chamada do arquivo.
for student in sorted(students, key=lambda student:student[sys.argv[1]]):
    print(f"hello, {student['name']} is in {student['house']}")