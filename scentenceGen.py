"""
SLM training data generator.
Generates ~1000 natural, meaningful sentences from controlled templates.
Vocab stays under 115 words.
Change NUM_SENTENCES.
"""

import random

# ── Change this number ────────────────────────────────────────────────────────
NUM_SENTENCES = 1000

# ── Semantic word groups ───────────────────────────────────────────────────────
# These are carefully chosen so only sensible combinations are made

SUBJECT_PRONOUNS  = ["i", "you", "he", "she", "we", "they"]

# People who can DO things
PEOPLE = ["the boy", "the girl", "the man", "the woman", "the child",
          "the baby", "the student", "the teacher", "the parent", "the friend"]

# Animals — limited verb set
ANIMALS = ["the dog", "the cat", "the bird"]

# Places you travel TO or are IN
PLACES = ["the park", "the garden", "the store", "school", "home",
          "the house", "the room", "the city"]

# Things you can hold / use / find
HOLDABLE = ["the book", "the bag", "the key", "the phone", "the ball", "the paper"]

# Things you put ON a surface
ON_SURFACE = ["the book", "the bag", "the key", "the phone", "the ball", "the paper", "the food", "the water"]

# Surfaces
SURFACES = ["the table", "the chair"]

# Adjectives paired with nouns they actually describe well
ADJ_PERSON = ["happy", "sad", "young", "old", "fast", "slow", "good"]
ADJ_THING  = ["big", "small", "new", "old", "good", "bad", "easy", "hard", "cold", "hot"]
ADJ_PLACE  = ["big", "small", "good", "old", "new"]

def make_sentences():
    S = []

    # ── 1. PRONOUN goes/walks/runs/comes to PLACE ─────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for verb in ["go", "walk", "run", "come"]:
            for place in PLACES:
                prep = "to" if place not in ["home", "school"] else "to"
                S.append(f"{subj} {verb} to {place}")
        S.append(f"{subj} walk home from school")
        S.append(f"{subj} run home from school")
        S.append(f"{subj} come home from school")
        S.append(f"{subj} go home after school")

    # ── 2. PERSON goes/walks/runs to PLACE ────────────────────────────────────
    for person in PEOPLE:
        for verb in ["goes", "walks", "runs", "comes"]:
            for place in ["the park", "the store", "school", "home", "the garden"]:
                S.append(f"{person} {verb} to {place}")
        S.append(f"{person} walks home from school")
        S.append(f"{person} comes home from school")

    # ── 3. ANIMAL runs/walks/plays in PLACE ───────────────────────────────────
    for animal in ANIMALS:
        for verb, places in [
            ("runs",  ["the park", "the garden", "the house"]),
            ("walks", ["the park", "the garden"]),
            ("plays", ["the park", "the garden", "the room"]),
        ]:
            for place in places:
                S.append(f"{animal} {verb} in {place}")

    # ── 4. PRONOUN eats / drinks ──────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        S.append(f"{subj} eat good food at home")
        S.append(f"{subj} eat hot food at home")
        S.append(f"{subj} drink cold water at home")
        S.append(f"{subj} eat breakfast at home")
        S.append(f"{subj} eat lunch at school")

    # ── 5. PERSON eats / drinks ───────────────────────────────────────────────
    for person in PEOPLE:
        S.append(f"{person} eats good food at home")
        S.append(f"{person} drinks cold water")
        S.append(f"{person} eats at home")
        S.append(f"{person} eats at school")

    # ── 6. PRONOUN reads / writes ─────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        S.append(f"{subj} read a good book")
        S.append(f"{subj} read at home")
        S.append(f"{subj} read at school")
        S.append(f"{subj} write in a book")
        S.append(f"{subj} write on the paper")

    # ── 7. PERSON reads / writes ──────────────────────────────────────────────
    for person in PEOPLE:
        S.append(f"{person} reads a good book")
        S.append(f"{person} reads at school")
        S.append(f"{person} writes on the paper")
        S.append(f"{person} reads to the child")

    # ── 8. PRONOUN plays ──────────────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        S.append(f"{subj} play in the park")
        S.append(f"{subj} play in the garden")
        S.append(f"{subj} play with the ball")
        S.append(f"{subj} play with the dog")

    # ── 9. PERSON plays ───────────────────────────────────────────────────────
    for person in ["the boy", "the girl", "the child", "the student", "the baby"]:
        S.append(f"{person} plays in the park")
        S.append(f"{person} plays in the garden")
        S.append(f"{person} plays with the ball")
        S.append(f"{person} plays with the dog")
        S.append(f"{person} plays with the cat")

    # ── 10. PRONOUN sees / looks at ───────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["the dog", "the cat", "the bird", "the book", "the sun"]:
            S.append(f"{subj} see {obj}")
        for obj in ["the dog", "the cat", "the bird", "the book"]:
            S.append(f"{subj} look at {obj}")
        S.append(f"{subj} see a bird in the tree")
        S.append(f"{subj} see the dog in the park")

    # ── 11. PRONOUN likes / loves ─────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["the dog", "the cat", "the bird"]:
            S.append(f"{subj} love {obj}")
            S.append(f"{subj} like {obj}")
        for place in ["the park", "the garden", "home", "school"]:
            S.append(f"{subj} love {place}")
            S.append(f"{subj} like {place}")
        for verb in ["read", "walk", "run", "play", "eat"]:
            S.append(f"{subj} like to {verb}")
            S.append(f"{subj} love to {verb}")

    # ── 12. PERSON loves ──────────────────────────────────────────────────────
    for person in PEOPLE:
        for obj in ["the dog", "the cat", "the bird"]:
            S.append(f"{person} loves {obj}")
        for place in ["the park", "the garden", "home"]:
            S.append(f"{person} loves {place}")

    # ── 13. PRONOUN wants / needs ─────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["a new book", "a new phone", "a new bag", "the key", "the ball"]:
            S.append(f"{subj} want {obj}")
            S.append(f"{subj} need {obj}")
        for verb in ["go home", "eat", "read", "play", "run"]:
            S.append(f"{subj} want to {verb}")
            S.append(f"{subj} need to {verb}")

    # ── 14. PRONOUN finds / gets / uses ───────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in HOLDABLE:
            S.append(f"{subj} find {obj}")
            S.append(f"{subj} get {obj}")
            S.append(f"{subj} use {obj}")

    # ── 15. PRONOUN opens / closes ────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["the door", "the bag", "the book"]:
            S.append(f"{subj} open {obj}")
            S.append(f"{subj} close {obj}")

    # ── 16. PRONOUN helps ─────────────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["the child", "the student", "the teacher",
                    "the baby", "the old man", "my friend"]:
            S.append(f"{subj} help {obj}")

    # ── 17. PERSON helps ──────────────────────────────────────────────────────
    helper_pairs = [
        ("the teacher", "the student"),
        ("the parent",  "the child"),
        ("the friend",  "the man"),
        ("the woman",   "the baby"),
        ("the man",     "the woman"),
        ("the student", "the teacher"),
    ]
    for helper, helped in helper_pairs:
        S.append(f"{helper} helps {helped}")

    # ── 18. PRONOUN gives ─────────────────────────────────────────────────────
    for subj in SUBJECT_PRONOUNS:
        for obj in ["the book", "the key", "the bag", "the ball", "the phone"]:
            S.append(f"{subj} give you {obj}")
            S.append(f"{subj} give me {obj}")

    # ── 19. PERSON gives ──────────────────────────────────────────────────────
    for giver, receiver, thing in [
        ("the teacher", "the student", "a book"),
        ("the parent",  "the child",   "food"),
        ("the friend",  "the boy",     "the ball"),
        ("the woman",   "the baby",    "food"),
        ("the man",     "the woman",   "the key"),
    ]:
        S.append(f"{giver} gives {receiver} {thing}")

    # ── 20. THING is on/in SURFACE/PLACE ─────────────────────────────────────
    for thing in ON_SURFACE:
        for surface in SURFACES:
            S.append(f"{thing} is on {surface}")
        for place in ["the bag", "the room", "the house"]:
            S.append(f"{thing} is in {place}")

    # ── 21. PERSON / ANIMAL is in/at PLACE ───────────────────────────────────
    for person in PEOPLE:
        for place, prep in [("school", "at"), ("home", "at"), ("the park", "in"),
                            ("the room", "in"), ("the store", "at"), ("the garden", "in")]:
            S.append(f"{person} is {prep} {place}")
    for animal in ANIMALS:
        for place, prep in [("the garden", "in"), ("the room", "in"),
                            ("the house", "in"), ("the park", "in")]:
            S.append(f"{animal} is {prep} {place}")
    S.append("the bird is in the tree")

    # ── 22. NOUN is ADJ ───────────────────────────────────────────────────────
    for person in PEOPLE:
        for adj in ADJ_PERSON:
            S.append(f"{person} is {adj}")
    for animal, adjs in [("the dog", ["big", "fast", "happy", "good"]),
                         ("the cat", ["small", "slow", "happy", "old"]),
                         ("the bird", ["small", "fast", "young"])]:
        for adj in adjs:
            S.append(f"{animal} is {adj}")
    for thing, adjs in [("the book",  ["good", "new", "old", "easy", "hard"]),
                        ("the food",  ["good", "hot", "cold", "bad"]),
                        ("the water", ["cold", "good"]),
                        ("the road",  ["long", "hard", "bad"]),
                        ("the house", ["big", "old", "good", "new"]),
                        ("the park",  ["big", "good", "old"])]:
        for adj in adjs:
            if adj in ["long"] and "long" not in ["big","small","good","bad","new","old","happy","sad","fast","slow","hot","cold","easy","hard","young"]:
                continue
            S.append(f"{thing} is {adj}")

    # ── 23. it is … ──────────────────────────────────────────────────────────
    for adj in ["good", "cold", "hot", "bad", "hard", "easy"]:
        S.append(f"it is {adj} today")
        S.append(f"it is {adj} at night")
        S.append(f"it is {adj} at home")
    for adj, noun in [("good","day"), ("cold","night"), ("hot","day"),
                      ("bad","day"), ("new","day"), ("good","time"),
                      ("hard","time"), ("good","place"), ("bad","place")]:
        S.append(f"it is a {adj} {noun}")

    # ── 24. nature ────────────────────────────────────────────────────────────
    S += [
        "the sun is hot today",
        "the sun is bright today",
        "the tree is big and old",
        "a big tree is in the park",
        "a big tree is in the garden",
        "the bird sits in the tree",
        "a bird sits in the tree",
    ]

    # ── 25. family ────────────────────────────────────────────────────────────
    S += [
        "the family eats dinner at home",
        "the family walks in the park",
        "the family loves their home",
        "the family comes home together",
        "the mother loves her baby",
        "the father helps his child",
        "the parent reads to the child",
        "the family plays in the garden",
        "the family runs in the park",
    ]

    return S


def generate(n: int, output_path: str = "train.txt", seed: int = None):
    if seed is not None:
        random.seed(seed)

    pool = list(dict.fromkeys(make_sentences()))  # deduplicate
    print(f"Total unique sentences in pool: {len(pool)}")

    if n > len(pool):
        print(f"Warning: only {len(pool)} unique sentences. Writing all.")
        result = list(pool)
    else:
        result = random.sample(pool, n)

    random.shuffle(result)
    with open(output_path, "w") as f:
        for s in result:
            f.write(" ".join(s.split()[:-1]) + "\n")
    print(f"Wrote {len(result)} sentences to '{output_path}'")



if __name__ == "__main__":
    generate(NUM_SENTENCES, output_path="train.txt")