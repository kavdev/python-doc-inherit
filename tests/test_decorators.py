"""
.. module:: tests.decorators
   :synopsis: python-doc-inherit Decorator tests

.. moduleauthor:: Shai Berger [source_]

.. _source: http://code.activestate.com/recipes/576862/

"""

from doc_inherit import method_doc_inherit
from unittest.case import TestCase


class Foo(object):
    def foo(self):
        """Frobber"""
        pass


class Bar(Foo):
    @method_doc_inherit
    def foo(self):
        pass


class TestDecorators(TestCase):

    def test_inheritance(self):
        self.assertTrue(Bar.foo.__doc__ == Bar().foo.__doc__ == Foo.foo.__doc__ == "Frobber")
