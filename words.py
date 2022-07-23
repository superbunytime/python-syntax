def print_upper_words(words):
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

'''insightful comment'''

def print_e(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

'''I feel like the triple quotes really de-emphasizes things, like when you use hand quotes in sarcasm
'''

print_e(["hello", "hey", "goodbye", "yo", "yes", "eeesh"])

def print_w(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_w(["hello", "hey", "goodbye", "yo", "yes", "eeesh", "dog", "goat"],{"d", "g"})

'''be sure to make more insightful comments when working with code that is more complex than writing 3 little functions'''