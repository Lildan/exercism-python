class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        lines = matrix_string.split('\n')
        for line in lines:
            self.matrix.append([int(num) for num in line.split(' ')])


    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
