filename = "learning_python.txt"
with open(filename) as f:
    for line in f.readlines():
        print(line.replace("Python", "Java"))
