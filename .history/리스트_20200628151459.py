# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 다음 정류장에서 하하씨가 탔다.
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 넣어본다.
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼낸다.
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능하다.
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
