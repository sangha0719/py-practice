# 패키지 설치 방법 알아보기
# 인터넷에서 pypi검색 거기서 찾아서 사용하기
# beautifulsoup4 검색
# 터미널 창에 pip install beautifulsoup4 쳐서 설치
# pip list 는 지금 깔려있는 것들 리스트 뽑아준다.
# pip show 는 원하는 패키지 설명을 볼 수 있다.
# pip install --upgrade beautifulsoup4 <- 방금 설치한 beautifulsoup4 의 버전을 업그레이드 할 수 있게 하는 명령어
# pip uninstall 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

