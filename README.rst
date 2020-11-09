typestring parser
=================

|PyPI| |Python Version| |License|

|Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/typestring-parser.svg
   :target: https://pypi.org/project/typestring-parser/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/typestring-parser
   :target: https://pypi.org/project/typestring-parser
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/typestring-parser
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Tests| image:: https://github.com/Dominik1123/typestring-parser/workflows/Tests/badge.svg
   :target: https://github.com/Dominik1123/typestring-parser/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/Dominik1123/typestring-parser/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Dominik1123/typestring-parser
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Installation
------------

You can install ``typestring-parser`` via pip_ from PyPI_:

.. code:: console

   $ pip install typestring-parser


Usage
-----

Use the ``parse`` function to convert type strings into `typing`_ instances:

.. code:: python

   >>> from typestring_parser import parse
   >>>
   >>> parse('int')
   <class 'int'>
   >>> parse('int or str')
   typing.Union[int, str]
   >>> parse('list of str or str')
   typing.Union[typing.List[str], str]
   >>> parse('list of (int, str)')
   typing.List[typing.Tuple[int, str]]


.. _PyPI: https://pypi.org/
.. _pip: https://pip.pypa.io/
.. _typing: https://docs.python.org/3/library/typing.html
