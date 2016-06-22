"""
.. module:: doc_inherit.metaclasses
   :synopsis: python-doc-inherit MetaClass Decorators

   This is a more robust version of the ``method_doc_inherit`` decorator that uses
   a metaclass in order to not break other method decorators.

http://stackoverflow.com/questions/8100166/inheriting-methods-docstrings-in-python

"""


class DocStringInheritor(type):
    """"A variation on
    http://groups.google.com/group/comp.lang.python/msg/26f7b4fcb4d66c95
    by Paul McGuire

    http://stackoverflow.com/questions/8100166/inheriting-methods-docstrings-in-python
    """

    def __new__(meta, name, bases, clsdict):
        if not('__doc__' in clsdict and clsdict['__doc__']):
            for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()):
                doc = mro_cls.__doc__
                if doc:
                    clsdict['__doc__'] = doc
                    break
        for attr, attribute in clsdict.items():
            if not attribute.__doc__:
                for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()
                                if hasattr(mro_cls, attr)):
                    doc = getattr(getattr(mro_cls, attr), '__doc__')
                    if doc:
                        attribute.__doc__ = doc
                        break
        return type.__new__(meta, name, bases, clsdict)
