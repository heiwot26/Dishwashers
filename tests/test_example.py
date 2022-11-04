from example_package.example import add_one
import pytest


def test_add_one_works():
    " Check that the method work as expected"
    number = 1
    assert number + 1 == add_one(number)


def test_add_one_fails():
    " Check that the method fails when it is given a string "
    number = "str"
    with pytest.raises(TypeError):
        add_one(number)
