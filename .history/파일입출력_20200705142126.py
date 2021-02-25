# score_file = open("score.txt", "w", encoding="utf8")
# # w는 쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
# a는 이어적기
score_file.write("과학 : 80점")
score_file.write("\n코딩 : 100점")
score_file.close()
