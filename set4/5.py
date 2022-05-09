def sms_encoding(data):
    # start writing your code here
    vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    data = data.split()
    encoded_msg = ""
    for word in data:
        consonant_present = False
        for character in word:
            if character not in vowel:
                consonant_present = True
                break
        if consonant_present:
            for character in word:
                if character not in vowel:
                    encoded_msg += character
            encoded_msg += " "
        else:
            encoded_msg += word + " "
    return encoded_msg[:-1]


data = "I love Python"
print(sms_encoding(data))
