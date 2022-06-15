import fileinput


def postac_schodkowa(matrix, right):

    if not matrix: 
        return

    lead = 0
    row_number = len(matrix)
    column_number = len(matrix[0])

    for curr_row in range(row_number):
        if lead >= column_number: 
            return
        i = curr_row

        while matrix[i][lead] == 0:
            i += 1
            if i == row_number:
                i = curr_row
                lead += 1
                if column_number == lead:
                    return

        matrix[i], matrix[curr_row], right[curr_row], right[i] = matrix[curr_row], matrix[i], right[i], right[curr_row]
        first_el = matrix[curr_row][lead]

        matrix[curr_row] = [row / float(first_el) for row in matrix[curr_row]]
        right[curr_row] = right[curr_row] / float(first_el)

        for i in range(row_number):
            if i != curr_row:
                first_el = matrix[i][lead]
                matrix[i] = [i_row_el - first_el * curr_row_el for curr_row_el, i_row_el in zip(matrix[curr_row],matrix[i])]
                right[i] = right[i] - first_el * right[curr_row]

        lead += 1
 
 
def printMatrix(matrix, right):
    for i in range(0, len(matrix)):
        print(str(', '.join((str(abs(el)) for el in matrix[i]))) + " | " + str(right[i]))


def number_of_solutions(matrix, right):
    if not matrix: 
        return

    extended_mtx = [[] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            extended_mtx[i].append(matrix[i][j])


    number_of_unknown_vals = len(matrix[0])
    rank_of_basic_mtx = 0
    rank_of_extended_mtx = 0

    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            rank_of_basic_mtx += 1
        # num_of_zero_vals = 0
        # for j in range(len(matrix[i])):
        #     if matrix[i][j] == 0:
        #         num_of_zero_vals += 1

        # if num_of_zero_vals < len(matrix[i]) and sum(matrix[i]) != 0:
        #     rank_of_basic_mtx += 1

    for i in range(len(extended_mtx)):
        if extended_mtx[i][-1] != 0:
            rank_of_extended_mtx += 1
        # num_of_zero_vals = 0
        # for j in range(len(extended_mtx[i])):
        #     if matrix[i][j] == 0:
        #         num_of_zero_vals += 1

        # if num_of_zero_vals < len(extended_mtx[i]):
        #     rank_of_extended_mtx += 1


    print(rank_of_basic_mtx)
    print(rank_of_extended_mtx)

    if rank_of_basic_mtx == rank_of_extended_mtx and rank_of_basic_mtx == number_of_unknown_vals:
        return 1
    elif rank_of_basic_mtx == rank_of_extended_mtx and rank_of_basic_mtx < number_of_unknown_vals:
        return 0
    elif rank_of_basic_mtx != rank_of_extended_mtx:
        return -1


def main():

    matrix = []
    right = []

    for line in fileinput.input():
        row = list(line.split(" "))
        row = [float(num) for num in row]
        matrix.append(row[:-1])
        right.append(row[-1])

    # print(matrix)

    postac_schodkowa(matrix, right)

    right = list(map(lambda x: round(x, 2), right))
    
    printMatrix(matrix, right)

    num_of_solutions = number_of_solutions(matrix, right)

    if num_of_solutions == -1:
        print("Układ jest sprzeczny.")
    elif num_of_solutions == 0:
        print("Układ ma nieskończenie wiele rozwiązań.")
    else:
        print("Układ ma jedno rozwiązanie: " + str(right))


if __name__ == "__main__":
    main()