import unittest
from tqdm import trange
from wordhasher import *

from itertools import chain, combinations


def subsets(s):
    opts = chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))
    yield from ["".join(opt) for opt in opts]


class WhasherTests(unittest.TestCase):
    def test_wrong_mode(self):
        wh = WordHasher()
        with self.assertRaises(AssertionError):
            wh.sample(mode="nvaNk")

    def test_collisions(self):
        wh = WordHasher()
        N = 1_000_000
        seen = set()
        for i in trange(N):
            sample = wh.sample()
            if sample not in seen:
                seen.add(sample)
            else:
                print(f"Collision after {i} samples. Unlucky :(")
                break
        self.assertEqual(len(seen), N)

    def test_sampling(self):
        wh = WordHasher()
        modes = subsets(wh.modes)
        for mode in modes:
            try:
                wh.sample(mode=mode)
            except AssertionError:
                self.fail(f"Invalid sampling mode : {mode}")
        with self.assertRaises(AssertionError):
            wh.sample(mode="")


if __name__ == "__main__":
    unittest.main()
