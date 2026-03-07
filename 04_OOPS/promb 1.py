class car:
    total_car = 5
    
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        car.total =+ 1
        
    def fuel_type(self):
        return "petrol and diesel"
    
    
    @staticmethod
    def general_description():
         return "cars are means of transport"
     
   
class ElectricalCar(car):
     def __init__(self,brand,model,battery_size):
         
        super().__init__(brand,model)
        self.battery_size = battery_size
        
     def fuel_type(self):
        return "electric charge"
    
    

my_tesla = ElectricalCar("90 kwh", "model p", "tesla")

'''isinstance(my_tesla.car)
isinstance(my_tesla.ElectricalCar)'''

'''print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)'''

#my_car = car("Tata" ,"safari")

'''print(my_car.brand)
print(my_car.model)

#print(my_car.general_description())
print(car.general_description())



safari = car("tata","safari")
print(safari.fuel_type())

print(car.total_car)'''


class battery:
    def battery_info(self):
        return "this is battery"

class engine:
    def engine_info(self):
        return "this is engine"
    

class electric_car(battery,engine,):
    pass

my_new_tesla = electric_car()
print(my_new_tesla.engine_info()) 
print(my_new_tesla.battery_info())