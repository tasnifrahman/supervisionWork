def find_anagrams(word, words_list):
    sorted_word = ''.join(sorted(word))
    anagrams = [w for w in words_list if ''.join(sorted(w)) == sorted_word]
    return anagrams


word = input("Enter a word: ")
words_list = input("Enter a list of words : ").split()

anagrams = find_anagrams(word, words_list)

print(f'Anagrams of "{word}" are: {anagrams}')
