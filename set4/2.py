def encrypt_sentence(sentence: str):
    # start writing your code here
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    sentence = sentence.split(" ")
    encrypted_sentence = ""
    counter = 1
    for word in sentence:
        vowels_in_word = ""
        consonant_in_word = ""
        if counter % 2 == 0:
            for character in word:
                if character not in vowels:
                    consonant_in_word += character
                else:
                    vowels_in_word += character

            encrypted_sentence += consonant_in_word + vowels_in_word + " "
        else:
            encrypted_sentence += word[::-1] + ' '
        counter += 1
    encrypted_sentence = encrypted_sentence[:-1]
    return encrypted_sentence


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
