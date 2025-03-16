# Your Student ID: 230543008
# Your Name and Surname:Emin Talha Celik
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
