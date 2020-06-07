#!/usr/bin/env python

import pytest
from boost_python_example.virtualfunctionsinpython import Base, identify


class PythonDerived(Base):
    def name(self):
        return "PythonDerived"


def test_virtualfunctionsinpython():
    b = Base()
    assert identify(b)=="Base called."

    p = PythonDerived()
    assert identify(p)=="PythonDerived called."
