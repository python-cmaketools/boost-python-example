#!/usr/bin/env python

import pytest
from boost_python_example import constructors as ctor


def test_constructors():

    c1 = ctor.Ctor("Bonjour")
    assert c1.greet() == "Bonjour"

    c2 = ctor.Ctor(3.141592654, 1.0)
    assert c2.greet() == "3:1"
