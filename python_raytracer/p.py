class Car():
    def __init__(self, is_car=True):
        self.is_car = is_car

class vol(Car):

    def __init__(self, types="volvo"):
        super().__init__()
        self.types = types


if __name__ == "__main__":
    v = vol()

    print(v.is_car)