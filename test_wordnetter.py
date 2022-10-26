from wordnetter import Wordnetter
from tqdm import trange

wnetter = Wordnetter()
print()
wnetter.uninstall()
wnetter.install()

test_string = "This is a test!"
print(f"\n Test string: {test_string}\nWordnet-hash: {wnetter.encode(test_string)}\n")

file = __file__
print(f"Self encoding: {file}\n Wordnet-hash: {wnetter.encode_file(file)}\n")

print("Checking for collisions")
N = 10_000_0
seen = set()
for i in trange(N):
    sample = wnetter.sample()
    if sample not in seen:
        seen.add(sample)
    else:
        print(f"Collision after {i} samples. Unlucky :(")
        break
else:
    print(f"{N - len(seen)} collisions in {N:_} samples.\n")
