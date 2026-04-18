# print('code is running')

# dictionary, list, keys, string, numbers, tupel

# funtion
def greetword(name):
    print(name)

greetword("hello_world")

# Variables
name = "Faizan"
age = 22

# List
skills = ["Python", "Django", "JavaScript"]

# Function
def user_info(name, age, skills):
    if age >= 18:
        status = "Adult"
    else:
        status = "Minor"

    return {
        "name": name,
        "age": age,
        "status": status,
        "skills": skills
    }

# Loop
info = user_info(name, age, skills)

for key, value in info.items():
    print(key, ":", value)


