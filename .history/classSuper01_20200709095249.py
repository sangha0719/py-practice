class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
# 다중상속의 경우 

# 드랍쉽
dropship = FlyableUnit()
