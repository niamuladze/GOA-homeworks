# 1) ფუნქცია, რომელიც სახელს upper case-ში გადაიყვანს
def upper_case_name(name):
    result = ''
    for letter in name:
        result += letter.upper()
    return result

# 2) ფუნქცია, რომელიც სიას გადაივლის და თითოეულ ელემენტს დაბეჭდავს
def print_list_elements(my_list):
    for element in my_list:
        print(element)

# გამოსაყენებლად:
name_input = "Nia"
print("სახელი Upper Case-ში:", upper_case_name(name_input))

print("\nსიის ელემენტები:")
sample_list = ["apple", "banana", "cherry"]
print_list_elements(sample_list)
