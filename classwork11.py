all_digits = ['!', ':', ';', ',', '.', '?', ]
string = input("type text")
total_digits = 0
for s in string:
    if s in all_digits:
        total_digits += 1
print("Totall digits->", total_digits)
