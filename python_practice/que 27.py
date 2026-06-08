population = 10000

for year in range(10,0,-1):
    print(f"{year}th year - {int(population)}")
    population= population / 1.10
