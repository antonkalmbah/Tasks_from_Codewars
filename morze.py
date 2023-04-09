morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
         'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..'}

morse_code = '.... . -.--   .--- ..- -.. .'


def decode_morse(morse_code):
    result = ''
    morse_code_split = morse_code.split()
    print('morse_code_split', morse_code_split)
    for word in morse_code_split:
        for key, value in morse.items():
            if word == value:
                result += key

    print(result)


decode_morse(morse_code)