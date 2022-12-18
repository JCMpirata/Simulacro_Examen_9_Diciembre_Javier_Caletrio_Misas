def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    substrings = {}

    for i in range(len(string)):
        if string[i] in vowels:
            for j in range(i + 1, len(string) + 1):
                substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
            kevin_score = sum(substrings.values())
            print(substrings)