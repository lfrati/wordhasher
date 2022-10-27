# WordHasher
Hashes are cool. But gosh they are ugly to read...

Let's convert them to verb-noun-adjective form to be more human friendly!

We are going to use [WordNet](https://wordnet.princeton.edu/) to get some words and [hashlib](https://docs.python.org/3/library/hashlib.html) to get some hashes.

# Example
``` python
from wordhasher import WordHasher
whash = WordHasher()

print(whash.encode("This is a test!")    # monkey-abeyant-boxthorn
print(whash.encode_file("wordhasher.py") # proclaim-ablated-molting
print(whash.encode("This is a test!")    # bundle-overshot-viewer-186
```

## Credits
> Princeton University "About WordNet." WordNet. Princeton University. 2010. 
