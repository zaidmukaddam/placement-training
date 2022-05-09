def max_frequency_word_counter(data: str):
    word = ""
    frequency = 0

    # start writing your code here
    # Populate the variables: word and frequency

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    # print(word,frequency)
    frequency_dict = {}
    data = data.lower()
    data = data.split()
    for word in data:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    max_word = ""
    max_frequency = 0
    for word, frequency in frequency_dict.items():
        if max_frequency == frequency and len(word) > len(max_word):
            max_word = word

        if frequency > max_frequency:
            max_word = word
            max_frequency = frequency
    print(max_word, max_frequency)


# Provide different values for data and test your program.
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
