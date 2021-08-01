class Vehicle:
    name =""
    kind ="car"
    color = "blue"
    value = 1000.0

    def desc(self):
        str = "%s is a %s with %s color, it cost rm %.2f" %(self.name, self.kind,self.color,self.value)
        return str

car1 = Vehicle();
car1.name = 'audi'
car1.color = 'red'

print(car1.desc())