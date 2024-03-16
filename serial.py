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

    def __init__(self, start = 0):
        """initialize a new generator with a start."""

        self.start = self.next = start

    def __repr__(self):
        """Representation for a clean output in terminal."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """generate and return next serial."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to the original start inputted by user."""

        self.next = self.start

