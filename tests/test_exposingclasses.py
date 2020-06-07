#!/usr/bin/env python

import pytest
from boost_python_example import exposingclasses as classes


def test_exposingclasses():
    t = classes.World()

    msg = "bom dia!"
    t.set(msg)
    assert t.greet() == msg

    msgs = ["Good Morning", "Buon giorno", "Kali mera"]
    t.many(msgs)
    assert t.greet() == ", ".join(msgs)
