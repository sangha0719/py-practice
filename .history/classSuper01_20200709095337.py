class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
# 두개 이상의 부모 클래스를 다중상속 받을 경우에는 super를 사용하게 되면
# 

# 드랍쉽
dropship = FlyableUnit()
