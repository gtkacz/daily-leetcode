class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = {chr(c): {} for c in range(65, 91)}

    def setCell(self, cell: str, value: int) -> None:
        key, index = cell[0], cell[1:]

        self.spreadsheet[key][index] = value

    def resetCell(self, cell: str) -> None:
        key, index = cell[0], cell[1:]

        if index not in self.spreadsheet[key]:
            return

        del self.spreadsheet[key][index]

    def getCellValue(self, cell: str) -> int:
        key, index = cell[0], cell[1:]

        return self.spreadsheet[key].get(index, 0)

    def getValue(self, formula: str) -> int:
        x, y = formula.removeprefix('=').split('+')

        x = int(x) if x.isdigit() else self.getCellValue(x)
        y = int(y) if y.isdigit() else self.getCellValue(y)

        return x + y
