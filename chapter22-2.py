import pickle
name = str(raw_input("Enter your name:"))
age = float(raw_input("Enter your age:"))
color = str(raw_input("Enter your favourite color:"))
food = str(raw_input("Enter your favourite food:"))
my_list = [name, age, color, food]
pickle_file = open("my_pickle_file.pkl", 'w')
pickle.dump(my_list, pickle_file)
pickle_file.close()
