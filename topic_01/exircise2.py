#Додавання рядків:

text1 = "Hello, "
text2 = "world!"
result = text1 + text2
print(result)

#Визначення кількості входжень підрядка в рядок:
text = "Hello world. Hello my future dreams!"
substring = "Hello"
count = text.count(substring)
print(count)

#Заміна тексту
text = "change word"
new_text = text.replace("word", "world")
print(new_text)


#Перетворення на маленькі літери:
text = "HELLO WORLD"
lowercase_text = text.lower()
print(lowercase_text)

#Перевірка, чи починається рядок з певного слова:
text = "Start speak with u"
starts_with_word = text.startswith("Start")
print(starts_with_word)


#Перевірка, чи закінчується рядок певним словом:
text = "Start speak with u"
ends_with_word = text.endswith("u")
print(ends_with_word)

#Розділення рядка на слова:
text = "Hello my world"
words = text.split()
print(words)

#Пошук підрядка у тексті:
text = "My name is Artem"
substring = "Artem"
found = substring in text
print(found)

#Визначення довжини рядка:
text = "Life"
length = len(text)
print(length)

#Вилучення пробілів з початку і кінця рядка:
text = "   Hello world   "
trimmed_text = text.strip()
print(trimmed_text)

#Повторення рядка:
text = "Repeat "
repeated_text = text * 3
print(repeated_text)

#Форматування рядка:
name = "Artem"
age = 18
formatted_text = f"My name is  {name} . I have {age} years old."
print(formatted_text)

#Видалення символу з рядка:
text = "delete 'this' symbol"
removed_char_text = text.replace("'", "")
print(removed_char_text)

#Перетворення числа в рядок:
number = 18
text = str(number)
print(text)

#Визначення позиції підрядка у тексті:
text = "just free time"
substring = "time"
position = text.find(substring)
print(position)

#Перетворення рядка у список символів:
text = "Line"
char_list = list(text)
print(char_list)

#Переведення першої літери у велику:
text = "my congratulations"
capitalized_text = text.capitalize()
print(capitalized_text)

#Розділення рядка на підрядки за роздільником:
text = "hello world, my name is Artem."
substrings = text.split(",")
print(substrings)

#Перевірка, чи складається рядок лише з букв:
text = "Only letters"
is_alpha = text.isalpha()
print(is_alpha)

#Перевірка, чи складається рядок лише з цифр:
text = "12345"
is_digit = text.isdigit()
print(is_digit)

#Перевірка, чи складається рядок лише з пробілів:
text = "     "
is_whitespace = text.isspace()
print(is_whitespace)

#Перевірка, чи починається рядок цифрою:
text = "42 is the answer"
starts_with_digit = text[0].isdigit()
print(starts_with_digit)


#Визначення, чи є рядок числом з плаваючою точкою:
text = "3.14"
is_float = text.replace(".", "", 1).isdigit()

#Перетворення на великі літери
text = "Великі літери"
uppercase_text = text.upper()
print(uppercase_text)
print(is_float)