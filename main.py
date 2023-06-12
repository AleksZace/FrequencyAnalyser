


def frequencyAnaliser(cipherText):
    dictionaryForEnglishFrequencyAnalysics = {
    'E': 21912, 'T': 16587, 'A': 14810, 'O': 14003, 'I': 13318, 'N': 12666,
    'S': 11450, 'R': 10977, 'H': 10795, 'D': 7874, 'L': 7253, 'U': 5246,
    'C': 4943, 'M': 4761, 'F': 4200, 'Y': 3853, 'W': 3819, 'G': 3693,
    'P': 3316, 'B': 2715, 'V': 2019, 'K': 1257, 'X': 315, 'Q': 205,
    'J': 188, 'Z': 128, 'e': 21912, 't': 16587, 'a': 14810, 'o': 14003,
    'i': 13318, 'n': 12666, 's': 11450, 'r': 10977, 'h': 10795, 'd': 7874,
    'l': 7253, 'u': 5246, 'c': 4943, 'm': 4761, 'f': 4200, 'y': 3853,
    'w': 3819, 'g': 3693, 'p': 3316, 'b': 2715, 'v': 2019, 'k': 1257,
    'x': 315, 'q': 205, 'j': 188, 'z': 128
    }
    dictionaryForCipherText  = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
    'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 0,
    'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
    't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, ' ': 0
    }
    for char in cipherText:
        if char in dictionaryForCipherText:
            dictionaryForCipherText[char] += 1

    max_freq_char = max(dictionaryForEnglishFrequencyAnalysics, key=dictionaryForEnglishFrequencyAnalysics.get)
    print(max_freq_char)
    max_freq_char2 = max(dictionaryForCipherText, key=dictionaryForCipherText.get)
    print(max_freq_char2)

    key = ord(max_freq_char2)-ord(max_freq_char)
    asciibet = "!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 
    print(key)
frequencyAnaliser("KSDFSDF SF IOSDF JSDFJ SUHDUFHDSI F")


