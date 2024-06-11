def words_starts_a(word_list):
    filtered_list = list(filter(lambda word: word.lower().startswith('a') or word.lower().startswith('а'), word_list))
    return filtered_list


words = ["Apple", "телефон", "турникет", "ancient", "анекдот"]
print(words_starts_a(words))