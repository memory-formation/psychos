Triggers
========

The ``psychos.triggers`` module provides classes and functions for sending triggers and signals to external devices. It's designed to simplify interactions with external hardware by providing a unified API and encapsulating repetitive logic, making it easier to synchronize behavioral experiments with external equipment.

Ports
-----

Classes for sending signals to different communication ports, providing a unified and easy-to-use API for port communication and management.

.. autosummary::
   :toctree: autosummary

   psychos.triggers.get_port
   psychos.triggers.DummyPort
   psychos.triggers.SerialPort
   psychos.triggers.ParallelPort
   psychos.triggers.BasePort

Triggers
--------

Classes designed to send triggers through communication ports, encapsulating repetitive logic and providing utility methods to handle timing and trigger patterns conveniently.

.. autosummary::
   :toctree: autosummary

   psychos.triggers.StepTrigger
   psychos.triggers.DelayTrigger
   psychos.triggers.BaseTrigger
   
