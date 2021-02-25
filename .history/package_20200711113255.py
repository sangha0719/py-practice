# import travel.thailand
# # import travel.thailand.ThailandPackage <- 사용이 불가능하다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel import vietnam
# from import 함수에서는 모듈, 패키지, 함수 모두 import할 수 있다.
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

trip_to = vietnam.VietnamPackage()
trip_to.detail()
