class SqrMatrix(object):
    def __init__(self, size, matrix):
        self.size = size
        self.matrix = matrix

    def __str__(self):
        output = ""
        for row in self.matrix:
            for value in row:
                output += ('|' + str(value) +'|')
            output += '\n'
        return output

    def diagonals(self):
        left_diagonal, right_diagonal = 0, 0
        for i in xrange(0, self.size-1):
            left_diagonal += self.matrix[i][i]
            right_diagonal += self.matrix[i][-(i+1)]
        return abs(left_diagonal - right_diagonal)
            
def main():
    p = SqrMatrix(  size = 4,
            matrix=[(0,3,4,5),
                    (3,4,5,6),
                    (4,5,6,7)])
    print p    
    print p.diagonals()

if __name__ == "__main__":
    main()

