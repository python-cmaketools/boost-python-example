#!/usr/bin/env python
import pytest
from boost_python_example import classmembers as cm


def test_classmembers():
    m1 = cm.SomeClass("Pavel")
    assert m1.name == "Pavel"
    m1.name = "Gunther"
    assert m1.name == "Gunther"
    n = 7.3
    m1.number = n
    assert(m1.number== -1 if (n>3.141592654) else n)
    n = 2
    m1.number = n
    assert(m1.number== -1 if (n>3.141592654) else n)
