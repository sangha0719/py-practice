import pickle
# profile_file = open("profile.pickle", "wb")
# # w 뒤에 오는 b는 바이너리라고 한다. pickle을 사용하기 위해서는 바이너리 타입을 설정해 주어야 한다.
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장한다.
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file


