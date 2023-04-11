students = [
    {"name":"Hermione","house":"Gryffindor","patronus":"otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slyntherin","patronus":None}
    
]

for student in students:
    print(student["name"], student["house"],student["patronus"],sep=', ')
    