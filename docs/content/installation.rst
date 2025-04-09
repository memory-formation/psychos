Installation
============

**Psychos** is a Python package extending `Pyglet <https://pyglet.org/>`_ designed specifically for creating psychophysics and timing-sensitive behavioral experiments. Its unique required dependency is `Pyglet>=2.0`.

**Psychos** is compatible with Python versions >=3.8 and supports Linux, macOS, and Windows platforms.

Stable releases can be easily installed via PyPI using any Python package manager:

.. code-block:: bash

    pip install psychos

Optional Dependencies
---------------------

Some modules in **Psychos** have optional dependencies:

- `NumPy <https://numpy.org/>`_: Required for certain stimuli types, such as Gabor patches.
- `Pyserial <https://pypi.org/project/pyserial/>`_ and `Pyparallel <https://github.com/pyparallel/pyparallel>`_: Necessary for communication modules or sending triggers to external devices.

These optional dependencies can be installed separately as needed, or collectively by running:

.. code-block:: bash

    pip install psychos[extra]

Troubleshooting
---------------

If you encounter interface-related errors, ensure that `Pyglet` is correctly installed and compatible with your system. Refer to the official `Pyglet documentation <https://pyglet.readthedocs.io/>`_ for guidance.

If you identify issues specifically related to **Psychos**, please open an issue on the `Psychos GitHub repository <https://github.com/memory-formation/psychos/issues>`_.

.. note::

    **Psychos** has been tested with `Pyglet>=2.0`. If you encounter compatibility issues with newer versions of `Pyglet`, please verify whether the package functions correctly with `Pyglet>=2.0,<2.1`. We encourage you to open an issue if you detect that recent changes in `Pyglet` introduce incompatibilities or break existing functionality.

Development Installation
------------------------

For development purposes, extra dependencies to run tests and build documentation can be installed via:

.. code-block:: bash

    pip install psychos[docs,test]

To install the latest development version directly from GitHub (e.g., from the master branch), use:

.. code-block:: bash

    pip install git+https://github.com/memory-formation/psychos/

