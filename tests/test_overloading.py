#!/usr/bin/env python

import pytest
from boost_python_example.overloading import Example


def test_overloading():
    e = Example()

    e.doit()
    assert str(e) == "void"
    assert str(e.doit(2)) == "2"
    e.doit("Hallo")
    assert str(e) == "Hallo"

    assert e.makeIt("xxx", 1) == 1 and str(e) == "xxx"
    assert e.makeIt("abc", 2) == 2 and str(e) == "abcabc"
    assert e.makeIt("xyz", 3, "abc") == 4 and str(e) == "xyzxyzxyzabc"
