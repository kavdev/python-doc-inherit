"""
.. module:: doc_inherit.decorators
   :synopsis: python-doc-inherit Decorators

.. moduleauthor:: Shai Berger [source1_]
.. moduleauthor:: Martijn Pieters [source2_]

.. _source1: http://code.activestate.com/recipes/576862/
.. _source2: http://stackoverflow.com/a/17393254

"""

from inspect import getmembers, isroutine, ismethod
from functools import wraps


class DocInherit(object):
    """
    Docstring inheriting method descriptor

    The class itself is also used as a decorator.
    """

    def __init__(self, method):
        self.method = method
        self.name = method.__name__

    def __get__(self, obj, cls):
        if obj:
            return self.get_with_inst(obj, cls)
        else:
            return self.get_no_inst(cls)

    def get_with_inst(self, obj, cls):
        overridden = getattr(super(cls, obj), self.name, None)

        @wraps(self.method, assigned=('__name__', '__module__'))
        def func(*args, **kwargs):
            return self.method(obj, *args, **kwargs)

        return self.use_parent_doc(func, overridden)

    def get_no_inst(self, cls):

        for parent in cls.__mro__[1:]:
            overridden = getattr(parent, self.name, None)
            if overridden:
                break

        @wraps(self.method, assigned=('__name__', '__module__'))
        def func(*args, **kwargs):
            return self.method(*args, **kwargs)

        return self.use_parent_doc(func, overridden)

    def use_parent_doc(self, func, source):
        if source is None:
            raise NameError("Can't find '{name}' in parents".format(name=self.name))

        func.__doc__ = source.__doc__
        return func


def class_inherit_docstrings(cls):
    for name, func in getmembers(cls, isroutine):
        if ismethod(func):
            func = func.__func__

        if func.__doc__:
            continue

        for parent in cls.__mro__[1:]:
            if hasattr(parent, name):
                func.__doc__ = getattr(parent, name).__doc__

    return cls
