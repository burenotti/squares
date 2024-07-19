__all__ = ["SquaresError", "InvalidArgumentsError"]


class SquaresError(Exception):
    """
    Base exception class for this library
    """

    pass


class InvalidArgumentsError(SquaresError):
    """
    This class of exception will be raised if some of
    the provided arguments are invalid: non-positive radius or sides,
    non-existing triangle, etc.
    """

    pass
