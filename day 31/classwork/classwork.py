# შენს სახელს ვინახავთ ცვლადში
my_name = "nia"

# მომხმარებელს შეაქვს თავისი სახელი
user_name = input("შეიყვანე შენი სახელი: ")

# ვადარებთ სახელებს Case-insensitive ფორმით
if my_name.lower() == user_name.lower():
    print(True)
else:
    print(False)
