

def standard_wordlist():
    words = set()
    with open('/usr/share/dict/words', 'r') as f:
        for l in f:
            words.add(l.rstrip())
    return words


