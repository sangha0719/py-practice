# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# stdout = 표준 출력
# stderr = 표준 에러 처리

# # 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():  # key와 value를 쌍으로 보내준다.
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # ljust()는 왼쪽 정렬을 의미한다.
#     # rjust()는 오른쪽 정렬을 의미한다.
#     # () 안의 숫자만큼의 칸을 띄어쓰기 해준다.

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill() 괄호 안의 숫자만큼 공간을 확보하고 빈 공간에는 0을 채워 넣는다.

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))  # <class 'str'>
# print("입력하신 값은 " + answer + "입니다.")

answer = 10
print(type(answer))  # <class 'str'>
