from preloaded import MORSE_CODE # this module is a codewars module

def decode_morse(morse_code):
    # you can use the preloaded MORSE_CODE dictionary:
    # letter = MORSE_CODE[morse]
    # For example: 
    #   MORSE_CODE['.-'] = 'A'
    #   MORSE_CODE['--...'] = '7'
    #   MORSE_CODE['...-..-'] = '$'
    morse_code = morse_code.strip()
    alpha = morse_code.split(' ')
    word = ''
    i = 0
    while i < len(alpha):
        if alpha[i]=='':
            word += ' '
            i += 2
            continue
        word += MORSE_CODE[alpha[i]]
        i += 1
        
    return word
