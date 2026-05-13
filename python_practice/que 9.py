a, b, c = map(int, input("Enter three angles: ").split())

if (a + b + c == 180):
    print("It is a triangle")
else:
    print("It is not a triangle")