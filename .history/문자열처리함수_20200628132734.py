python = "Python is Amazing"
print(python.lower())  # python is amazing
# 전부 소문자로
print(python.upper())  # PYTHON IS AMAZING
# 전부 대문자로
print(python[0].isupper())  # True
# 첫 문자가 대문자인지에 관한 참 / 거짓 판명
print(len(python))  # 17
# 문자 길이 표시
print(python.replace("Python", "Java"))  # Java is Amazing
# Python 을 Java로 대체

index = python.index("n")  # 5
# n 의 위치파악
print(index)
index = python.index("n", index + 1)  # 15
# 2번째 n 의 위치파악
print(index)
