cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet.get(3))
# .get을 쓸데에는 ()를 쓴다.
# print(cabinet[5])
# 키값 5가 없기 때문에 오류발생후 종료
print(cabinet.get(5))
# .get를 사용하면 None이 뜨고 계속 작동 가능
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet)