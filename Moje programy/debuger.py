import random

def make_token(integer):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    ]
    token = ''
    for i, l in enumerate(str(integer)):
        if random.randrange(1,4) == 3:
            token += random.choice(letters)+l
        else:
            token += l
    return token

def change_token_for_int(integer_or_token):
    
    token = False
    new_in_integer_str = ''
    for i in range(len(str(integer_or_token))):
        # print(i)
        try:
            x = int(str(integer_or_token)[i])
            new_in_integer_str += f'{str(integer_or_token)[i]}'
        except Exception as e:
            # print(f'Ocurrent Error: {e} dla {i}')
            token = True
    # print(token, new_in_integer_str)
    if token:
        return int(new_in_integer_str)
    else:
        integer = integer_or_token
        return int(integer)

def encode_string(s, pin=None):

    if pin is None:
        pin = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    if len(str(pin)) != 4:
        return 0
    correct_pin = str(pin)
    s = f'#{s}{correct_pin}#'
    # print(f"String with delimiters: {s}")
    
    ascii_codes = [ord(char) for char in s]
    # print(f"ASCII codes: {ascii_codes}")
    
    divider = random.randint(3, 9)
    # print(f"Divider: {divider}")
    
    modified_codes = []

    for code in ascii_codes:
        if len(str(code)) == 1:
            code = f'{divider}{divider}{code}'
        elif len(str(code)) == 2:
            code = f'{divider}{code}'
        else:
            code = str(code)
        modified_codes.append(code)

    long_string = ''.join(modified_codes)
    # print(f"Long string: {long_string}")
    
    int_code = int(long_string) // divider
    # print(f"Integer code divided: {int_code}")
    
    encoded_string = str(int_code) + str(divider)
    # print(f"Encoded string with divider: {encoded_string}")
    
    encoded_integer = int(encoded_string)
    # print(f"Encoded integer: {encoded_integer}")
    
    return {
        "EI":encoded_integer,
        "CS":correct_pin,
        "TK": make_token(encoded_integer)
            }

def decode_integer(encoded_integer, pin):
    encoded_integer = change_token_for_int(encoded_integer)
    pin = str(pin)
    if encoded_integer == 0 or len(pin) != 4:
        return 'Brak autoryzacji!'
    
    encoded_string = str(encoded_integer)
    # print(f"Encoded string from integer: {encoded_string}")
    
    divider = int(encoded_string[-1])
    encoded_string = encoded_string[:-1]
    # print(f"Divider: {divider}")
    # print(f"Encoded string without divider: {encoded_string}")

    int_code = int(encoded_string) * divider
    # print(f"Integer code multiplied: {int_code}")
    
    long_string = str(int_code)
    # print(f"Long string: {long_string}")
    
    modified_codes = []
    a = 0
    for i in range(len(long_string)):
        if a == 3:
            tree_part_str = long_string[i:i+3]
            if tree_part_str.startswith(str(divider)):
                tree_part_str = tree_part_str[1:]
            modified_codes.append(tree_part_str)
            a = 0
        a += 1
    # print(f"Modified codes: {modified_codes}")
    
    ascii_codes = [int(a) for a in modified_codes]
    # print(f"ASCII codes: {ascii_codes}")
    
    decoded_string_with_pin = ''.join(chr(code) for code in ascii_codes)
    # Poprawne usuwanie delimiterów
    if decoded_string_with_pin[0] == '#' and decoded_string_with_pin[-1] == '#':
        decoded_string_with_pin = decoded_string[1:-1]
    # print(f"Decoded string with pin: {decoded_string_with_pin}")
    decoded_string = decoded_string_with_pin[:-5]
    decoded_pin = decoded_string_with_pin[-5:-1]
    # print(f"Decoded pin: {pin, decoded_pin}")
    if len(pin) != 4:
        return 'Brak autoryzacji!'
    if pin != decoded_pin:
        return 'Brak autoryzacji!'
    return decoded_string

if __name__ == "__main__":
    while True:
        rout = input('''[e] - encode\n[d] - decode\n\n>>> ''')
        if rout == 'e':
            pin=input('czy chcesz ustawić swój pin? (t/n): ')
            if pin.startswith('t'):
                pin = input('podaj czterocyfrowy pin: ')
                print(f'pin: {pin} został zapisany')
            else:
                pin = None
            encoded = encode_string(
                input("Podaj widomość: "),
                pin
                )
            print(f"Encoded: {encoded}")
            break
        elif rout == 'd':
            decoded = decode_integer(
                input('podaj liczbę lub token: '), input('Podaj pin: '))
            print(f"Decoded: {decoded}")
            break
        else:
            print('Nieznana komenda')
