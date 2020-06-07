#!/usr/bin/env python

import pytest
from boost_python_example.operators import NumberLike


def test_operators():
    n = NumberLike(7)
    m = n + 2
    assert str(m) == "9"

    n0 = NumberLike()
    m0 = n0 + 1
    assert str(m0) == "1"

    assert repr(m0) == "NumberLike(1)"
