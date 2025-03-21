# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input_binary_string = "01001001 00100000 01110111 01100101 01101110 01110100 00100000 01110100 01101111 00100000 01110100 01101000 01100101 00100000 01110011 01110100 01101111 01110010 01100101 00100000 01100001 01101110 01100100 00100000 01100001 01110100 01100101 00100000 01100001 00100000 01100100 01101111 01100111"


def numberToASCII(number):
    try:
        # Return the ASCII character for the number
        return chr(number)  # Converts the number to its ASCII character
    except ValueError:
        print(f"Value {number} is out of ASCII range")
        return ''


def separateBinary(input_binary):
    # Remove any spaces and make sure the binary string length is a multiple of 8
    input_binary = input_binary.replace(' ', '')

    # Create a list with 8-bit chunks
    binary_chunks = [input_binary[i:i + 8] for i in range(0, len(input_binary), 8)]

    return binary_chunks


def binaryToNumber(input_binary, text_bool):
    binary_chunks = separateBinary(input_binary)
    output_string = ""
    for chunk in binary_chunks:
        value = 0
        for i in range(8 - 1, -1, -1):
            if chunk[8 - 1 - i] == '1':
                value += 2 ** i
        if text_bool:
            output_string += numberToASCII(value) + ""
        else:
            output_string += str(value) + " "
    return output_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(binaryToNumber(input_binary_string, True))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
