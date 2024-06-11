def list_words_to_str(words):
    a = words.split()
    for k in a:
        yield k

words = "aqua fish sunset rain mouse keyboard"

for k in list_words_to_str(words):
    print(k)