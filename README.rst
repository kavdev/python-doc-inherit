==================
python-doc-inherit
==================
A decorator used to inherit method documentation from parent classes.

Badges
------

.. image:: https://img.shields.io/travis/kavdev/python-doc-inherit/master.svg?style=flat-square
        :target: https://travis-ci.org/kavdev/python-doc-inherit
.. image:: https://img.shields.io/codecov/c/github/kavdev/python-doc-inherit/master.svg?style=flat-square
        :target: http://codecov.io/github/kavdev/python-doc-inherit?branch=master
.. image:: https://img.shields.io/requires/github/kavdev/python-doc-inherit.svg?style=flat-square
        :target: https://requires.io/github/kavdev/python-doc-inherit/requirements/?branch=master
.. image:: https://img.shields.io/codacy/75dbe2685efe47c3aa203a53154c9e7e.svg?style=flat-square
        :target: https://www.codacy.com/app/kavanaugh-development/python-doc-inherit/dashboard

.. image:: https://img.shields.io/pypi/v/python-doc-inherit.svg?style=flat-square
        :target: https://pypi.python.org/pypi/python-doc-inherit
.. image:: https://img.shields.io/pypi/dw/python-doc-inherit.svg?style=flat-square
        :target: https://pypi.python.org/pypi/python-doc-inherit

.. image:: https://img.shields.io/github/issues/kavdev/python-doc-inherit.svg?style=flat-square
        :target: https://github.com/kavdev/python-doc-inherit/issues
.. image:: https://img.shields.io/github/license/kavdev/python-doc-inherit.svg?style=flat-square
        :target: https://github.com/kavdev/python-doc-inherit/blob/master/LICENSE

Usage
-----

Install python-doc-inherit:

.. code-block:: bash

    pip install python-doc-inherit

Put it to use:

.. code-block:: python

    from doc_inherit import method_doc_inherit

    class Foo(object):

        def foo(self):
            """Frobber"""

            pass
    
    class Bar(Foo):

        @method_doc_inherit
        def foo(self):
            pass 

Now, ``Bar.foo.__doc__ == Bar().foo.__doc__ == Foo.foo.__doc__ == "Frobber"``


Running the Tests
------------------

.. code-block:: bash

    pip install -r requirements/test.txt
    ./runtests.py
