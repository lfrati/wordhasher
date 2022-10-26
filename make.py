import nltk
from nltk.corpus import wordnet as wn
from tqdm import tqdm
import re

if __name__ == "__main__":
    nltk.download("wordnet")
    nltk.download("omw-1.4")

    only_letters = re.compile(r"^[a-zA-Z]+$")
    assert only_letters.match("apple") is not None
    assert only_letters.match("apple_2") is None

    words = {"n": set(), "v": set(), "a": set()}
    for category in words.keys():
        for n in tqdm(list(wn.all_synsets(category))):
            opts = n.lemma_names()
            for opt in opts:
                if (
                    only_letters.match(opt)
                    and len(opt) > 3
                    and len(opt) < 9
                    and opt.islower()
                ):
                    words[category].add(opt)

    words = {cat: sorted(list(ws)) for cat, ws in words.items()}

    for cat, ws in words.items():
        print(cat, len(ws))

    with open("nouns.txt", "w") as f:
        for w in words["n"]:
            f.write(w + "\n")
    with open("adjectives.txt", "w") as f:
        for w in words["a"]:
            f.write(w + "\n")
    with open("verbs.txt", "w") as f:
        for w in words["v"]:
            f.write(w + "\n")
