from datasets import load_dataset
import re

def getScents(numStories, startStory):
    ds = load_dataset("roneneldan/TinyStories")

    print("DATASET SPECS:")
    print(ds)
    print(ds["train"][0]["text"])

    numscents = 0
    with open("train.txt", "w") as f:

        for i in range(startStory, startStory+numStories+1):

            story = ds["train"][i]["text"]

            sentences = re.split(r"[.!?]+", story)
            
            for sentence in sentences:
                numscents += 1
                sentence = sentence.strip().lower()
                # get rid of punctuation
                sentence = re.sub(r"[^a-z ]", "", sentence.lower())
                sentence = " ".join(sentence.split())

                if sentence:
                        f.write(sentence + '\n')

            if (i - startStory) % 100 == 0:
                print(f"{i} stories added to train.txt")
    print("Number of scentences added to train.txt: " + str(numscents))

getScents(100000, 0)