def encode(message):
    count = 1
    message += " "
    encoded_message = ""
    for i in range(0, len(message) - 1):
        if message[i] == message[i + 1]:
            count += 1
        else:
            encoded_message += str(count) + message[i]
            count = 1
    return encoded_message

    # Remove pass and write your logic here


# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
