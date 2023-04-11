#x = ''
#try:
#    x = input("what's is x: ")
#    x_int = int(x)
#    print(f"X is {x_int}")
#except ValueError:
#    print(f"{x} is not an integer")
#


#try:
#    x = input("what's is x: ")
#except ValueError:
#    print(f"{x} is not an integer")
#else:
#    print(f"X is {x_int}")

while True:
    try:
        x = int(input("what's is x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"X is {x}")