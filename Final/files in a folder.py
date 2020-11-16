import os
x=os.getcwd()
#print(os.path.abspath(__file__))
for file in os.listdir(x):
   # print(file)
    if file.endswith(".txt"):
        print(file)
