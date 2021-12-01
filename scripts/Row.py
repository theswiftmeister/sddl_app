from scripts.Cell import Cell


class Row(object):
    def __init__(self, data_list: list) -> None:
        """
        (class)

        Row object.
        Params :
                row_number : row number in table
                data_list : list -> list of items
        """
        super().__init__()
        self.row_item = [Cell() for i in range(len(data_list))]
        self.set_item(data_list)

    def set_item(self, list):
        for col, cell in enumerate(self.row_item):
            cell.set_item(col, list[col])

    def get_item(self):
        """
        (method)

        Getter\ns
        Return:
                self.row_item : list of cells
        """
        return self.row_item

    def get_name_cell(self):
        """(method)

        Returns the cell which contains name text.
        dev pref.
        index = 1, as per [date,name,...]"""
        return self.row_item[1]

    def get_unit_cell(self):
        """(method)

        Returns the cell which contains unit text.
        dev pref.
        index = 1, as per [date,name,unit...]"""
        return self.row_item[2]

    def get_row_texts(self):
        return [cell.get_text() for cell in self.get_item()]
