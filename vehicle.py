class vehicle:
    def __init__(self, brand , year):
        self.brand=brand
        self.year= year

        
class car(vehicle):
    def __init__(self, brand, year, no_of_doors):
        super().__init__(brand, year)
        self.no_of_doors=no_of_doors

    def examine(self):
        print(f"the car is a {self.brand} {self.year} with {self.no_of_doors} doors")

class motorcycles(vehicle):
    def __init__(self, brand, year , has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar=has_sidecar

    def examine(self):
        print(f"the motorcycle is a {self.brand} {self.year} and {self.has_sidecar}")


car1= car('toyota_corolla', 2023, 4)
motorcycles1= motorcycles('BMW R75', 1943, 'Has a side_car')

car1.examine()
motorcycles1.examine()
