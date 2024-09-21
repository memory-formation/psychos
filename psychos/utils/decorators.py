import functools
from typing import Callable

__all__ = ["docstring"]


def docstring(from_method: Callable) -> Callable:
    """
    Decorator that copies the docstring from one method to another.

    Parameters
    ----------
    from_method : callable
        The method to copy the docstring from.

    Returns
    -------
    callable
        The decorated method with the copied docstring.
    """

    def decorator(to_method):
        # Copy the docstring from the source method to the target method
        to_method.__doc__ = from_method.__doc__
        return functools.update_wrapper(to_method, from_method)

    return decorator
