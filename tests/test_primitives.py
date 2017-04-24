import pytest

from basic_utils.primitives import (
    complement, compose, dec, even, identity, inc, odd
)


@pytest.mark.parametrize("data", [
    (10), ((10, 20)), (("Homer", "Marge"))
])
def test_identity(data):
    """Tests that identity returns the same arguments as it was passed"""
    assert identity(data) == data


def test_compose():
    assert compose(complement, even)(3)
    assert compose(complement, odd)(2)


def test_complement():
    fn = complement(even)
    assert fn(5)
    fn = complement(lambda x: x.startswith('a'))
    assert fn('grapple')


def test_primitives():
    assert inc(1) == 2
    assert dec(2) == 1
    assert even(2)
    assert not even(1)
    assert odd(1)
    assert not odd(2)
