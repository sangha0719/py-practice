# 모듈은 확장자가 .py이다.

# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv  # as로 별명 설정하여 줄여 사용 가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *  # 모듈에 있는 모든 것을 사용하겠다는 의미
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price, price_morning  # 모듈에 있는 내가 선택한 것을 사용하겠다는 의미

