alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()"

def find_char_alphabet_lower(string_to_find, current_index):
    for j in range(26):
        if string_to_find[current_index] == alphabet_lower[j]:
            return alphabet_lower[j]
    return -1

def find_char_alphabet_upper(string_to_find, current_index):
    for j in range(26):
        if string_to_find[current_index] == alphabet_upper[j]:
            return alphabet_upper[j]
    return -1

def find_char_digits(string_to_find, current_index):
    for j in range(10):
        if string_to_find[current_index] == digits[j]:
            return digits[j]
    return -1

def find_char_symbols(string_to_find, current_index):
    for j in range(10):
        if string_to_find[current_index] == symbols[j]:
            return symbols[j]
    return -1



password_test = "hH78%GJY675E76$*f87&6"
len_password_test = len(password_test)


john_ripper = ""
for i in range(len_password_test):
    if password_test[i] in alphabet_lower:
        john_ripper = john_ripper + find_char_alphabet_lower(password_test, i)
    elif password_test[i] in alphabet_upper:
        john_ripper = john_ripper + find_char_alphabet_upper(password_test, i)
    elif password_test[i] in digits:
        john_ripper = john_ripper + find_char_digits(password_test, i)
    elif password_test[i] in symbols:
        john_ripper = john_ripper + find_char_symbols(password_test, i)

print(f'''Original: {password_test}
John Ripper: {john_ripper}''')
        
