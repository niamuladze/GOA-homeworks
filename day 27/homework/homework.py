# 1) ფუნქცია, რომელიც მიიღებს სტრინგს და დააბრუნებს დიდ ასოებში
def to_upper(text):
    return text.upper()

# 2) მომხმარებელს შემოატანინეთ სახელი და გამოიტანეთ მისი პირველი ასო Upper Case-ში
name = input("შეიყვანეთ თქვენი სახელი: ")
print("სახელის პირველი ასო Upper Case-ში:", name[0].upper())

# 3) ცვლადი სადაც შევიყვანთ წინადადებას და მოძებნით სიტყვას
sentence = "მე მიყვარს პროგრამირება და სწავლა."
search_word = "პროგრამირება"
if search_word in sentence:
    print(f"სიტყვა '{search_word}' მოიძებნა წინადადებაში.")
else:
    print(f"სიტყვა '{search_word}' არ მოიძებნა წინადადებაში.")

# 4) ფუნქცია რომელიც მიიღებს 2 არგუმენტს და დაუმუშავებს
def combine_words(word1, word2):
    return word1.upper() + word2.lower()

# გამოსაყენებლად:
first = "Hello"
second = "WORLD"
print("შედეგი:", combine_words(first, second))

# 5) დღეს ნასწავლი მეთოდების 5-5 მაგალითი:

# .upper() მეთოდის 5 მაგალითი:
print("\n.upper() მეთოდის მაგალითები:")
print("python".upper())
print("გამარჯობა".upper())
print("hello world".upper())
print("text123".upper())
print("საქართველო".upper())

# .lower() მეთოდის 5 მაგალითი:
print("\n.lower() მეთოდის მაგალითები:")
print("PYTHON".lower())
print("GAMARJOBA".lower())
print("HELLO WORLD".lower())
print("TEXT123".lower())
print("SAKARTVELO".lower())

# სტრინგის ინდექსაციის 5 მაგალითი:
print("\nსტრინგის ინდექსაციის მაგალითები:")
sample_text = "Programming"
print(sample_text[0])   # P
print(sample_text[1])   # r
print(sample_text[2])   # o
print(sample_text[3])   # g
print(sample_text[4])   # r

# სტრინგში სიტყვის ძიების 5 მაგალითი:
print("\nსტრინგში სიტყვის ძიების მაგალითები:")
text = "მე ვსწავლობ პროგრამირებას და მიყვარს ახალი პროექტები."
print("პროგრამირებას" in text) # True
print("პროექტი" in text)        # False
print("ახალი" in text)          # True
print("ვსწავლობ" in text)       # True
print("პროგრამირება" in text)   # False

# ორი სტრინგის გაერთიანების 5 მაგალითი:
print("\nორი სტრინგის გაერთიანების მაგალითები:")
print("Hello".upper() + "world".lower())
print("Python".upper() + "rocks".lower())
print("Good".upper() + "Morning".lower())
print("Fast".upper() + "Code".lower())
print("Learn".upper() + "Programming".lower())
