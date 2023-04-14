'''
with open("names.txt","r") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())
'''
# arquivo csv separado por virgula


with open("names.csv","r") as file:
    for line in file:
        '''row = line.rstrip().split(',')
        print(f"hello, {row[0]} is in {row[1]}")'''
        
        name, house = line.rstrip().split(',')
        print(f"hello, {name} is in {house}")
        