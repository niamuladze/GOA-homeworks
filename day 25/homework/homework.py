
# რა არის def ფუნქცია და მისი სტრუქტურა


# def — ეს არის სიტყვა, რომლითაც იწყება ფუნქციის აღწერა.
# ფუნქცია ქმნის კოდს, რომელსაც შეგვიძლია რამდენჯერმე გამოვიყენოთ,
# უბრალოდ მისი სახელით მივმართავთ.

# def ფუნქციის_სახელი(პარამეტრები): მოქმედებები, return შედეგი

def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8


#  ორი ტექსტის შეერთება

def combine_texts(text1, text2):
    return text1 + text2

print(combine_texts("Hello", "World"))  # Output: HelloWorld


# ტექსტის გამრავლება

def repeat_text(text, times):
    return text * times

print(repeat_text("Hi", 3))  # Output: HiHiHi


#  f-სტრიქონით მისალმება

def greet(name):
    return f"გამარჯობა, {name}!"

print(greet("ზუკა"))  # Output: გამარჯობა, ზუკა!


#  სიტყვების ჩამონათვალის f-სტრიქონით ფორმატირება

def format_words(words):
    return f"{words[0]}, {words[1]} და {words[2]}"

print(format_words(["ლომი", "ვეფხვი", "დათვი"]))  # Output: ლომი, ვეფხვი და დათვი
