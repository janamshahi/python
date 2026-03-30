import string
def is_pangram(text):
    text = text.lower()
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(text))
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
