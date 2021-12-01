
class Cell(object):
    def __init__(self) -> None:
        """
        (class)

        Cell object
        """
        super().__init__()
        self.column = 0
        self.text = 0

    def set_item(self, col: int, text: str):
        """
        (function)
        Setter.\n
        Params : 
                col : int
                text : str
        """
        self.column = col
        self.text = text

    def get_item(self):
        """
        (function)
        Getter\n
        Return :
                Tuple consisting (col,text)
        """
        return (self.column, self.text)

    def get_text(self):
        """(method)
        Returns : self.text"""
        return self.text

    def set_text(self, text):
        """(method)
        Sets self.text"""
        self.text = text

    def get_column(self):
        """(method)
        Returns : self.column """
        return self.column

    def set_column(self, column):
        """(method)
        Sets self.column """
        self.column = column
