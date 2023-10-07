def define_matrix(e1, e2, e3, e4, e5, e6, e7):
    matrix = [
        [0, 0, 0, 0, 0, 0, 4*e1],
        [e5-e6, 0, 0, 0, 0, e1, 3*e2],
        [-e5, -e3, 0, -e1, 0, e2, 2*e3],
        [-e3-2*e4, 0, -e2, 0, e2, 0, e3+2*e4],
        [-2*e3, ],
        [-3*e2, ],
        [-4*e1, ]
    ]


def define_small_matrix(e1, e2, e3):

    def get_value(x1, x2):
        index_1 = int(x1[1:]) - 1
        index_2 = int(x2[1:]) - 1

        return matrix[index_1][index_2]

    def lie_multiply(x1, x2, i, j, k):
        if x1 == x2 or x1 == '0' or x2 == '0':
            # return '0' + "(" + str(i) + ", " + str(j) + ", " + str(k) + ")"
            return '0'
        else:
            print("here = ", "index: ", x1, ", ", x2)
            # return get_value(x1, x2) + "(" + str(i) + ", " + str(j) + ", " + str(k) + ")"
            return get_value(x1, x2)

    params = [
        e1, e2, e3
    ]

    matrix = [
        ['0', e3, e2],
        ['0', '0', e1],
        [e1, '0', '0']
    ]

    sumLie = []
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):

                if k == j or k == i:
                    continue

                sumLie.append(
                    lie_multiply(matrix[i][j], params[k], i, j, k)
                )

    return sumLie


if __name__ == '__main__':
    ans = define_small_matrix('e1', 'e2', 'e3')
    print("ans:", ans)



