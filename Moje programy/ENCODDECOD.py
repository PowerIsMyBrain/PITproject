import random

def encode_string(s):
    ascii_codes = [ord(char) for char in s]
    divider = random.randint(1, 9)
    modified_codes = []
    
    for code in ascii_codes:
        str_code = str(code)
        if str_code.startswith('0'):
            str_code = '2' + str_code[1:]
        modified_codes.append(str_code)
    
    long_string = ''.join(modified_codes)
    encoded_string = long_string + str(divider)
    encoded_integer = int(encoded_string)
    
    return encoded_integer

def decode_integer(encoded_integer):
    encoded_string = str(encoded_integer)
    divider = int(encoded_string[-1])
    encoded_string = encoded_string[:-1]
    ascii_codes = []
    
    i = 0
    while i < len(encoded_string):
        if encoded_string[i] == '2':
            code = '0' + encoded_string[i+1:i+3]
            i += 3
        else:
            if i + 4 <= len(encoded_string) and encoded_string[i+3] != '2':
                code = encoded_string[i:i+4]
                i += 4
            else:
                code = encoded_string[i:i+3]
                i += 3
        ascii_codes.append(int(code))
    
    decoded_string = ''.join(chr(code) for code in ascii_codes)
    
    return decoded_string

# Przykład użycia
test_string = "okej ja wychodzę z domu Mogę podjechać"
encoded = encode_string(test_string)
decoded = decode_integer(encoded)

print(f"Zakodowana liczba: {encoded}")
print(f"Odkodowana wiadomość: {decoded}")
print(f"Zgodność: {test_string == decoded}")
