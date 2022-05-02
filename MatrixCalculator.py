import numpy as np


class ProcessMatrix:
    """ Creates a matrix.
    """
    initial_matrix = list[list]
    new_matrix = list
    record = list[str]
    edits = list[str]

    def __init__(self, initial_matrix: list[list]) -> None:
        """ Initializes a matrix.
        Precondition: initial_matrix is not None
        """
        self.matrix = np.array(initial_matrix)
        self.new_matrix = []
        self.record = []
        self.edits = []

    def __str__(self) -> str:
        """Return a str representation of the matrix"""
        s = ''
        for matrices in range(0, len(self.new_matrix)):
            s += f'=== Matrix {matrices + 1} === \n\n'
            s += f'{self.new_matrix[matrices]} \n\n'
        for records in self.record:
            s += f'=== Process for Matrix {self.record.index(records) + 1} === \n\n'
            s += records
        return f'{s}'

    def _record_process(self, record: str) -> None:
        self.record.append(record)

    def _record_edits(self, record: str) -> None:
        self.edits.append(record)


class Matrix(ProcessMatrix):
    """ Processes simple arithmetic calculations between
    two matrices.
    """
    initial_matrix = list[list]

    def __init__(self, initial_matrix) -> None:
        """Inherits ProcessMatrix's properties
        """
        ProcessMatrix.__init__(self, initial_matrix)

    def add_matrix(self, other: list[list]) -> None:
        """ Adds two matrices together.
        Precondition: len(self.matrix[0]) == len(other)
        """
        second = np.array(other)
        self._record_process(f'{self.matrix}\n' + ' ' * 2 *
                             min(len(self.matrix[0]), len(other[0])) + '+' + f'\n{second}\n\n')
        self.new_matrix.append(self.matrix + second)

    def multiply_matrix(self, other: list[list]) -> None:
        """ Multiplies two matrices together.
        """
        second = np.array(other)
        self._record_process(f'{self.matrix}\n' + ' ' * 2 *
                             min(len(self.matrix[0]), len(other[0])) + 'x' + f'\n{second}\n\n')
        self.new_matrix.append(self.matrix.dot(second))

    def sub_matrix(self, other: list[list]) -> None:
        """ Subtracts two matrices together.
        Precondition: len(self.matrix[0]) == len(other)
        """
        second = np.array(other)
        self._record_process(f'{self.matrix}\n' + ' ' * 2 *
                             min(len(self.matrix[0]), len(other[0])) + '-' + f'\n{second}\n\n')
        self.new_matrix.append(self.matrix - second)

    def edit(self, edit_matrix: list[list]) -> None:
        """ Changes initial matrix to a new matrix and records the edit.
        """
        old_matrix = self.matrix
        self.matrix = np.array(edit_matrix)
        self._record_edits(f'Edited\n{old_matrix}\n\nto\n\n{self.matrix}\n\n')

    def reset(self) -> None:
        """ Resets all attributes.
        """
        self.new_matrix = []
        self.record = []
        self.edits = []


if __name__ == '__main__':
    matrix = Matrix([[2, 4], [5, -6]])
    matrix.add_matrix([[9, -3], [3, 6]])
    matrix.multiply_matrix([[9, -3], [3, 6]])
    matrix.sub_matrix([[9, -3], [3, 6]])
    matrix.edit([[1, 2], [2, 3]])
    matrix.add_matrix([[9, -3], [3, 6]])
    print(matrix)
    matrix.reset()
    matrix.edit([[0, 0, 0], [1, 0, 1], [2, 0, 2]])
    matrix.multiply_matrix([[1, -1, 1], [1, -2, 1], [1, 3, 5]])
    print(matrix)
