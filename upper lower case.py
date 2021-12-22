char = "D"
upper_char =char.isupper()

# lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# uper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
#              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# ========================================================
# if char in lower_case:
#     print(char + " is in lower case")
# elif char in uper_case:
#     print(char + " is in uper case")
# ========================================================
# print(char, upper_char)
# ========================================================
# if char == upper_char:
#     print(char + " is in uppercase")
# else:
#     print(char + " is in lowercase")
# ========================================================
print(upper_char)
if upper_char == True:
    print(char + " is in uppercase")
else:
    print(char + " is in lowercase")
    
# ========================================================

if char.isupper():
    print(char, "is uppercase")
else:
    print(char, "is lowercase")