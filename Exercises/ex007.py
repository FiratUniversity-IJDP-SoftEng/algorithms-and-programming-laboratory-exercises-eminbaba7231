# Your Student ID:230543008
# Your Name and Surname:Emin Talha Celik
input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1
for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")
