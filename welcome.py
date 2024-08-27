import datetime

current_time = datetime.datetime.now().time()

if current_time < datetime.time(12):
    greeting = "Good morning"
elif current_time < datetime.time(18):
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

name = input("What is your name? ")
print(f"{greeting}, {name}!")
