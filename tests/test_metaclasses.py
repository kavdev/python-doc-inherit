"""
.. module:: tests.decorators
   :synopsis: python-doc-inherit Decorator tests

.. moduleauthor:: unutbu [source1_]

.. _source1: http://stackoverflow.com/questions/8100166/inheriting-methods-docstrings-in-python

"""

from doc_inherit.metaclasses import DocStringInheritor
from unittest.case import TestCase
from six import add_metaclass


class TestMetaClass(TestCase):
    def test_null(self):
        class Foo(object):
            def frobnicate(self):
                pass

        @add_metaclass(DocStringInheritor)
        class Bar(Foo):
            pass

        self.assertEqual(Bar.__doc__, object.__doc__)
        self.assertEqual(Bar().__doc__, object.__doc__)
        self.assertEqual(Bar.frobnicate.__doc__, None)

    def test_with_other_decorators(self):
        class Animal(object):
            def move_to(self, dest):
                """Move to *dest*"""
                pass

        def check_docstring(func):
            # Check that this will still work.
            assert True
            return func

        @add_metaclass(DocStringInheritor)
        class Bird(Animal):
            @check_docstring
            def move_to(self, dest):
                pass

        self.assertEqual(Animal.move_to.__doc__, Bird.move_to.__doc__)

    def test_method_has_docstring(self):
        class Animal(object):
            def move_to(self, dest):
                """Move to *dest*"""
                pass

        @add_metaclass(DocStringInheritor)
        class Bird(Animal):
            def move_to(self, dest):
                """ Existing docstring."""

                pass

        self.assertEqual(""" Existing docstring.""", Bird.move_to.__doc__)

    def test_inherit_from_parent(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'

        @add_metaclass(DocStringInheritor)
        class Bar(Foo):
            pass

        self.assertEqual(Foo.__doc__, 'Foo')
        self.assertEqual(Foo().__doc__, 'Foo')
        self.assertEqual(Bar.__doc__, 'Foo')
        self.assertEqual(Bar().__doc__, 'Foo')
        self.assertEqual(Bar.frobnicate.__doc__, 'Frobnicate this gonk.')

    def test_inherit_from_mro(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'

        class Bar(Foo):
            pass

        @add_metaclass(DocStringInheritor)
        class Baz(Bar):
            def frobnicate(self):
                pass

        self.assertEqual(Baz.__doc__, 'Foo')
        self.assertEqual(Baz().__doc__, 'Foo')
        self.assertEqual(Baz.frobnicate.__doc__, 'Frobnicate this gonk.')

    def test_inherit_metaclass_(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'

        @add_metaclass(DocStringInheritor)
        class Bar(Foo):
            pass

        class Baz(Bar):
            def frobnicate(self):
                pass

        self.assertEqual(Baz.__doc__, 'Foo')
        self.assertEqual(Baz().__doc__, 'Foo')
        self.assertEqual(Baz.frobnicate.__doc__, 'Frobnicate this gonk.')
