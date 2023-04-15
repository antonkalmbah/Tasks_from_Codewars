morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
         'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..'}

# hey jude
morse_code = '.... . -.--   .--- ..- -.. .'


def decode_morse(morse_code):
    result = ''
    morse_code_split = morse_code.split(' ')
    for word in morse_code_split:
        for key, value in morse.items():
            if word == value:
                result += key
        if word == '':
            result += ' '

    result_split = result.split()
    correct_phrase = ' '.join(result_split)

    print(correct_phrase)


decode_morse(morse_code)