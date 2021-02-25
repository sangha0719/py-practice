# import travel.thailand
# # import travel.thailand.ThailandPackage <- 사용이 불가능하다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from import 함수에서는 모듈, 패키지, 함수 모두 import할 수 있다.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage() <- 
trip_to.detail()
