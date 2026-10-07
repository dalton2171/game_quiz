#user is asked hies or her name
name = input("what is your name? ").strip().title()

first, last = name.split(" ")
# say hello to the user
print(f"hello, {name}")