def check_palindrome(word):
    word2 = word[len(word) // 2:]
    word = word[::-1]
    word = word[len(word) // 2:]
    if word2 == word:
        return True
    else:
        return False
    # Remove pass and write your logic here


status = check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
