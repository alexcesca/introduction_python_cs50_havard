def main():
    x = int(input("what's x?"))
    if (is_even(x)):
        print("Even")
    else:
        print("Odd")
        
def is_even(x):
    return ((x%2)==0)

main()