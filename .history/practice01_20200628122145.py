# 애완동물을 소개해 주세요~
print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 강아지 이름이 연탄에서 해피로 변경할 때
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 변수를 변경할 때
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# + 를 대신하여 , 로 사용가능하다.
# , 를 사용할 때에는 자동으로 한칸이 띄어지기 때문에 주의해야한다.
# , 를 사용할 경우에는 정수형 변수나 불리언 변수를 그대로 사용할 수 있기에 str없이 사용 가능하다.
print(name + "는 어른일까요? " + str(is_adult))
