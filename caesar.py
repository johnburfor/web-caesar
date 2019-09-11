def rotate_string(text,rot):

    output = ""
    for i in range(0,len(text)):
        output = output + rotate_character(text[i],rot)

    return output

def alphabet_position(users_letter):

    alphabet = []
    for i in range(97,123):
        alphabet.append(chr(i))

    for i in range(0,len(alphabet)):
        current = alphabet[i]
        if users_letter == current.lower():
            return i

def rotate_character(char, rot):

    alphabet = []
    for i in range(97,123):
        alphabet.append(chr(i))

    if char.isalpha():
        new_position = alphabet_position(char) + int(rot)
        new_position %= 26

    if char.isupper():
        current = alphabet[new_position]
        return current.upper()
    elif char.islower():
        return alphabet[new_position]
    else:
        return char
