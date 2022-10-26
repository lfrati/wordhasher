import hashlib
from pathlib import Path
import random
import shutil

import requests
from tqdm import tqdm


class Wordnetter:
    def __init__(self):

        self.storage = Path().home() / ".wordnetter"
        self.filenames = [
            self.storage / name for name in ["nouns.txt", "adjectives.txt", "verbs.txt"]
        ]

        if not self.storage.exists():
            self.install()

        # to make the linter shut up
        self.nouns = []
        self.verbs = []
        self.adjectives = []
        for file in self.filenames:
            name = file.stem
            with open(file, "r") as f:
                words = f.read().splitlines()
                setattr(self, name, words)

    def install(self):

        print("Storing data in ", self.storage)
        if not self.storage.exists():
            self.storage.mkdir(parents=True)

        for path in self.filenames:
            filename = path.name

            if not path.exists():
                print(f"Downloading {path}...")
                data = self.from_github(filename)
                with open(path, "w") as f:
                    f.write(data)
            print(f"{filename} ready.")
        print()

    def from_github(self, filename: str) -> str:
        data = requests.get(
            f"https://raw.githubusercontent.com/lfrati/wordnetter/main/{filename}"
        )
        if data.ok:
            return data.text
        raise RuntimeError

    def uninstall(self):
        print("Deleting", self.storage)
        shutil.rmtree(self.storage)
        print("Removed.\n")

    def encode(self, text):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()
        n = int(h[:20], 16) % len(self.nouns)
        v = int(h[20:30], 16) % len(self.verbs)
        a = int(h[30], 16) % len(self.adjectives)
        return self.get(n, v, a)

    def encode_file(self, file):
        with open(file, "r") as f:
            text = f.read()
        return self.encode(text)

    def get(self, n, v, a):
        noun = self.nouns[n]
        adj = self.adjectives[a]
        verb = self.verbs[v]
        words = f"{verb}-{adj}-{noun}"
        return words

    def sample(self):

        n = random.randrange(len(self.nouns))
        v = random.randrange(len(self.verbs))
        a = random.randrange(len(self.adjectives))

        return self.get(n, v, a) + f"-{random.randint(1,999)}"


if __name__ == "__main__":
    wnetter = Wordnetter()
    print(wnetter.sample())
