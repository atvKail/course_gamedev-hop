class cars:
    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed

    def body_momentum(self):
        return self.weight * self.speed, "кг*м/с"


class passenger_s(cars):
    def __init__(self, weight, speed, passengers):
        cars.__init__(self, weight, speed)
        self.passengers = passengers

    def weight_with_passengers(self):
        return self.weight + self.passengers[0] * self.passengers[1]


class cargo(cars):
    def __init__(self, weight, speed, cargo_weight):
        cars.__init__(self, weight, speed)
        self.cargo_weight = cargo_weight

    def loaded_weight(self):
        return self.weight + self.cargo_weight


cargo_car = cargo(3000, 40, 1200)
passenger_car = passenger_s(2000, 120, (3, 95))
car_all = cars((cargo_car.weight + passenger_car.weight) // 2, (cargo_car.speed + passenger_car.speed) // 2)
print(cargo_car.loaded_weight())
print(passenger_car.weight_with_passengers())
print(car_all.body_momentum())
