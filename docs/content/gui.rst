GUI Dialogs
===========

The ``psychos.gui`` module provides a simple graphical user interface (GUI) class for displaying dialogs and basic forms during experiments. It is based on Python's built-in ``tkinter`` library and allows researchers to easily present confirmation dialogs or forms for gathering participant or experiment information.

Dialogs
-------

Class for creating simple GUI dialogs such as confirmation messages and input forms, suitable for collecting participant data or setting up initial experiment conditions.

.. autosummary::
   :toctree: autosummary

   psychos.gui.Dialog

Compatibility Note
------------------

The GUI dialogs depend on Python's ``tkinter`` module. While typically pre-installed on standard Python distributions, some Linux distributions require manual installation. If you encounter issues related to ``tkinter``, ensure it is installed and configured correctly on your system.
