# weather = "비"
# if 조건 : == "비":
#     실행 명령문

weather = "비"
if weather == "비":
    print("우산을 챙기세요")

weather = "맑아요"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")
