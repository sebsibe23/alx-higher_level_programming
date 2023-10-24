class Square:
    """
    Class Name: Square
    Attributes:
    - size: size of a square (1 side).

    This class defines properties of a square.
    """

    def __init__(self, size=0):
        """
        Function Name: __init__
        Parameters:
        - size: size of the square (1 side).

        This function creates new instances of square.
        """
        self.__size = size

    def area(self):
        """
        Function Name: area

        This function calculates the area of square and returns it.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Function Name: size

        This function returns the size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function Name: size
        Parameters:
        - value: new size of a square (1 side).

        This function sets the size of a square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

