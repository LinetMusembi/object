class Car:
    def __init__(self,make,color,model):
        self.make = make
        self.color=color
        self.model=model
    def show_description(self):
        return f"This is a {self.color},{self.make}"
    def change_colour(self):
        return self.color
    def show_make(self):
        return f"This type {self.make} is more preferable"
    



    # car.py

class Car:
    make = "Unknown"
    
    def __init__(self, model, color, mileage):
        self.model = model
        self.color = color
        self.mileage = mileage
        
    def drive(self, miles):
        self.mileage += miles
        
    def repaint(self, new_color):
        self.color = new_color
        
    def get_info(self):
        print(f"This is a {self.color} {self.make} {self.model} with {self.mileage} miles.")
        



