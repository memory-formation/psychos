Sound
=====

The ``psychos.sound`` module provides functionality for reproducing sound stimuli (synthetic or from `.wav` files) during experiments. It builds upon `pyglet.media` to manage sound playback efficiently.

Sounds
------

Functions and classes to create sound stimuli for playback during experiments.

.. autosummary::
   :toctree: autosummary

   psychos.sound.load_sound
   psychos.sound.Sawtooth
   psychos.sound.Silence
   psychos.sound.Sine
   psychos.sound.Square
   psychos.sound.Triangle
   psychos.sound.WhiteNoise

Envelopes
---------

Classes to create envelopes for controlling sound volume dynamics over time.

.. autosummary::
   :toctree: autosummary

   psychos.sound.Envelope
   psychos.sound.FlatEnvelope
   psychos.sound.LinearDecayEnvelope
   psychos.sound.TremoloEnvelope

Player
------

Pyglet classes for advanced sound management, such as grouping multiple sounds for simultaneous playback or continuous streaming scenarios.

.. autosummary::
   :toctree: autosummary

   psychos.sound.Player
   psychos.sound.PlayerGroup
   psychos.sound.StaticSource
   psychos.sound.StreamingSource

Compatibility Troubleshooting
-----------------------------

All sound functionalities in **Psychos** rely on the pyglet implementation, which attempts to locate a compatible audio driver on your system. If you encounter issues with sound playback or compatibility, consult the `Pyglet media documentation <https://pyglet.readthedocs.io/en/latest/programming_guide/media.html>`_ for guidance on installing or troubleshooting compatible audio drivers.

The default settings typically work well for most platforms (Linux, macOS, Windows).
