# score_file = open("score.txt", "r", encoding="utf8")
# # r은 읽어 오는 것
# print(score_file.read())
# score_file.close()

# 한줄 씩 처리할 때
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다.
print(score_file.readline())  # 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다.
print(score_file.readline())  # 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다.
print(score_file.readline())  # 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다.
print(score_file.readline())  # 줄별로 읽기 수행 후 커서는 다음 줄로 이동한다.
score_file.close()
