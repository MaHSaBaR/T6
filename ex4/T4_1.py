import numpy as np

def read_matrix(file_name):
    with open(file_name) as f:
        reader = f.readlines()

        n, m = map(int, reader[0].split())
        matrices = []

        for i in range(1, n * m + 1, m):
            matrix_data = [list(map(float, row.split())) for row in reader[i:i+m]]
            matrices.append(np.array(matrix_data))

    return matrices

def main():
    file_name = input('Enter file name: ') + '.txt'
    matrices = read_matrix(file_name)

    matrix_dict = {}
    for matrix in matrices:
        determinant = np.linalg.det(matrix)
        matrix_dict[determinant] = matrix

    sorted_determinants = sorted(matrix_dict.keys())
    positive_determinants = [x for x in sorted_determinants if x > 0]
    negative_determinants = [x for x in sorted_determinants if x <= 0]

    if len(positive_determinants) > 1 and len(negative_determinants) > 1:
        if positive_determinants[0] * positive_determinants[1] > negative_determinants[0] * negative_determinants[1]:
            result_matrix = np.matmul(matrix_dict[positive_determinants[0]], matrix_dict[positive_determinants[1]])
        else:
            result_matrix = np.matmul(matrix_dict[negative_determinants[1]], matrix_dict[negative_determinants[0]])
    elif len(positive_determinants) <= 1:
        result_matrix = np.matmul(matrix_dict[sorted_determinants[1]], matrix_dict[sorted_determinants[0]])
    elif len(negative_determinants) <= 1:
        result_matrix = np.matmul(matrix_dict[sorted_determinants.pop()], matrix_dict[sorted_determinants.pop()])

    inverse_matrix = np.linalg.inv(result_matrix)

    for row in inverse_matrix:
        for i, element in enumerate(row[:-1]):
            print(format(element, '.3f'), end=' ')
        print(format(row[-1], '.3f'))

if __name__ == "__main__":
    main()
