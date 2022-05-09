# lex_auth_012693825794351104168

def find_common_characters(msg1, msg2):
    common_characters = ""
    msg1, msg2 = msg1.replace(" ", ""), msg2.replace(" ", "")
    for i in msg1:
        if i in msg2:
            if i in common_characters:
                continue
            else:
                common_characters += i
    if not common_characters:
        return -1
    return common_characters  # Remove pass and write your logic here


# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
