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

        else:
            for j in range(i + 1, len(string) + 1):
                substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
            stuart_score = sum(substrings.values())

    if kevin_score > stuart_score:
        print("Kevin es el ganador con ", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart es el ganador con ", stuart_score)
    else:
        print("Empate")

        