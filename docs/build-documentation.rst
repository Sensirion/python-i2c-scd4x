Build documentation
===================

The documentation is built with `Sphinx <http://www.sphinx-doc.org>`_:

.. code-block:: bash

    python setup.py install                        # Install package
    pip install -r docs/requirements.txt           # Install requirements
    sphinx-build -b html docs docs/_build/html     # Build documentation
