"""
Centralized logging utility to control verbose output across the project.
"""

_VERBOSE: bool = False


def set_verbose(enabled: bool) -> None:
    """
    Enables or disables the verbose mode globally.
    """
    global _VERBOSE
    _VERBOSE = enabled


def log(message: str) -> None:
    """
    Prints the message only if verbose mode is enabled.
    """
    if _VERBOSE:
        print(message)
