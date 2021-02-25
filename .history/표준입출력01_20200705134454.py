# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# stdout = 표준 출력
# stderr = 표준 에러 처리

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():  # key와 value를 쌍으로 보내준다.
    # print(subject, score)
    print(subject.ljust(), score)
    