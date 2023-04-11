#create a main function
def main() :
    name = input("what's your name? ")
    hello(name)

##create a main function
# you can define a default value with = value
def hello(to="world" ):
    print(f"hello, {to}")
     
#python rum top down 
main()