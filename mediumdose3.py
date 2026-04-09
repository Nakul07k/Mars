def decode(message):
    message = message.upper()
    result = ""
    for i in range(len(message)):
        shift = i + 1
        # Convert character to its ASCII value using ord()
        # Subtract 65 to map 'A' → 0, 'B' → 1, ..., 'Z' → 25
        # Apply reverse shift (decoding) and wrap using modulo 26
        char = (ord(message[i]) - 65 - shift) % 26 + 65  
        result += chr(char)
    return result


def main():
    message = input("Enter encoded message: ")
    if message.isalpha():
        print("Decoded message:", decode(message))
    else:
        print("Invalid input! Please enter alphabets only.")
    

if __name__ == "__main__":
    main()