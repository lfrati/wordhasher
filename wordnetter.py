import hashlib
from pathlib import Path
import pickle
import random

from tqdm import tqdm


class Wordnetter:
    def __init__(self):

        if not (Path.home() / ".wordnetter").exists():
            self.download()

        with open("wordnetter.pkl", "rb") as f:
            self.words = pickle.load(f)

        self.len_n = len(self.words["n"])
        self.len_v = len(self.words["v"])
        self.len_a = len(self.words["a"])

    def download(self):
        pass

    def encode(self, text):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()

        n = int(h[:20], 16)
        v = int(h[20:30], 16)
        a = int(h[30], 16)
        return self.get(n, v, a)

    def get(self, n, v, a):
        noun = self.words["n"][n % self.len_n]
        adj = self.words["a"][v % self.len_a]
        verb = self.words["v"][a % self.len_v]
        words = f"{verb}-{adj}-{noun}"
        return words

    def sample(self):

        n = random.randint(1, 2**32)
        v = random.randint(1, 2**32)
        a = random.randint(1, 2**32)
        words = self.get(n, v, a)
        words = words + f"-{random.randint(1,999)}"

        return words


#%%

wnetter = Wordnetter()
print(wnetter.encode("This is a test2"))
print(wnetter.sample())
print(wnetter.sample())

N = 10_000_000
print(N, len(set([wnetter.sample() for _ in tqdm(range(N))])))
