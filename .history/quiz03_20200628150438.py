# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

site = "http://naver.com"
index = site.index("/")
rule1 = site.index("/", index + 1)
pass1 = site[rule1 + 1:]
print(pass1)
rule2 = pass1[:pass1.index(".")]
print(rule2)
password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
print(password)

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[my_str.index(".")] # 규칙 2
password1 = my_str[:3] + str(len(my_str)) + str(my)