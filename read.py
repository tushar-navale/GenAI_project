import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
    
file = read_file('train.txt')
story = file.split('\n')
print(story[0]+ "\n")
print(story[1] + "\n")
print(story[2]+ "\n")
print(story[3]+ "\n")
