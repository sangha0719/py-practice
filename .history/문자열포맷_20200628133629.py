# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)  # 20
# %d는 정수값만 입력이 가능하다.
print("나는 %s을 좋아해요." % "파이썬")  # 파이썬
# %s는 문자열 입력 가능
print("나는 %c로 시작해요." % "A")  # A
# %c는 한 문자만 가능하다.
print("나는 %s살입니다." % 20)  # 20
# %s는 다 가능 정수를 문자로 인식
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 파란, 빨간
# 순서대로 2개가 들어간다.

# 방법 2
print("나는 {}살입니다.".format(20))
# {}이용 format()의 값을 {}에 넣는다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# {}안에 숫자를 인식해서 format()의 위치에 맞는 값을 출력한다.
