class ArgumentCompatibilityException(Exception):
    """Custom Exception for when arguments are incompatible with each other

    Attributes
    ----------
    args -- the arguments that caused the exception
    message -- explanation of the error
    """

    def __init__(self, args: list):
        self.args = args
        self.message = f"The following areguments are incompatible with each other: {args}"
        super().__init__(self.message)
