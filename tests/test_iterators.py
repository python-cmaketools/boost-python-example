#!/usr/bin/env python

from sys import stdout
import pytest
from boost_python_example.iterators import Example

def test_iterators():
    e = Example()
    content = ["a","b","c"]
    for x in content:
        e.add(x)

    print ([ s for s in e.strings() ])

    assert all([a == b for a, b in zip(e.strings(), content)])
