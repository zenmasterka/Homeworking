class Car:
    def __init__(self, name, model):
        self.name = name        
        self.model = model
    def engine(self, eng):
        self.eng = eng
        print(f"Тип двигателя {self.name} {self.model} - {self.eng}")
    def colour(self, col):
        self.col = col
        print(f"Машина имеет {self.col} цвет")
car1 = Car('БМВ', 'X5')
car1.engine('Дизель')
car1.colour('синий')
