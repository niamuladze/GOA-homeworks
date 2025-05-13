# 2) სტრინგის და სიის ძირითადი ფუნქციები კომენტარით:

#  სტრინგის ფუნქციები 
# .lower() - გარდაქმნის სტრინგს პატარა ასოებად
# .upper() - გარდაქმნის სტრინგს დიდ ასოებად
# .capitalize() - მხოლოდ პირველ ასოს გადაქცევს დიდ ასოდ
# .strip() - შლის ცარიელ სივრცეს სტრინგის თავიდან და ბოლოდან
# .replace("a", "b") - სტრინგში "a" შეცვლის "b"-ით
# .split() - ყოფს სტრინგს სიად
# .find("x") - აბრუნებს სიმბოლოს ინდექსს, თუ იპოვა
# .count("x") - დათვლის რამდენჯერ გვხვდება სიმბოლო

#  სიის ფუნქციები 
# .append(x) - სიას ბოლოში უმატებს ელემენტს
# .pop() - აშორებს ბოლო ელემენტს
# .remove(x) - აშორებს პირველ შემხვედრ ელემენტს, რომელიც ტოლია x-ს
# .insert(i, x) - ჩაამატებს ელემენტს მითითებულ ინდექსზე
# .sort() - ალაგებს სიას ზრდადობით
# .reverse() - აბრუნებს სიას უკუღმა
# .clear() - ცლის სიას
# len(list) - აბრუნებს სიის სიგრძეს

# 3) გვარის შედარება Case Insensitive
my_surname = "kiknadze"
user_surname = input("შეიყვანე შენი გვარი: ")

if my_surname.lower() == user_surname.lower():
    print("Our surnames are similar.")
else:
    print("We have different surnames.")

# 4) არაჯანსაღი საკვების ამოღება და ჯანსაღის დამატება
food = ["burger", "pizza", "chips"]
food.pop()  # ამოიღებს "chips"-ს
food.append("salad")  # დაამატებს ჯანსაღ საკვებს
print("განახლებული სია:", food)

# 5) სახელის ასოების შედარება
my_name = "nia"
user_name = input("შეიყვანე შენი სახელი: ")

# ვადარებთ პირველ და ბოლო ასოებს
if my_name[0].lower() == user_name[0].lower() and my_name[-1].lower() == user_name[-1].lower():
    print(2)
elif my_name[0].lower() == user_name[0].lower() or my_name[-1].lower() == user_name[-1].lower():
    print(1)
else:
    print(0)

#BOSS LVL
names = []

while True:
    name = input("შეიყვანე სახელი (ან დაწერე 'stop' გასასვლელად): ")
    if name.lower() == "stop":
        break
    cap_name = name.capitalize()
    names.append(cap_name)
    print("სიაში არსებული სახელები:", names)
