def decode(signal):

    morse_code = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '-----': '0', '--..--': ',',
        '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
        '-.--.': '(', '-.--.-': ')'
    }

    message = []

    signal = signal.replace(' / ', '   ')  # Replace " / " with 3 spaces
    words = signal.strip().split('   ')   # Split the signal into words (3 spaces = new word)

    for w in words:
        decoded_wrd = ""
        chars = w.split(' ')  # Split word into individual Morse characters (1 space = new letter)
        # Decode each Morse character
        for c in chars:
            if c in morse_code :
                decoded_wrd += morse_code [c]
            else:
                decoded_wrd += '[?]'
        message.append(decoded_wrd)

    return ' '.join(message)


signal = str(input("Enter morse code: "))
print("Decoded Message:",decode(signal))