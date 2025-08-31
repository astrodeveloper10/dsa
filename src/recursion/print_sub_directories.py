import os

def print_sub_directories(directory_name):
    for filename in os.listdir(directory_name):
        path = os.path.join(directory_name, filename)

        if os.path.isdir(path):
            print(path)
            print_sub_directories(path)



print_sub_directories('/Users/sivamadhira/swe')