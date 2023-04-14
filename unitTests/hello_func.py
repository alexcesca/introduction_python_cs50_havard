# create a main function
def main():
    name = input("what's your name? ")
    print(hello(name))


##create a main function
# you can define a default value with = value
def hello(to="world"):
    return f"hello, {to}"


# python rum top down
if __name__ == "__main__":
    main()
