# score_file = open("score.txt", "r", encoding="utf8")
# # r은 읽어 오는 것
# print(score_file.read())
# score_file.close()

# 한줄 씩 처리할 때
score_file = open("score.txt", "r", encoding="utf8")
# 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다. 뒤에 end를 표시하면 한줄 더 건너뛰기를 안 할 수 있다.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
