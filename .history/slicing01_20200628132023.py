jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])  # 2 부터 4 직전까지 (2, 3)
print("일 : " + jumin[4:6])  # 4 부터 6 직전까지 (4, 5)

print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7 부터 끝까지
print("뒤 7자리 : (뒤에서 부터)" + jumin[-])
