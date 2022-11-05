import hashlib
import random


class WordHasher:
    def __init__(self):
        with open("nouns.txt", "r") as f:
            self.nouns = f.read().splitlines()
        with open("adjectives.txt", "r") as f:
            self.adjectives = f.read().splitlines()
        with open("verbs.txt", "r") as f:
            self.verbs = f.read().splitlines()

        self.samplers = {
            "v": lambda: self.verbs[random.randrange(len(self.verbs))],
            "a": lambda: self.adjectives[random.randrange(len(self.adjectives))],
            "n": lambda: self.nouns[random.randrange(len(self.nouns))],
            "N": lambda: str(random.randrange(1000)),
        }
        self.modes = set(list(self.samplers.keys()))

    def from_str(self, text):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()

        n = int(h[:20], 16) % len(self.nouns)
        noun = self.nouns[n]

        a = int(h[30], 16) % len(self.adjectives)
        adj = self.adjectives[a]

        v = int(h[20:30], 16) % len(self.verbs)
        verb = self.verbs[v]

        wh = f"{verb}-{adj}-{noun}"
        return wh

    def from_file(self, file):
        with open(file, "r") as f:
            text = f.read()
        return self.from_str(text)

    def sample(self, mode: str = "vanN") -> str:
        assert mode != ""
        assert all(m in self.modes for m in mode)
        parts = [self.samplers[m]() for m in mode]
        return "-".join(parts)


if __name__ == "__main__":
    whash = WordHasher()
    m = "This is a test."
    print(f"Hashing {m} = {whash.from_str(m)}")
    print(f"Hashing {m} = {whash.from_str(m)}")
    print(f"Hashing {__file__} = {whash.from_str(__file__)}")
    print(f"Hashing {__file__} = {whash.from_str(__file__)}")
    print("Default sample:", whash.sample())
    for mode in ["va", "an", "anN", "van", "vanN"]:
        print(f"  mode:{mode:<5}: {whash.sample(mode=mode)}")
