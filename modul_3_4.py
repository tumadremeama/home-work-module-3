def single_root_words(root_word, *other_words):
    same_words = []


    for words in other_words:
        words_lower = words.lower()
        if words_lower in words_lower or words_lower in root_word_lower:
            same_words.append(words)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
