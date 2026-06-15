# stores a dictionary of ids for each token
# there are 99 words, one padding token

vocab = {
    # Pronouns (8)
    "i": 1,
    "you": 2,
    "he": 3,
    "she": 4,
    "we": 5,
    "they": 6,
    "it": 7,
    "me": 8,

    # Verbs (24)
    "go": 9,
    "come": 10,
    "see": 11,
    "look": 12,
    "get": 13,
    "give": 14,
    "know": 15,
    "think": 16,
    "like": 17,
    "love": 18,
    "want": 19,
    "need": 20,
    "eat": 21,
    "drink": 22,
    "run": 23,
    "walk": 24,
    "play": 25,
    "read": 26,
    "write": 27,
    "open": 28,
    "close": 29,
    "help": 30,
    "find": 31,
    "use": 32,

    # Articles / Determiners (4)
    "a": 33,
    "the": 34,
    "this": 35,
    "that": 36,

    # Adjectives (15)
    "big": 37,
    "small": 38,
    "good": 39,
    "bad": 40,
    "new": 41,
    "old": 42,
    "happy": 43,
    "sad": 44,
    "fast": 45,
    "slow": 46,
    "hot": 47,
    "cold": 48,
    "easy": 49,
    "hard": 50,
    "young": 51,

    # People / Animals (15)
    "man": 52,
    "woman": 53,
    "boy": 54,
    "girl": 55,
    "friend": 56,
    "family": 57,
    "teacher": 58,
    "student": 59,
    "dog": 60,
    "cat": 61,
    "bird": 62,
    "child": 63,
    "parent": 64,
    "person": 65,
    "baby": 66,

    # Places (10)
    "house": 67,
    "school": 68,
    "room": 69,
    "park": 70,
    "store": 71,
    "city": 72,
    "road": 73,
    "place": 74,
    "home": 75,
    "garden": 76,

    # Objects (12)
    "book": 77,
    "table": 78,
    "chair": 79,
    "phone": 80,
    "door": 81,
    "car": 82,
    "food": 83,
    "water": 84,
    "ball": 85,
    "bag": 86,
    "paper": 87,
    "key": 88,

    # Time / Nature (5)
    "day": 89,
    "night": 90,
    "time": 91,
    "sun": 92,
    "tree": 93,

    # Prepositions (6)
    "in": 94,
    "on": 95,
    "at": 96,
    "to": 97,
    "from": 98,
    "with": 99,


    "<PAD>" : 0
}