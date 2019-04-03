class Engine:
    def start (self):
        pass

    def stop (self):
        pass
class ElectricEngine (Engine):
    pass
class V8Engine (Engine):
    pass
class Car:
    engine_cls = Engine

    def __init__ (self) :
        self.engine = self.engine_cls ()
    def start (self):
        print("Starting engine (0) for car {0} for car {1} Wroom, wroomx!"
                .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
        )
    def stop (self):
        self.engine.stop ()

class RaceCar (Car):
     engine_cls = V8Engine
class CityCar (Car):
    engine_cls = ElectricEngine
class F1Car (RaceCar):
    pass

car = Car()
racecar = RaceCar ()
citycar = CityCar ()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()