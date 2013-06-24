
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def neighborhood(wordlist, word):
    for (slot, ltr) in enumerate(word):
        for change_to in ALPHABET:
            if ltr != change_to:
                new_word = list(word)
                new_word[slot] = change_to
                new_word = "".join(new_word)
                if new_word in wordlist:
                    yield new_word

