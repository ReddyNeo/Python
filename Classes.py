class car():
    def __init__(self, modeltype , yearm, price):
        self.modeltype = modeltype
        self.yearm = yearm
        self.price = price
    def price_inc(self):
        self.price=int(self.price * 1.5)

honda = car("City", 2017 , 100000)
tata = car("Neoxn" , 2021, 1200000)

print(honda.price)
honda.price_inc()
print(honda.price)