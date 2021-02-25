class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
# 두개 이상의 부모 클래스를 다중상속 받을 경우에는 super를 사용하게 되면
# 순서상의 맨 마지막에 상속받는 클래스에 대해서만 init함수가 호출된다.
# 그래서 다중 상속을 할 때에는 따로 명시적으로
        Unit.__init__(self)
        Flyable.__init__(self)
#


# 드랍쉽
dropship = FlyableUnit()
