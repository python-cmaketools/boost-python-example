#!/usr/bin/env python
import pytest
from boost_python_example.exceptions import someFunction


def test_exceptions():
    with pytest.raises(UserWarning) as excinfo:
        someFunction()
    assert excinfo.type == UserWarning
    assert str(excinfo.value) == "The meat is gone, go for the cheese...."
