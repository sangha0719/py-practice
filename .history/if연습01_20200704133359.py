weather = input("오늘 날씨는 어때요? ")

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
