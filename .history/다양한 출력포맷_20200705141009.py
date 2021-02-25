# 빈 자리는 빈공간을 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 때는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(100000000000))
