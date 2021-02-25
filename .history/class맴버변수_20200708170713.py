class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# __init__ 은 생성자이다.


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)
# __init__ 함수에 정의된 self를 제외한 갯수만큼 똑같은 정보를 보내주어야 객체생성이 가능하다.
