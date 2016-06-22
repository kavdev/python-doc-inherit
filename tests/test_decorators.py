"""
.. module:: tests.decorators
   :synopsis: python-doc-inherit Decorator tests

.. moduleauthor:: Shai Berger [source_]
.. moduleauthor:: Alexander Kavanaugh (@kavdev)

.. _source: http://code.activestate.com/recipes/576862/

"""

from doc_inherit import method_doc_inherit, class_doc_inherit
from unittest.case import TestCase


class TestMethodDecorators(TestCase):

    def test_inheritance(self):
        class Foo(object):
            def foo(self):
                """Frobber"""
                pass

        class Bar(Foo):
            @method_doc_inherit
            def foo(self):
                pass

        self.assertTrue(Bar.foo.__doc__ == Bar().foo.__doc__ == Foo.foo.__doc__ == "Frobber")


class TestClassDecorators(TestCase):

    def test_inheritance(self):
        class Foo(object):
            def foo(self):
                """Frobber"""
                pass

        @class_doc_inherit
        class Bar(Foo):
            def foo(self):
                pass

        self.assertTrue(Bar.foo.__doc__ == Bar().foo.__doc__ == Foo.foo.__doc__ == "Frobber")

    def test_method_docstring_isnt_overridden(self):
        class Foo(object):
            def foo(self):
                """Frobber"""
                pass

        @class_doc_inherit
        class Bar(Foo):
            def foo(self):
                """Blobber"""
                pass

        self.assertTrue(Bar.foo.__doc__ == Bar().foo.__doc__ == "Blobber")
        self.assertFalse(Bar.foo.__doc__ == Foo.foo.__doc__)
