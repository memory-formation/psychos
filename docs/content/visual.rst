Visual
======

The ``psychos.visual`` module provides tools to easily create, display, and control visual stimuli, supporting precise control over timing, appearance, and spatial configuration for behavioral experiments.

Window
------

A Pyglet-based window class used to display, contain, and refresh visual stimuli during experiments.

.. autosummary::
   :toctree: autosummary

   psychos.visual.Window
   psychos.visual.get_window

Visual Stimuli
--------------

Basic building blocks with predefined and parametrizable visual stimuli to easily create behavioral experiments.

.. autosummary::
   :toctree: autosummary

   psychos.visual.Text
   psychos.visual.Image
   psychos.visual.Rectangle
   psychos.visual.BorderedRectangle
   psychos.visual.Gabor
   psychos.visual.RawImage
   psychos.visual.Circle

Units system
------------

Different unit systems to configure the sizes and positions of visual stimuli within the window (e.g., pixels, centimeters, visual degrees, screen percentage, etc.). Most units are transparently integrated into windows and stimuli, but direct access to these classes is provided for custom cases or defining new unit types.

.. autosummary::
   :toctree: autosummary

   psychos.visual.Unit
   psychos.visual.units.PixelUnits
   psychos.visual.units.NormalizedUnits
   psychos.visual.units.PercentageUnit
   psychos.visual.units.VWUnit
   psychos.visual.units.VHUnit
   psychos.visual.units.CMUnit
   psychos.visual.units.VDUnit
   psychos.visual.units.MMUnit
   psychos.visual.units.PTUnit
   psychos.visual.units.DegUnit
   psychos.visual.units.INUnit

Synthetic Stimuli
-----------------

Utility functions for creating synthetic stimuli, such as Gabor patches or scaled textures, useful for generating precise visual stimuli programmatically.

.. autosummary::
   :toctree: autosummary

   psychos.visual.synthetic.gabor_2d
   psychos.visual.synthetic.gabor_3d
   psychos.visual.synthetic.reescale
