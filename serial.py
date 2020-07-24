"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Make a new number generator that starts at start"""
        self.start = start
        self.current_value = start

    def __repr__(self):
        """Show a representation of the class"""
        return f"SerialGenerator(start={self.start})"

    def generate(self):
        """Return the next number in the sequence"""
        result = self.current_value
        self.current_value += 1
        return result

    def reset(self):
        """Reset the value back to original start value"""
        self.current_value = self.start
