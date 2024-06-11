def count_vowels(string):
    vowels = "aeiouy"
    words = string.split()
    count = 0

    for word in words:
        vowel_count = 0
        for letter in word:
            if letter.lower() in vowels:
                vowel_count += 1
        if vowel_count >= 3:
            count += 1

    return count

a = "zalupa govno pomidor"
print(count_vowels(a))