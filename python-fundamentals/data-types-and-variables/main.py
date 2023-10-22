# Number data types:
an_interger: int = 5
a_float: float = 3.142
a_complex: complex = complex(5,-2) # 5 - 2j j = i in electrical engineering standards

# Boolean data types aka bool:
a_true_bool: bool = True
a_false_bool: bool = False

#String data types aka strings:
empty_string: str = ""
a_character: str = 's'
a_string: str = "game of thrones"
a_multiline_string: str = '''Hello
my name is
Suncerie Daye.'''

a_string_length: int = len(a_string)

batman = "Bruce Wayne"
print(batman[0], "is the first character")
print(batman[len(batman)-1], "is the last character")
print(batman[-1])
print(batman[2:7])
print(batman[0:8:2])
print(batman[8:0:-1])
print(batman[:8])

print("Number literals look like this:", an_interger, a_float, a_complex)
print("Bools look like this:", a_true_bool, a_false_bool)
print("Strings look like:", empty_string, a_character, a_string, a_multiline_string)