import builtins
import typing
from unittest.mock import patch

from pyparsing import (
    Word, alphas, alphanums, delimitedList, infixNotation, nestedExpr, opAssoc,
    ParseException
)

from .errors import UnsupportedTypeString


def parse(type_string: str, *, func=None):
    """Parse the given type string.

    Args:
        type_string (str): The type string to be parsed.
        func (function): The function to which the type string belongs (optional).
                         This causes the type string to be evaluated in func's context.

    Returns:
        The corresponding typing instance (or type).
    """
    try:
        token, = EXPR.parseString(type_string, parseAll=True).asList()
    except ParseException:
        raise UnsupportedTypeString(type_string) from None
    type_hint = convert(token)

    if func is None:
        def func(x: type_hint):
            pass
        tp = typing.get_type_hints(func, {}, {})['x']
    else:
        with patch.object(func, '__annotations__', dict(x=type_hint)):
            tp = typing.get_type_hints(func)['x']
    return tp


class TokenGroup:
    def convert(self):
        """Convert the token group to a `typing` instance."""
        raise NotImplementedError


class Tuple(TokenGroup):
    def __init__(self, tokens):
        self.args = tuple(tokens.asList()[0])

    def convert(self):
        return typing.Tuple[self.args]


class BinaryOperatorGroup(TokenGroup):
    def __init__(self, tokens):
        self.left, self.right = tokens[0][0::2]


class Sequence(BinaryOperatorGroup):
    def convert(self):
        return getattr(typing, self.left.capitalize())[convert(self.right)]


class Union(BinaryOperatorGroup):
    def convert(self):
        return typing.Union[convert(self.left), convert(self.right)]


def convert(obj: typing.Union[str, TokenGroup]):
    """Convert the given object to a typing instance unless it is a string."""
    if isinstance(obj, TokenGroup):
        return obj.convert()
    return obj


NAME = Word(alphas + '_', alphanums + '_')
TUPLE = nestedExpr(content=delimitedList(NAME)).setParseAction(Tuple)

EXPR = infixNotation(
    NAME | TUPLE,
    [('of', 2, opAssoc.RIGHT, Sequence),
     ('or', 2, opAssoc.RIGHT, Union)],
)
