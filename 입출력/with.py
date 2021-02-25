import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# close() 없이 자동으로 종료가 된다.
