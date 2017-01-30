import string


def alphabet_position(letter):
    alphlow = string.ascii_lowercase
    alphup = string.ascii_uppercase
    for i in range(26):
        if letter == alphlow[i] or letter == alphup[i]:
            return i

def rotate_character(char,rot):
    alphlow = string.ascii_lowercase
    alphup = string.ascii_uppercase
    if not char.isalpha():
        return char
    newpos = (int(alphabet_position(char) + int(rot)) % 26)
    if char in alphlow:
        newchar = alphlow[newpos]
    if char in alphup:
        newchar = alphup[newpos]
    return newchar

def encrypt(text,rot):
    newtext = ''
    for ltr in text:
        newltr = rotate_character(ltr,rot)
        newtext += newltr
    return newtext
