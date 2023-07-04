# Reversed string algorithm

def reversed_string(string_input) -> str:
    str_len = len(string_input) - 1
    reversed_str = ""

    for str_index in range(str_len + 1):
        reversed_str += (string_input[str_len])
        str_len -= 1

    return reversed_str


name = "Hasmieu"

test = reversed_string(name)

print(test)
