from typing import List, Tuple, Union

import pytest

from typestring_parser import parse
from typestring_parser.errors import UnsupportedTypeString


def test_parse_simple_type():
    assert parse("int") is int
    assert parse("str") is str


def test_parse_union():
    assert parse("int or str") == Union[int, str]


def test_parse_list():
    assert parse("list of int") == List[int]


def test_parse_list_of_list():
    assert parse("list of list of int") == List[List[int]]


def test_parse_list_and_union():
    assert parse("list of int or str") == Union[List[int], str]


def test_parse_tuple():
    assert parse("(int, str)") == Tuple[int, str]


def test_parse_list_of_tuple():
    assert parse("list of (int, str)") == List[Tuple[int, str]]


def test_parse_list_and_union_and_tuple():
    assert (
        parse("int or list of (str, str) or float")
        == Union[int, List[Tuple[str, str]], float]
    )


class _CustomType:
    pass


def test_parse_custom_type():
    def func():
        pass

    with pytest.raises(NameError):
        parse("list of _CustomType")

    assert parse("list of _CustomType", func=func) == List[_CustomType]


def test_parse_raise_on_unsupported_type_string():
    with pytest.raises(UnsupportedTypeString) as excinfo:
        parse("int and str")

    assert str(excinfo.value) == "int and str"
