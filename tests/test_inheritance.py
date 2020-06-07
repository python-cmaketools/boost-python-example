#!/usr/bin/env python

import pytest
from boost_python_example import inheritance

def test_inheritance():
    b = inheritance.Base()
    d = inheritance.Derived()

    assert inheritance.fb(b)=="Base called."
    assert inheritance.fb(d)=="Derived called."

    # not possible, fd is only for Derived objects
    # inheritance.fd(b)
    assert inheritance.fd(d)=="Derived Derived called."

    x = inheritance.factory()
    assert inheritance.fb(x)=="Derived called."

