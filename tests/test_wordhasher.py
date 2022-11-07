from itertools import chain, combinations
import pytest
from tqdm import trange

from wordhasher import *


def subsets(s):
    opts = chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))
    yield from ["".join(opt) for opt in opts]


def test_wrong_mode():
    wh = WordHasher()
    with pytest.raises(AssertionError):
        wh.sample(mode="nvaNk")


def test_collisions():
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
    assert len(seen) == N


def test_sampling():
    wh = WordHasher()
    modes = subsets(wh.modes)
    for mode in modes:
        try:
            wh.sample(mode=mode)
        except AssertionError:
            pytest.fail(f"Invalid sampling mode : {mode}")
    with pytest.raises(AssertionError):
        wh.sample(mode="")
