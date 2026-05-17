heads = int(input("enter total heads: "))
legs = int(input("enter total legs: "))

chicken = (4*heads-legs)//2
dogs = heads-chicken

print("dogs is: ",dogs)
print("chicken is: ",chicken)
