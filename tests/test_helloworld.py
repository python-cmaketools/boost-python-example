#!/usr/bin/env python

from boost_python_example import helloworld

def test_hello():
    assert helloworld.greet()=="hello, world"
